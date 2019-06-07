from antlr4 import ParseTreeWalker

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from new.ExpressionListener import ExpressionListener
from new.FunctionContext import FunctionContext
from llvmlite import ir

from new.type_mapper import map_type


class StatementListener(CodeListener):
    def __init__(self, builder: ir.IRBuilder, context: FunctionContext):
        self.context = context
        self.builder = builder

    def enterReturnStatement(self, ctx: CodeParser.ReturnStatementContext):
        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.context)
        walker.walk(listener, ctx)
        self.builder.ret(listener.stack.pop())

    def enterAssignmentStatement(self, ctx: CodeParser.AssignmentStatementContext):
        t = map_type(ctx.type())
        name = ctx.ID().getText()
        pointer = self.builder.alloca(t, 1, name)
        self.context.add_variable(name, pointer)