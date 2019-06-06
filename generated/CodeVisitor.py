# Generated from /home/luka/Projects/antl4-llvm-language/Code.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CodeParser import CodeParser
else:
    from CodeParser import CodeParser

# This class defines a complete generic visitor for a parse tree produced by CodeParser.

class CodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CodeParser#program.
    def visitProgram(self, ctx:CodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:CodeParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#functionBody.
    def visitFunctionBody(self, ctx:CodeParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#expr.
    def visitExpr(self, ctx:CodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#value.
    def visitValue(self, ctx:CodeParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#add.
    def visitAdd(self, ctx:CodeParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#mult.
    def visitMult(self, ctx:CodeParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#statement.
    def visitStatement(self, ctx:CodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#arguments.
    def visitArguments(self, ctx:CodeParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#argument.
    def visitArgument(self, ctx:CodeParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#params.
    def visitParams(self, ctx:CodeParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#param.
    def visitParam(self, ctx:CodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#functionCall.
    def visitFunctionCall(self, ctx:CodeParser.FunctionCallContext):
        return self.visitChildren(ctx)



del CodeParser