// Generated from /home/luka/Projects/antl4-llvm-language/Code.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CodeParser}.
 */
public interface CodeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CodeParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(CodeParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(CodeParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeParser#moduleDefinition}.
	 * @param ctx the parse tree
	 */
	void enterModuleDefinition(CodeParser.ModuleDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#moduleDefinition}.
	 * @param ctx the parse tree
	 */
	void exitModuleDefinition(CodeParser.ModuleDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(CodeParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(CodeParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(CodeParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(CodeParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeParser#functionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDefinition(CodeParser.FunctionDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#functionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDefinition(CodeParser.FunctionDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeParser#functionBody}.
	 * @param ctx the parse tree
	 */
	void enterFunctionBody(CodeParser.FunctionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#functionBody}.
	 * @param ctx the parse tree
	 */
	void exitFunctionBody(CodeParser.FunctionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(CodeParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(CodeParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expressionAdd}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpressionAdd(CodeParser.ExpressionAddContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expressionAdd}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpressionAdd(CodeParser.ExpressionAddContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expressionMul}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpressionMul(CodeParser.ExpressionMulContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expressionMul}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpressionMul(CodeParser.ExpressionMulContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expressionNumber}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpressionNumber(CodeParser.ExpressionNumberContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expressionNumber}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpressionNumber(CodeParser.ExpressionNumberContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expressionNested}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpressionNested(CodeParser.ExpressionNestedContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expressionNested}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpressionNested(CodeParser.ExpressionNestedContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(CodeParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(CodeParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeParser#assignmentType}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentType(CodeParser.AssignmentTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#assignmentType}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentType(CodeParser.AssignmentTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(CodeParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(CodeParser.TypeContext ctx);
}