from llvmlite import ir

from compiler.types import get_llvm_type_by_name
from compiler.walker import function_definition_walker
from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ProgramListener(CodeListener):

    def __init__(self):
        self.module = None

    def enterProgram(self, ctx: CodeParser.ProgramContext):
        self.module = ir.Module(ctx.moduleDefinition().ID().getText())

        int_type = ir.IntType(32)
        printint_type = ir.FunctionType(int_type, (int_type,))
        printint = ir.Function(self.module, printint_type, name="printint")
        self.module.functions.append(printint)

        self.module.declare_intrinsic("printint", (get_llvm_type_by_name("i32"),))

    def enterFunctionDefinition(self, ctx: CodeParser.FunctionDefinitionContext):
        function_definition_walker.walk(self.module, ctx)

    def exitProgram(self, ctx: CodeParser.ProgramContext):
        print(self.module)
