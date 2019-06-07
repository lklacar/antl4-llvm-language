from antlr4 import ParseTreeWalker

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from llvmlite import ir

from new.ExpressionListener import ExpressionListener
from new.StatemetListener import StatementListener


class FunctionBodyListener(CodeListener):
    def __init__(self, function):
        self.function = function
        block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def enterFunctionBody(self, ctx: CodeParser.FunctionBodyContext):
        for child in ctx.children:
            if isinstance(child, CodeParser.ExpressionContext):
                listener = ExpressionListener(self.builder)
                walker = ParseTreeWalker()
                walker.walk(listener, child)
            elif isinstance(child, CodeParser.StatementContext):
                listener = StatementListener(self.builder)
                walker = ParseTreeWalker()
                walker.walk(listener, child)