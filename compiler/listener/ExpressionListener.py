from llvmlite import ir

from generated.CodeLexer import CodeLexer
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ExpressionListener(CodeListener):
    def __init__(self, builder: ir.IRBuilder):
        self.builder = builder
        self.stack = []

    def exitExpressionAdd(self, ctx: CodeParser.ExpressionAddContext):
        left = self.stack.pop()
        right = self.stack.pop()

        if ctx.op.text == "+":
            self.stack.append(self.builder.add(right, left))
        elif ctx.op.text == "-":
            self.stack.append(self.builder.sub(right, left))

    def enterAtom(self, ctx: CodeParser.AtomContext):
        t = ctx.op.type
        val = ctx.getText()
        if t == CodeLexer.Constant:
            res = ir.Constant(ir.IntType(32), int(val))
        elif t == CodeLexer.DECIMAL:
            res = ir.Constant(ir.DoubleType(), float(val))
        elif t == CodeParser.ID:
            pointer = self.context.get_variable(val)

            # Can be either argument or local variable
            if isinstance(pointer, Argument):
                res = pointer
            else:
                res = self.builder.load(pointer, val)
        else:
            raise Exception("Cannot convert type {0} to machine LLVM".format(str(t)))

        self.stack.append(res)
