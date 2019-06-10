from compiler.walker import statement_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class FunctionBodyListener(CodeListener):

    def __init__(self, builder):
        self.builder = builder

    def enterStatement(self, ctx: CodeParser.StatementContext):
        statement_walker.walk(ctx, self.builder)
