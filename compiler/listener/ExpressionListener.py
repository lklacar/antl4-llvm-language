from llvmlite import ir

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ExpressionListener(CodeListener):
    def __init__(self, builder: ir.IRBuilder, t: ir.Type):
        self.builder = builder
        self.t = t
        self.stack = []

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
