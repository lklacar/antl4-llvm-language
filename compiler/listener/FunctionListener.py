from antlr4 import ParseTreeWalker

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from llvmlite import ir

from compiler.listener.FunctionBodyListener import FunctionBodyListener
from compiler.context.FunctionContext import FunctionContext
from compiler.util.type_mapper import map_type


class FunctionListener(CodeListener):

    def __init__(self, module, program_context):
        self.module = module
        self.program_context = program_context
        self.function = None
        self.context = None
        self.builder = None

    def enterFunctionHead(self, ctx: CodeParser.FunctionHeadContext):
        return_type = map_type(ctx.type())
        argument_types = [map_type(arg.type()) for arg in ctx.arguments().arg()]
        function_name = ctx.ID().symbol.text
        function_type = ir.FunctionType(return_type, tuple(argument_types))

        self.init_function(function_name, function_type)

        args = [a.ID().getText() for a in ctx.arguments().arg()]
        for i, arg in enumerate(self.function.args):
            self.context.add_variable(args[i], arg)

    def init_function(self, function_name, function_type):
        self.function = ir.Function(self.module, function_type, function_name)
        block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.context = FunctionContext(function_name, self.program_context, self.function)

    def enterFunctionBody(self, ctx: CodeParser.FunctionBodyContext):
        listener = FunctionBodyListener(self.builder, self.context)

        walker = ParseTreeWalker()
        walker.walk(listener, ctx)
