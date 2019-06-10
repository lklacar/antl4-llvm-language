from compiler.types import map_type
from generated.CodeParser import CodeParser
from llvmlite import ir


def to_ir_types(ctx: CodeParser.ArgumentsContext) -> ir.Type:
    return map_type(ctx.type())
