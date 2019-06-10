from llvmlite import ir

from generated.CodeParser import CodeParser

m = {
    'i32': ir.IntType(32),
    'i16': ir.IntType(16),
    'i8': ir.IntType(8),
    'double': ir.DoubleType()
}


def map_type(t: CodeParser.TypeContext) -> ir.Type:
    return m[t.getText()]
