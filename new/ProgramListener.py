from antlr4 import ParseTreeWalker
from llvmlite import ir

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from new.FunctionListener import FunctionListener


class ProgramListener(CodeListener):
    stack = []

    def __init__(self):
        self.module = ir.Module("expression")

    def enterFunction(self, ctx: CodeParser.FunctionContext):
        listener = FunctionListener(self.module)

        walker = ParseTreeWalker()
        walker.walk(listener, ctx)
