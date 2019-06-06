# Generated from /home/luka/Projects/antl4-llvm-language/Code.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CodeParser import CodeParser
else:
    from CodeParser import CodeParser

# This class defines a complete listener for a parse tree produced by CodeParser.
class CodeListener(ParseTreeListener):

    # Enter a parse tree produced by CodeParser#file.
    def enterFile(self, ctx:CodeParser.FileContext):
        pass

    # Exit a parse tree produced by CodeParser#file.
    def exitFile(self, ctx:CodeParser.FileContext):
        pass


    # Enter a parse tree produced by CodeParser#expression.
    def enterExpression(self, ctx:CodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CodeParser#expression.
    def exitExpression(self, ctx:CodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CodeParser#atom.
    def enterAtom(self, ctx:CodeParser.AtomContext):
        pass

    # Exit a parse tree produced by CodeParser#atom.
    def exitAtom(self, ctx:CodeParser.AtomContext):
        pass


    # Enter a parse tree produced by CodeParser#scientific.
    def enterScientific(self, ctx:CodeParser.ScientificContext):
        pass

    # Exit a parse tree produced by CodeParser#scientific.
    def exitScientific(self, ctx:CodeParser.ScientificContext):
        pass


    # Enter a parse tree produced by CodeParser#variable.
    def enterVariable(self, ctx:CodeParser.VariableContext):
        pass

    # Exit a parse tree produced by CodeParser#variable.
    def exitVariable(self, ctx:CodeParser.VariableContext):
        pass


    # Enter a parse tree produced by CodeParser#relop.
    def enterRelop(self, ctx:CodeParser.RelopContext):
        pass

    # Exit a parse tree produced by CodeParser#relop.
    def exitRelop(self, ctx:CodeParser.RelopContext):
        pass


