# Generated from /home/luka/Projects/antl4-llvm-language/Code.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CodeParser import CodeParser
else:
    from CodeParser import CodeParser

# This class defines a complete listener for a parse tree produced by CodeParser.
class CodeListener(ParseTreeListener):

    # Enter a parse tree produced by CodeParser#program.
    def enterProgram(self, ctx:CodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by CodeParser#program.
    def exitProgram(self, ctx:CodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by CodeParser#function.
    def enterFunction(self, ctx:CodeParser.FunctionContext):
        pass

    # Exit a parse tree produced by CodeParser#function.
    def exitFunction(self, ctx:CodeParser.FunctionContext):
        pass


    # Enter a parse tree produced by CodeParser#functionHead.
    def enterFunctionHead(self, ctx:CodeParser.FunctionHeadContext):
        pass

    # Exit a parse tree produced by CodeParser#functionHead.
    def exitFunctionHead(self, ctx:CodeParser.FunctionHeadContext):
        pass


    # Enter a parse tree produced by CodeParser#arg.
    def enterArg(self, ctx:CodeParser.ArgContext):
        pass

    # Exit a parse tree produced by CodeParser#arg.
    def exitArg(self, ctx:CodeParser.ArgContext):
        pass


    # Enter a parse tree produced by CodeParser#arguments.
    def enterArguments(self, ctx:CodeParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by CodeParser#arguments.
    def exitArguments(self, ctx:CodeParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by CodeParser#functionBody.
    def enterFunctionBody(self, ctx:CodeParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by CodeParser#functionBody.
    def exitFunctionBody(self, ctx:CodeParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by CodeParser#statement.
    def enterStatement(self, ctx:CodeParser.StatementContext):
        pass

    # Exit a parse tree produced by CodeParser#statement.
    def exitStatement(self, ctx:CodeParser.StatementContext):
        pass


    # Enter a parse tree produced by CodeParser#returnStatement.
    def enterReturnStatement(self, ctx:CodeParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by CodeParser#returnStatement.
    def exitReturnStatement(self, ctx:CodeParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by CodeParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:CodeParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by CodeParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:CodeParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by CodeParser#expressionAdd.
    def enterExpressionAdd(self, ctx:CodeParser.ExpressionAddContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionAdd.
    def exitExpressionAdd(self, ctx:CodeParser.ExpressionAddContext):
        pass


    # Enter a parse tree produced by CodeParser#expressionMul.
    def enterExpressionMul(self, ctx:CodeParser.ExpressionMulContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionMul.
    def exitExpressionMul(self, ctx:CodeParser.ExpressionMulContext):
        pass


    # Enter a parse tree produced by CodeParser#expressionNumber.
    def enterExpressionNumber(self, ctx:CodeParser.ExpressionNumberContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionNumber.
    def exitExpressionNumber(self, ctx:CodeParser.ExpressionNumberContext):
        pass


    # Enter a parse tree produced by CodeParser#expressionNested.
    def enterExpressionNested(self, ctx:CodeParser.ExpressionNestedContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionNested.
    def exitExpressionNested(self, ctx:CodeParser.ExpressionNestedContext):
        pass


    # Enter a parse tree produced by CodeParser#expressionFunctionCall.
    def enterExpressionFunctionCall(self, ctx:CodeParser.ExpressionFunctionCallContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionFunctionCall.
    def exitExpressionFunctionCall(self, ctx:CodeParser.ExpressionFunctionCallContext):
        pass


    # Enter a parse tree produced by CodeParser#expressionPow.
    def enterExpressionPow(self, ctx:CodeParser.ExpressionPowContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionPow.
    def exitExpressionPow(self, ctx:CodeParser.ExpressionPowContext):
        pass


    # Enter a parse tree produced by CodeParser#param.
    def enterParam(self, ctx:CodeParser.ParamContext):
        pass

    # Exit a parse tree produced by CodeParser#param.
    def exitParam(self, ctx:CodeParser.ParamContext):
        pass


    # Enter a parse tree produced by CodeParser#params.
    def enterParams(self, ctx:CodeParser.ParamsContext):
        pass

    # Exit a parse tree produced by CodeParser#params.
    def exitParams(self, ctx:CodeParser.ParamsContext):
        pass


    # Enter a parse tree produced by CodeParser#functionCall.
    def enterFunctionCall(self, ctx:CodeParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CodeParser#functionCall.
    def exitFunctionCall(self, ctx:CodeParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CodeParser#atom.
    def enterAtom(self, ctx:CodeParser.AtomContext):
        pass

    # Exit a parse tree produced by CodeParser#atom.
    def exitAtom(self, ctx:CodeParser.AtomContext):
        pass


    # Enter a parse tree produced by CodeParser#type.
    def enterType(self, ctx:CodeParser.TypeContext):
        pass

    # Exit a parse tree produced by CodeParser#type.
    def exitType(self, ctx:CodeParser.TypeContext):
        pass


