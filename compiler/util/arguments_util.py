from compiler.types import get_llvm_type_by_context
from generated.CodeParser import CodeParser
from llvmlite import ir


def to_ir_types(ctx: CodeParser.ArgumentsContext) -> ir.Type:
    return get_llvm_type_by_context(ctx.type())
