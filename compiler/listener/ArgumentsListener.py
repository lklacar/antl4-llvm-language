from compiler.util import arguments_util
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ArgumentsListener(CodeListener):
    def __init__(self):
        self.argument_types = []

    def enterArguments(self, ctx: CodeParser.ArgumentsContext):
        self.argument_types.append(arguments_util.to_ir_types(ctx))
