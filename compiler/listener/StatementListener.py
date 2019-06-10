from llvmlite import ir

from compiler.types import get_llvm_type_by_context, get_llvm_type_by_name
from compiler.walker import expression_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class StatementListener(CodeListener):

    def __init__(self, builder: ir.IRBuilder):
        self.builder = builder

    def enterAssignmentStatement(self, ctx: CodeParser.AssignmentStatementContext):
        t = get_llvm_type_by_context(ctx.type())
        name = ctx.ID().getText()
        expression_result = expression_walker.walk(ctx.expression(), self.builder, t).stack.pop()

        pointer = self.builder.alloca(t, 1, name=name)
        self.builder.store(expression_result, pointer)

        self.builder.function.context.add_variable(name, expression_result)

    def enterReturnStatement(self, ctx: CodeParser.ReturnStatementContext):
        return_type = self.builder.function.return_value.type
        expression_result = expression_walker.walk(ctx.expression(), self.builder, return_type).stack.pop()
        self.builder.ret(expression_result)

    def enterIfStatement(self, ctx: CodeParser):
        expression = ctx.expression()
        expression_result = expression_walker.walk(ctx.expression(), self.builder, ir.DoubleType()).stack.pop()
