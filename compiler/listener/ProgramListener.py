from antlr4 import ParseTreeWalker
from llvmlite import ir

from compiler.context.ProgramContext import ProgramContext
from compiler.listener.FunctionListener import FunctionListener
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ProgramListener(CodeListener):
    stack = []

    def __init__(self):
        self.module = ir.Module("expression")
        self.context = ProgramContext()

    def enterFunction(self, ctx: CodeParser.FunctionContext):
        listener = FunctionListener(self.module, self.context)

        walker = ParseTreeWalker()
        walker.walk(listener, ctx)
