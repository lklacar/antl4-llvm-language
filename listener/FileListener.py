from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from listener.ExpressionListener import ExpressionListener
from llvmlite import ir


class FileListener(CodeListener):
    def __init__(self):
        self.expression_listener = ExpressionListener()

    def enterFile(self, ctx: CodeParser.FileContext):
        for child in ctx.children:
            res = self.expression_listener.enterExpression(child)

    def get_llvm_module(self):
        values = self.expression_listener.values

        int_type = ir.IntType(32)
        function_type = ir.FunctionType(int_type, ())
        module = ir.Module("expression")
        function = ir.Function(module, function_type, "evaluate")
        block = function.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        converted = []

        for val in values:
            if isinstance(val, int):
                converted.append(ir.Constant(int_type, val))
            else:
                converted.append(val)

        l = []

        for i in converted:
            if not isinstance(i, str):
                l.append(i)
            else:
                operation = i
                a = l.pop()
                b = l.pop()
                res = None
                if operation == "+":
                    res = builder.add(a, b)
                elif operation == "-":
                    res = builder.sub(a, b)
                elif operation == "*":
                    res = builder.mul(a, b)
                elif operation == "/":
                    res = builder.udiv(a, b)

                l.append(res)

        builder.ret(l.pop())

        return module
