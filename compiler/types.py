from llvmlite import ir

from generated.CodeParser import CodeParser

m = {
    'i32': [ir.IntType(32), int],
    'i16': [ir.IntType(16), int],
    'i8': [ir.IntType(8), int],
    'double': [ir.DoubleType(), float]
}


def get_llvm_type_by_context(t: CodeParser.TypeContext) -> ir.Type:
    return m[t.getText()][0]


def get_llvm_type_by_name(name) -> ir.Type:
    return m[name][0]


def get_python_type_by_name(name):
    return m[name][1]


def get_python_type_by_llvm_type(llvm_type):
    for key in m:
        val = m[key]
        if val[0] == llvm_type:
            return val[1]

    raise Exception("Type not found")
