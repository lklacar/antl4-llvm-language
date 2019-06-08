from antlr4 import ParseTreeWalker

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from llvmlite import ir

from compiler.context.FunctionContext import FunctionContext
from compiler.listener.StatemetListener import StatementListener


class FunctionBodyListener(CodeListener):
    def __init__(self, builder: ir.IRBuilder, context: FunctionContext):
        self.builder = builder
        self.context = context

    def enterFunctionBody(self, ctx: CodeParser.FunctionBodyContext):
        for child in ctx.children:
            listener = StatementListener(self.builder, self.context)
            walker = ParseTreeWalker()
            walker.walk(listener, child)
