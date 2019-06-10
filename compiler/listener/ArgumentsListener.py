from llvmlite import ir

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ArgumentsListener(CodeListener):
    def __init__(self, argument_names: [str], builder: ir.IRBuilder):
        self.argument_names = argument_names
        self.builder = builder

    def enterArguments(self, ctx: CodeParser.ArgumentsContext):
        for i, arg in enumerate(self.builder.function.args):
            self.builder.function.metadata[self.argument_names[i]] = arg
