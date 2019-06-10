from types import m

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser


class ExpressionTypeListener(CodeListener):
    def __init__(self, builder):
        self.types = []
        self.builder = builder

    def enterAtom(self, ctx: CodeParser.AtomContext):
        val = ctx.getText()

        if '.' in val:
            self.types.append(m['double'])
