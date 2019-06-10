from llvmlite import ir

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

        args = []
        for _ in function.args:
            args.append(self.stack.pop())

        call = self.builder.call(function, args, function_name)
        self.stack.append(call)

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
            res = self.builder.function.context.get_variable(val)

        self.stack.append(res)
