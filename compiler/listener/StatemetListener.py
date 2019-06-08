from antlr4 import ParseTreeWalker
from llvmlite import ir

from compiler.context.FunctionContext import FunctionContext
from compiler.listener.ExpressionListener import ExpressionListener
from compiler.util.type_mapper import map_type
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


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

        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.context)
        walker.walk(listener, ctx)
        value = listener.stack.pop()
        self.builder.store(value, pointer)

        self.context.add_variable(name, pointer)
