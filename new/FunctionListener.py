from antlr4 import ParseTreeWalker

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from llvmlite import ir

from new.FunctionBodyListener import FunctionBodyListener
from new.FunctionContext import FunctionContext
from new.type_mapper import map_type


class FunctionListener(CodeListener):

    def __init__(self, module):
        self.module = module
        self.function = None
        self.context = FunctionContext()

    def enterFunctionHead(self, ctx: CodeParser.FunctionHeadContext):
        return_type = map_type(ctx.type())
        argument_types = [map_type(arg.type()) for arg in ctx.arguments().arg()]
        function_name = ctx.ID().symbol.text
        function_type = ir.FunctionType(return_type, tuple(argument_types))
        self.function = ir.Function(self.module, function_type, function_name)

    def enterFunctionBody(self, ctx: CodeParser.FunctionBodyContext):
        listener = FunctionBodyListener(self.function, self.context)

        walker = ParseTreeWalker()
        walker.walk(listener, ctx)
