from antlr4 import TerminalNode

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from listener.AtomListener import AtomListener


class ExpressionListener(CodeListener):
    def __init__(self):
        self.atom_listener = AtomListener()

    def enterExpression(self, ctx: CodeParser.ExpressionContext):
        if isinstance(ctx, TerminalNode):
            return

        elif len(ctx.children) == 1:
            for child in ctx.children:
                if isinstance(child, CodeParser.AtomContext):
                    self.atom_listener.enterAtom(child)

        elif len(ctx.children) == 3:
            if isinstance(ctx.children[1], CodeParser.ExpressionContext):
                expression = ctx.children[1]
                self.enterExpression(expression)
            else:
                left = ctx.children[0]
                terminmal = ctx.children[1]
                right = ctx.children[2]

                self.enterExpression(left)
                self.enterExpression(right)
                print(terminmal)
