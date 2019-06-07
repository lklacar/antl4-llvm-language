from generated.CodeLexer import CodeLexer
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from llvmlite import ir


class ExpressionListener(CodeListener):
    stack = []

    def __init__(self, builder: ir.IRBuilder, context):
        self.context = context
        self.builder = builder

    def exitExpressionAdd(self, ctx: CodeParser.ExpressionAddContext):
        left = self.stack.pop()
        right = self.stack.pop()

        if isinstance(left.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
            add_function = self.builder.fadd
            sub_function = self.builder.fsub

            double_type = ir.DoubleType()
            left = self.builder.inttoptr(left, double_type)
            right = self.builder.inttoptr(right, double_type)

        elif isinstance(left.type, ir.IntType) and isinstance(right.type, ir.IntType):
            add_function = self.builder.add
            sub_function = self.builder.sub
        else:
            raise Exception("Cannot convert {} and {} to the same type".format(left, right))

        if ctx.op.text == "+":
            self.stack.append(add_function(left, right))
        elif ctx.op.text == "-":
            self.stack.append(sub_function(left, right))

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
        elif t == CodeParser.ID:
            pointer = self.context.get_variable(val)
            res = self.builder.load(pointer, val)
        else:
            raise Exception("Cannot convert type {0} to machine LLVM".format(str(t)))

        self.stack.append(res)
