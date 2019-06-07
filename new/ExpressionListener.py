from generated.CodeLexer import CodeLexer
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from llvmlite import ir


class ExpressionListener(CodeListener):
    stack = []

    def __init__(self, builder: ir.IRBuilder):
        self.builder = builder

    def exitExpressionAdd(self, ctx: CodeParser.ExpressionAddContext):
        left = self.stack.pop()
        right = self.stack.pop()

        if ctx.op.text == "+":
            self.stack.append(self.builder.fadd(left, right))
        elif ctx.op.text == "-":
            self.stack.append(self.builder.sub(left, right))

    def exitExpressionMul(self, ctx: CodeParser.ExpressionAddContext):
        left = self.stack.pop()
        right = self.stack.pop()

        if ctx.op.text == "*":
            self.stack.append(self.builder.mul(left, right))
        elif ctx.op.text == "/":
            self.stack.append(self.builder.udiv(left, right))

    def enterAtom(self, ctx: CodeParser.AtomContext):
        t = ctx.op.type
        val = ctx.getText()
        if t == CodeLexer.INT:
            res = ir.Constant(ir.IntType(32), int(val))
        elif t == CodeLexer.DECIMAL:
            res = ir.Constant(ir.DoubleType(), float(val))
        else:
            raise Exception("Cannot convert type {0} to machine LLVM".format(str(t)))

        self.stack.append(res)
