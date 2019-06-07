from antlr4 import ParseTreeWalker

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from new.ExpressionListener import ExpressionListener


class StatementListener(CodeListener):
    def __init__(self, builder):
        self.builder = builder

    def enterReturnStatement(self, ctx: CodeParser.ReturnStatementContext):
        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder)
        walker.walk(listener, ctx)
        self.builder.ret(listener.stack.pop())
