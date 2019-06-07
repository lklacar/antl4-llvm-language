from antlr4 import ParseTreeWalker

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from llvmlite import ir

from new.FunctionContext import FunctionContext
from new.StatemetListener import StatementListener


class FunctionBodyListener(CodeListener):
    def __init__(self, function: ir.Function, context: FunctionContext):
        self.function = function
        self.context = context
        block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def enterFunctionBody(self, ctx: CodeParser.FunctionBodyContext):
        for child in ctx.children:
            listener = StatementListener(self.builder, self.context)
            walker = ParseTreeWalker()
            walker.walk(listener, child)
