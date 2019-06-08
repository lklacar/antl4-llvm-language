from llvmlite import ir

from generated.CodeParser import CodeParser


def map_type(t: CodeParser.TypeContext):
    val = t.getText()

    if val == "int":
        return ir.IntType(32)
    elif val == "double":
        return ir.DoubleType()
    else:
        raise Exception("Can't map type to llvm")
