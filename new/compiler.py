import sys
from antlr4 import *

from generated.CodeLexer import CodeLexer
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from llvmlite import ir


class ProgramListener(CodeListener):
    stack = []

    def __init__(self):
        self.module = ir.Module("expression")
        int_type = ir.IntType(32)
        function_type = ir.FunctionType(int_type, ())
        function = ir.Function(self.module, function_type, "evaluate")
        block = function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def exitExpressionAdd(self, ctx: CodeParser.ExpressionAddContext):
        left = self.stack.pop()
        right = self.stack.pop()

        if ctx.op.text == "+":
            self.stack.append(self.builder.add(left, right))
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
            res = ir.Constant(ir.DoubleType, float(val))
        else:
            raise Exception("Type not found")

        self.stack.append(res)


def main(argv):
    input_stream = FileStream("test/example.code")
    lexer = CodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CodeParser(stream)
    tree = parser.program()

    printer = ProgramListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print(printer.module)

if __name__ == '__main__':
    main(sys.argv)
