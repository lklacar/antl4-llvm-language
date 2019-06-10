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


    # Enter a parse tree produced by CodeParser#moduleDefinition.
    def enterModuleDefinition(self, ctx:CodeParser.ModuleDefinitionContext):
        pass

    # Exit a parse tree produced by CodeParser#moduleDefinition.
    def exitModuleDefinition(self, ctx:CodeParser.ModuleDefinitionContext):
        pass


    # Enter a parse tree produced by CodeParser#statement.
    def enterStatement(self, ctx:CodeParser.StatementContext):
        pass

    # Exit a parse tree produced by CodeParser#statement.
    def exitStatement(self, ctx:CodeParser.StatementContext):
        pass


    # Enter a parse tree produced by CodeParser#ifStatement.
    def enterIfStatement(self, ctx:CodeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CodeParser#ifStatement.
    def exitIfStatement(self, ctx:CodeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CodeParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:CodeParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by CodeParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:CodeParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by CodeParser#returnStatement.
    def enterReturnStatement(self, ctx:CodeParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by CodeParser#returnStatement.
    def exitReturnStatement(self, ctx:CodeParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by CodeParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CodeParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CodeParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CodeParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CodeParser#functionBody.
    def enterFunctionBody(self, ctx:CodeParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by CodeParser#functionBody.
    def exitFunctionBody(self, ctx:CodeParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by CodeParser#parameters.
    def enterParameters(self, ctx:CodeParser.ParametersContext):
        pass

    # Exit a parse tree produced by CodeParser#parameters.
    def exitParameters(self, ctx:CodeParser.ParametersContext):
        pass


    # Enter a parse tree produced by CodeParser#arguments.
    def enterArguments(self, ctx:CodeParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by CodeParser#arguments.
    def exitArguments(self, ctx:CodeParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by CodeParser#functionCall.
    def enterFunctionCall(self, ctx:CodeParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CodeParser#functionCall.
    def exitFunctionCall(self, ctx:CodeParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CodeParser#expressionAdd.
    def enterExpressionAdd(self, ctx:CodeParser.ExpressionAddContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionAdd.
    def exitExpressionAdd(self, ctx:CodeParser.ExpressionAddContext):
        pass


    # Enter a parse tree produced by CodeParser#expressionEquation.
    def enterExpressionEquation(self, ctx:CodeParser.ExpressionEquationContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionEquation.
    def exitExpressionEquation(self, ctx:CodeParser.ExpressionEquationContext):
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


    # Enter a parse tree produced by CodeParser#expressionFunctionCall.
    def enterExpressionFunctionCall(self, ctx:CodeParser.ExpressionFunctionCallContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionFunctionCall.
    def exitExpressionFunctionCall(self, ctx:CodeParser.ExpressionFunctionCallContext):
        pass


    # Enter a parse tree produced by CodeParser#expressionNested.
    def enterExpressionNested(self, ctx:CodeParser.ExpressionNestedContext):
        pass

    # Exit a parse tree produced by CodeParser#expressionNested.
    def exitExpressionNested(self, ctx:CodeParser.ExpressionNestedContext):
        pass


    # Enter a parse tree produced by CodeParser#atom.
    def enterAtom(self, ctx:CodeParser.AtomContext):
        pass

    # Exit a parse tree produced by CodeParser#atom.
    def exitAtom(self, ctx:CodeParser.AtomContext):
        pass


    # Enter a parse tree produced by CodeParser#assignmentType.
    def enterAssignmentType(self, ctx:CodeParser.AssignmentTypeContext):
        pass

    # Exit a parse tree produced by CodeParser#assignmentType.
    def exitAssignmentType(self, ctx:CodeParser.AssignmentTypeContext):
        pass


    # Enter a parse tree produced by CodeParser#type.
    def enterType(self, ctx:CodeParser.TypeContext):
        pass

    # Exit a parse tree produced by CodeParser#type.
    def exitType(self, ctx:CodeParser.TypeContext):
        pass


