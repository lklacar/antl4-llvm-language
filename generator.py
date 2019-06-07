from antlr4 import TerminalNode
from llvmlite import ir

from generated import CodeLexer
from generated.CodeParser import CodeParser


class CodeGenerator:
    def __init__(self, module_name):
        self.module = ir.Module(module_name)

    # noinspection PyShadowingBuiltins
    @staticmethod
    def get_type(type: CodeParser.TypeContext) -> ir.Type:
        t = type.children[0].symbol.text

        if t == 'int':
            return ir.IntType(32)
        elif t == 'double':
            return ir.DoubleType()

    def generate_function(self, context: CodeParser.FunctionContext) -> ir.Function:
        function = self.generate_function_definition(context.functionHead())

        block = function.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        for function_entry in context.functionBody().children:
            if isinstance(function_entry, CodeParser.StatementContext):
                self.generate_statement(builder, function_entry)
            elif isinstance(function_entry, CodeParser.ExpressionContext):
                self.generate_expression(builder, function_entry, True)

        return function

    def generate_function_definition(self, function_head: CodeParser.FunctionHeadContext) -> ir.Function:
        return_type = self.get_type(function_head.type())
        argument_types = [self.get_type(arg.type()) for arg in function_head.arguments().arg()]
        function_name = function_head.ID().symbol.text
        function_type = ir.FunctionType(return_type, tuple(argument_types))
        function = ir.Function(self.module, function_type, function_name)
        return function

    def generate_statement(self, builder: ir.IRBuilder, ctx: CodeParser.StatementContext):
        for child in ctx.children:
            if isinstance(child, CodeParser.ReturnStatementContext):
                self.generate_return_statement(builder, child)
            elif isinstance(child, CodeParser.AssignmentStatementContext):
                self.generate_assignment_statement(builder, child)

    def generate_expression(self, builder: ir.IRBuilder, ctx: CodeParser.ExpressionContext,
                            generate=False) -> [TerminalNode]:
        stack = []

        for child in sorted(ctx.children, key=lambda x: str(type(x)), reverse=True):
            if isinstance(child, CodeParser.ExpressionContext):
                stack += self.generate_expression(builder, child)

            elif isinstance(child, CodeParser.AtomContext):
                stack += child.children

            elif isinstance(child, TerminalNode):
                val = str(child)
                if val == "(" or val == ")":
                    continue

                stack.append(child)

        if not generate:
            return stack

        l = []
        for i in stack:
            i = self.map_terminal(i)
            if not isinstance(i, int):
                l.append(i)
            else:
                operation = i
                a = l.pop()
                b = l.pop()
                res = None
                if operation == CodeLexer.CodeLexer.PLUS:
                    res = builder.add(a, b)
                elif operation == CodeLexer.CodeLexer.MINUS:
                    res = builder.sub(a, b)
                elif operation == CodeLexer.CodeLexer.TIMES:
                    res = builder.mul(a, b)
                elif operation == CodeLexer.CodeLexer.DIV:
                    res = builder.udiv(a, b)

                l.append(res)

        print(l)


    def expression_postfix(self):


    def map_terminal(self, ctx):
        type = ctx.symbol.type
        value = ctx.symbol.text
        if type == CodeLexer.CodeLexer.INT:
            int_type = ir.IntType(32)
            return ir.Constant(int_type, int(value))

        return type

    def generate_return_statement(self, builder: ir.IRBuilder, ctx: CodeParser.ReturnStatementContext):
        expression_result = self.generate_expression(builder, ctx.expression(), True)
        builder.ret(expression_result)

    def generate_assignment_statement(self, builder: ir.IRBuilder, ctx: CodeParser.AssignmentStatementContext):
        pass
