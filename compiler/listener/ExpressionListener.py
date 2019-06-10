from llvmlite import ir

from compiler.walker import arguments_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ExpressionListener(CodeListener):
    def __init__(self, builder: ir.IRBuilder, t: ir.Type):
        self.builder = builder
        self.t = t
        self.stack = []

    def exitExpressionFunctionCall(self, ctx: CodeParser.ExpressionFunctionCallContext):
        function_name = ctx.functionCall().ID().getText()
        function = self.builder.module.get_global(function_name)

        arguments_listener = arguments_walker.walk(ctx.functionCall().arguments(), self.builder, function)
        arguments = arguments_listener.result

        self.builder.call(function, reversed(arguments), function_name)

    def exitExpressionAdd(self, ctx: CodeParser.ExpressionAddContext):
        left = self.stack.pop()
        right = self.stack.pop()

        if ctx.op.text == "+":
            self.stack.append(self.builder.add(right, left))
        elif ctx.op.text == "-":
            self.stack.append(self.builder.sub(right, left))

    def enterAtom(self, ctx: CodeParser.AtomContext):
        val = ctx.getText()
        t = self.t

        if val.isnumeric():
            res = t(val)
        else:
            res = self.builder.function.metadata[val]

        self.stack.append(res)
