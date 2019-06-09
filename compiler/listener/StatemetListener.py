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

        self.condition = None

    def enterReturnStatement(self, ctx: CodeParser.ReturnStatementContext):
        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.context)
        walker.walk(listener, ctx)

        if self.condition is not None:
            with self.builder.if_then(self.condition):
                self.builder.ret(listener.stack.pop())
        else:
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

    def enterIfStatement(self, ctx:CodeParser.IfStatementContext):
        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.context)
        walker.walk(listener, ctx.equation().expression(0))
        left = listener.stack.pop()

        walker = ParseTreeWalker()
        listener = ExpressionListener(self.builder, self.context)
        walker.walk(listener, ctx.equation().expression(1))
        right = listener.stack.pop()

        operation = ctx.equation().op.getText()
        self.condition = self.builder.icmp_signed(cmpop=operation, lhs=left, rhs=right)

    def exitIfStatement(self, ctx: CodeParser.IfStatementContext):
        self.context = None
