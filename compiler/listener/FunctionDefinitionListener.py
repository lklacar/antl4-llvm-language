from compiler.types import get_llvm_type_by_context
from compiler.util import function_util
from compiler.walker import parameter_types_walker, function_body_walker, parameters_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class FunctionDefinitionListener(CodeListener):
    def __init__(self, module):
        self.module = module
        self.builder = None

    def enterFunctionDefinition(self, ctx: CodeParser.FunctionDefinitionContext):
        parameter_types_listener = parameter_types_walker.walk(ctx.parameters())
        parameter_types = parameter_types_listener.parameter_types
        parameter_names = parameter_types_listener.parameter_names

        self.builder = function_util.create(self.module, ctx.ID().getText(),
                                            get_llvm_type_by_context(ctx.type()),
                                            parameter_types)

        parameters_walker.walk(ctx.parameters(), parameter_names, self.builder)

    def enterFunctionBody(self, ctx: CodeParser.FunctionBodyContext):
        function_body_walker.walk(ctx, self.builder)
