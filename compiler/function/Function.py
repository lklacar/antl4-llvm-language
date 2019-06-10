from llvmlite import ir

from compiler.function.Context import Context


class Function(ir.Function):

    def __init__(self, module, ftype, name):
        super().__init__(module, ftype, name)
        self.context = Context()