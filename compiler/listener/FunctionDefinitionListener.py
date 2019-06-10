from compiler.types import get_llvm_type_by_context
from compiler.util import function_util
from compiler.walker import argument_types_walker, function_body_walker, arguments_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class FunctionDefinitionListener(CodeListener):
    def __init__(self, module):
        self.module = module
        self.builder = None

    def enterFunctionDefinition(self, ctx: CodeParser.FunctionDefinitionContext):
        argument_types_listener = argument_types_walker.walk(ctx.arguments())
        argument_types = argument_types_listener.argument_types
        argument_names = argument_types_listener.argument_names

        self.builder = function_util.create(self.module, ctx.ID().getText(),
                                            get_llvm_type_by_context(ctx.type()),
                                            argument_types)

        arguments_walker.walk(ctx.arguments(), argument_names, self.builder)

    def enterFunctionBody(self, ctx: CodeParser.FunctionBodyContext):
        function_body_walker.walk(ctx, self.builder)
