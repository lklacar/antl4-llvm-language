from llvmlite import ir

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ParametersListener(CodeListener):
    def __init__(self, parameter_names: [str], builder: ir.IRBuilder):
        self.parameter_names = parameter_names
        self.builder = builder

    def enterParameters(self, ctx: CodeParser.ParametersContext):
        for i, arg in enumerate(self.builder.function.args):
            self.builder.function.metadata[self.parameter_names[i]] = arg
