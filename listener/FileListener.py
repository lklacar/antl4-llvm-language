from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from listener.ExpressionListener import ExpressionListener


class FileListener(CodeListener):
    def __init__(self):
        self.expression_listener = ExpressionListener()

    def enterFile(self, ctx: CodeParser.FileContext):
        for child in ctx.children:
            self.expression_listener.enterExpression(child)
