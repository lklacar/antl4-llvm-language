from llvmlite import ir

from compiler.walker import expression_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ArgumentsListener(CodeListener):
    def __init__(self, builder: ir.IRBuilder, callee_function: ir.Function):
        self.arguments = []
        self.builder = builder
        self.callee_function = callee_function
        self.callee_arguments = list(reversed(self.callee_function.args))
        self.result = []

    def enterArguments(self, ctx: CodeParser.ArgumentsContext):
        expression = ctx.expression()

        expression_result = expression_walker.walk(expression, self.builder,
                                                   self.callee_arguments[len(self.result)].type)

        self.result.append(expression_result.stack.pop())