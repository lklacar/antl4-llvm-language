from antlr4 import TerminalNode

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ScientificListener(CodeListener):
    def enterScientific(self, ctx: CodeParser.ScientificContext):
        if len(ctx.children) == 1 and isinstance(ctx.children[0], TerminalNode):
            val = ctx.children[0]
            print(val)