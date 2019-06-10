from compiler import util
from compiler.types import map_type
from compiler.util import function_util
from compiler.walker import arguments_walker, function_body_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class FunctionDefinitionListener(CodeListener):
    def __init__(self, module):
        self.module = module
        self.builder = None

    def enterFunctionDefinition(self, ctx: CodeParser.FunctionDefinitionContext):
        argument_types = arguments_walker.walk(ctx.arguments()).argument_types

        self.builder = function_util.create(self.module, ctx.ID().getText(),
                                            map_type(ctx.type()),
                                            argument_types)

    def enterFunctionBody(self, ctx: CodeParser.FunctionBodyContext):
        function_body_walker.walk(ctx, self.builder)
