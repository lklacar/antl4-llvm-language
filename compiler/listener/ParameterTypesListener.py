from compiler.util import parameters_util
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ParameterTypesListener(CodeListener):
    def __init__(self):
        self.parameter_types = []
        self.parameter_names = []

    def enterParameters(self, ctx: CodeParser.ParametersContext):
        self.parameter_types.append(parameters_util.to_ir_types(ctx))
        self.parameter_names.append(ctx.ID().getText())
