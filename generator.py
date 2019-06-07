from antlr4 import TerminalNode
from llvmlite import ir

from generated import CodeLexer
from generated.CodeParser import CodeParser


class CodeGenerator:
    def __init__(self, module_name):
        self.module = ir.Module(module_name)

        self.function_context = {

        }

    # noinspection PyShadowingBuiltins
    @staticmethod
    def get_type(type: CodeParser.TypeContext) -> ir.Type:
        t = type.children[0].symbol.text

        if t == 'int':
            return ir.IntType(32)
        elif t == 'double':
            return ir.DoubleType()

    def generate_program(self, ctx: CodeParser.ProgramContext):
        for function in ctx.function():
            self.function_context[function.functionHead().ID().symbol.text] = {
                "variables": {}
            }

            self.generate_function(function)

        return self.module

    def generate_function(self, context: CodeParser.FunctionContext) -> ir.Function:
        function = self.generate_function_definition(context.functionHead())

        block = function.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        for function_entry in context.functionBody().children:
            if isinstance(function_entry, CodeParser.StatementContext):
                self.generate_statement(builder, function_entry)
            elif isinstance(function_entry, CodeParser.ExpressionContext):
                self.generate_expression(builder, function_entry)

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

    def expression_postfix(self, ctx: CodeParser.ExpressionContext) -> [TerminalNode]:
        stack = []

        for child in sorted(ctx.children, key=lambda x: str(type(x)), reverse=True):
            if isinstance(child, CodeParser.FunctionCallContext):
                stack.append(child)

            elif isinstance(child, CodeParser.ExpressionContext):
                stack += self.expression_postfix(child)

            elif isinstance(child, CodeParser.AtomContext):
                stack += child.children

            elif isinstance(child, TerminalNode):
                val = str(child)
                if val == "(" or val == ")":
                    continue

                stack.append(child)

        return stack

    def generate_expression(self, builder, ctx: CodeParser.ExpressionContext):
        stack = self.expression_postfix(ctx)
        l = []
        for i in stack:

            if isinstance(i, CodeParser.FunctionCallContext):
                l.append(self.generate_function_call(builder, i))
                continue

            value = self.map_terminal(builder, i)

            if not isinstance(value, int):
                l.append(value)
            else:
                operation = value
                a = l.pop()
                b = l.pop()
                res = None
                if operation == CodeParser.PLUS:
                    res = builder.add(a, b)
                elif operation == CodeParser.MINUS:
                    res = builder.sub(a, b)
                elif operation == CodeParser.TIMES:
                    res = builder.mul(a, b)
                elif operation == CodeParser.DIV:
                    res = builder.udiv(a, b)

                l.append(res)

        return l[0]

    def map_terminal(self, builder, ctx):
        type = ctx.symbol.type
        value = ctx.symbol.text
        function_name = builder.function._name

        if type == CodeLexer.CodeLexer.INT:
            int_type = ir.IntType(32)
            return ir.Constant(int_type, int(value))

        if type == CodeLexer.CodeLexer.ID:
            pointer = self.function_context[function_name]['variables'][value]
            return builder.load(pointer, value)

        return type

    def generate_return_statement(self, builder: ir.IRBuilder, ctx: CodeParser.ReturnStatementContext):
        expression_result = self.generate_expression(builder, ctx.expression())
        builder.ret(expression_result)

    def generate_assignment_statement(self, builder: ir.IRBuilder, ctx: CodeParser.AssignmentStatementContext):
        type = self.get_type(ctx.type())
        name = ctx.ID().symbol.text

        function_name = builder.function._name

        val = self.generate_expression(builder, ctx.expression())
        pointer = builder.alloca(type, 1, name)

        builder.store(val, pointer)
        self.function_context[function_name]['variables'][name] = pointer

    def generate_function_call(self, builder : ir.IRBuilder, ctx: CodeParser.FunctionCallContext):
        value = [self.generate_expression(x.expression()) for x in ctx.params().param()]
        print("A");

