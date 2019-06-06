from antlr4 import TerminalNode

from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from listener.AtomListener import AtomListener



class ExpressionListener(CodeListener):
    def __init__(self):
        self.atom_listener = AtomListener()

        self.values = []

    def enterExpression(self, ctx: CodeParser.ExpressionContext):
        # The expression is value itself
        if len(ctx.children) == 1:
            for child in ctx.children:
                if isinstance(child, CodeParser.AtomContext):
                    val = self.atom_listener.enterAtom(child)
                    self.values.append(int(val.symbol.text))

        # The expression needs further evaluation
        elif len(ctx.children) == 3:
            # The expression is between parentheses, where [0] and [2] are terminal characters, but parentheses
            if isinstance(ctx.children[1], CodeParser.ExpressionContext):
                expression = ctx.children[1]
                self.enterExpression(expression)

            # The expression contains a terminal character (an operation) between two expression
            else:
                left = ctx.children[0]
                terminmal = ctx.children[1]
                right = ctx.children[2]

                self.enterExpression(left)
                self.enterExpression(right)

                self.values.append(terminmal.symbol.text)
