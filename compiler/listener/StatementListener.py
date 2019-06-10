from llvmlite import ir

from compiler.types import get_llvm_type_by_context
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

        self.builder.function.metadata[name] = expression_result
