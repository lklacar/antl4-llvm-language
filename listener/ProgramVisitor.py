from generated.CodeParser import CodeParser
from generated.CodeVisitor import CodeVisitor
from generator import CodeGenerator


class ProgramVisitor(CodeVisitor):
    def __init__(self):
        self.generator = CodeGenerator("program")

    def visitProgram(self, ctx: CodeParser.ProgramContext):
        for function in ctx.function():
            self.generator.generate_function(function)