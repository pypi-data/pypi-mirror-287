import logging
import operator
from typing import Dict, Sequence, Tuple, Union

import numpy as np
import tensorrt as trt
import torch
from torch.fx.node import Argument, Node, Target
from torch_tensorrt.dynamo._SourceIR import SourceIR
from torch_tensorrt.dynamo.conversion._ConversionContext import ConversionContext
from torch_tensorrt.dynamo.conversion._ConverterRegistry import (
    ConverterRegistry,
    dynamo_tensorrt_converter,
)
from torch_tensorrt.dynamo.conversion.converter_utils import (
    cast_trt_tensor,
    get_trt_tensor,
)
from torch_tensorrt.dynamo.conversion.impl.elementwise import sub, trunc_div
from torch_tensorrt.fx.types import TRTTensor
from torch_tensorrt.fx.utils import Frameworks, unified_dtype_converter

_LOGGER: logging.Logger = logging.getLogger(__name__)


def getitem_validator(getitem_node: Node) -> bool:
    from torch_tensorrt.dynamo.conversion._ConverterRegistry import DYNAMO_CONVERTERS

    # Getitem nodes can only be converted if their parent node also can
    return getitem_node.args[0] in DYNAMO_CONVERTERS


# TODO: Subsequent evaluators should be registered here with their own validators
@dynamo_tensorrt_converter(
    operator.getitem,
    capability_validator=getitem_validator,
    supports_dynamic_shapes=True,
)
@dynamo_tensorrt_converter(torch.ops.aten.detach.default, supports_dynamic_shapes=True)
def generic_evaluator(
    ctx: ConversionContext,
    target: Target,
    args: Tuple[Argument, ...],
    kwargs: Dict[str, Argument],
    name: str,
) -> Union[TRTTensor, Sequence[TRTTensor]]:
    _LOGGER.debug(
        f"Evaluating {ConverterRegistry.qualified_name_or_str(target)} on object with name: {name}"
    )
    return target(*args)


@dynamo_tensorrt_converter(
    torch.ops.aten.arange.start_step, supports_dynamic_shapes=True
)
def aten_ops_arange_start_step(
    ctx: ConversionContext,
    target: Target,
    args: Tuple[Argument, ...],
    kwargs: Dict[str, Argument],
    name: str,
) -> Union[TRTTensor, Sequence[TRTTensor]]:
    # Case where inputs to arange are dynamic
    if any(isinstance(tensor, TRTTensor) for tensor in args):
        start_rank_0 = get_trt_tensor(ctx, args[0], name + "_start_rank_0", min_rank=0)
        start_rank_1 = get_trt_tensor(ctx, args[0], name + "_start_rank_1", min_rank=1)
        end = get_trt_tensor(ctx, args[1], name + "_end", min_rank=1)
        step = args[2] if len(args) > 2 else 1
        step = get_trt_tensor(ctx, step, name + "_step", min_rank=1)
        # Calculate shape = (end-start) / step
        shape = sub(
            ctx,
            target,
            SourceIR.ATEN,
            name + "_sub",
            end,
            start_rank_1,
        )
        shape = trunc_div(
            ctx,
            target,
            SourceIR.ATEN,
            name + "_shape",
            shape,
            step,
        )
        shape = cast_trt_tensor(ctx, shape, end.dtype, name + "_shape_casted")
        fill_layer = ctx.net.add_fill(
            shape.shape, trt.FillOperation.LINSPACE, shape.dtype
        )
        fill_layer.set_input(0, shape)
        # Set start index
        fill_layer.set_input(1, start_rank_0)
        # Set delta/step
        fill_layer.set_input(2, step)
        return fill_layer.get_output(0)
    return np.arange(*args)


def rand_validator(rand_node: Node) -> bool:
    dtype = rand_node.kwargs.get("dtype", None)
    layout = rand_node.kwargs.get("layout", None)
    if dtype is not None:
        _LOGGER.debug(
            f"Currently we don't support specifying output dtype, got {dtype}."
        )
        return False
    if layout is not None:
        _LOGGER.debug(f"Currently we don't support specifying layout, got {layout}.")
        return False
    return True


@dynamo_tensorrt_converter(
    torch.ops.aten.rand.default, capability_validator=rand_validator
)
def aten_ops_rand(
    ctx: ConversionContext,
    target: Target,
    args: Tuple[Argument, ...],
    kwargs: Dict[str, Argument],
    name: str,
) -> Union[TRTTensor, Sequence[TRTTensor]]:
    return np.random.rand(*args[0])


@dynamo_tensorrt_converter(
    torch.ops.aten.randn.default, capability_validator=rand_validator
)
def aten_ops_randn(
    ctx: ConversionContext,
    target: Target,
    args: Tuple[Argument, ...],
    kwargs: Dict[str, Argument],
    name: str,
) -> Union[TRTTensor, Sequence[TRTTensor]]:
    return np.random.randn(*args[0])


def randperm_validator(randperm_node: Node) -> bool:
    dtype = randperm_node.kwargs.get("dtype", None)
    layout = randperm_node.kwargs.get("layout", None)
    input = randperm_node.args[0]
    if not isinstance(input, int):
        _LOGGER.error("Input should be of type int.")
        return False
    if dtype is not None:
        _LOGGER.debug(
            f"Currently we don't support specifying output dtype, got {dtype}."
        )
        return False
    if layout is not None:
        _LOGGER.debug(f"Currently we don't support specifying layout, got {layout}.")
        return False
    return True


@dynamo_tensorrt_converter(
    torch.ops.aten.randperm.default, capability_validator=randperm_validator
)
def aten_ops_randperm(
    ctx: ConversionContext,
    target: Target,
    args: Tuple[Argument, ...],
    kwargs: Dict[str, Argument],
    name: str,
) -> Union[TRTTensor, Sequence[TRTTensor]]:
    return np.random.permutation(args[0])


def empty_validator(empty_node: Node) -> bool:
    device = empty_node.kwargs.get("device", None)
    if device is not None:
        _LOGGER.debug(f"Currently we don't support specifying device, got {device}.")
        return False
    layout = empty_node.kwargs.get("layout", None)
    if layout is not None:
        _LOGGER.debug(f"Currently we don't support specifying layout, got {layout}.")
        return False
    memory_format = empty_node.kwargs.get("memory_format", None)
    if memory_format is not None:
        _LOGGER.debug(
            f"Currently we don't support specifying memory_format, got {memory_format}."
        )
        return False
    return True


@dynamo_tensorrt_converter(
    torch.ops.aten.empty.memory_format, capability_validator=empty_validator
)
def aten_ops_empty(
    ctx: ConversionContext,
    target: Target,
    args: Tuple[Argument, ...],
    kwargs: Dict[str, Argument],
    name: str,
) -> Union[TRTTensor, Sequence[TRTTensor]]:
    empty_np_tensor = None
    if kwargs.get("dtype") is not None:
        empty_np_tensor = np.empty(
            tuple(args[0]),
            dtype=unified_dtype_converter(kwargs.get("dtype"), Frameworks.NUMPY),
        )
    else:
        # default returns np.float64. Verify the correctness of this
        empty_np_tensor = np.empty(tuple(args[0]))
    return empty_np_tensor
