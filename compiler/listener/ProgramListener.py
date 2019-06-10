from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ProgramListener(CodeListener):

    def enterProgram(self, ctx: CodeParser.ProgramContext):
        super().enterProgram(ctx)