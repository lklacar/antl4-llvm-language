from compiler.util import arguments_util
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ArgumentTypesListener(CodeListener):
    def __init__(self):
        self.argument_types = []
        self.argument_names = []

    def enterArguments(self, ctx: CodeParser.ArgumentsContext):
        self.argument_types.append(arguments_util.to_ir_types(ctx))
        self.argument_names.append(ctx.ID().getText())
