from generated.CodeListener import CodeListener
from generated.CodeParser import CodeParser
from listener.ScientificListener import ScientificListener


class AtomListener(CodeListener):
    def __init__(self):
        self.scientific_listener = ScientificListener()

    def enterAtom(self, ctx: CodeParser.AtomContext):
        for child in ctx.children:
            if isinstance(child, CodeParser.ScientificContext):
                self.scientific_listener.enterScientific(child)