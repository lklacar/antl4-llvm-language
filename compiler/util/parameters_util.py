from llvmlite import ir

from compiler.types import get_llvm_type_by_context
from generated.CodeParser import CodeParser


def to_ir_types(ctx: CodeParser.ParametersContext) -> ir.Type:
    return get_llvm_type_by_context(ctx.type())
