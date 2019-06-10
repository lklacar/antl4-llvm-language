from generated.CodeParser import CodeParser
from llvmlite import ir


class CodeGenerator:

    def __init__(self, tree):
        self.tree = tree

    def expression(self, ctx: CodeParser.ExpressionContext):
        module = ir.Module("expression")
