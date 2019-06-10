from llvmlite import ir

from compiler.walker import function_definition_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ProgramListener(CodeListener):

    def __init__(self):
        self.module = None

    def enterProgram(self, ctx: CodeParser.ProgramContext):
        self.module = ir.Module(ctx.moduleDefinition().ID().getText())

    def enterFunctionDefinition(self, ctx: CodeParser.FunctionDefinitionContext):
        function_definition_walker.walk(self.module, ctx)

    def exitProgram(self, ctx: CodeParser.ProgramContext):
        print(self.module)
