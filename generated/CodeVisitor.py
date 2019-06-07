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


    # Visit a parse tree produced by CodeParser#function.
    def visitFunction(self, ctx:CodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#functionHead.
    def visitFunctionHead(self, ctx:CodeParser.FunctionHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#arg.
    def visitArg(self, ctx:CodeParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#arguments.
    def visitArguments(self, ctx:CodeParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#functionBody.
    def visitFunctionBody(self, ctx:CodeParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#statement.
    def visitStatement(self, ctx:CodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#returnStatement.
    def visitReturnStatement(self, ctx:CodeParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:CodeParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#expression.
    def visitExpression(self, ctx:CodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#param.
    def visitParam(self, ctx:CodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#params.
    def visitParams(self, ctx:CodeParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#functionCall.
    def visitFunctionCall(self, ctx:CodeParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#atom.
    def visitAtom(self, ctx:CodeParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeParser#type.
    def visitType(self, ctx:CodeParser.TypeContext):
        return self.visitChildren(ctx)



del CodeParser