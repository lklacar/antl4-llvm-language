from compiler.walker import expression_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class StatementListener(CodeListener):

    def __init__(self, builder):
        self.builder = builder

    def enterAssignmentStatement(self, ctx: CodeParser.AssignmentStatementContext):
        expression_result = expression_walker.walk(ctx.expression(), self.builder).stack.pop()
        pass