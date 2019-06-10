// Generated from /home/luka/Projects/antl4-llvm-language/Code.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CodeParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CodeVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link CodeParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(CodeParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link CodeParser#moduleDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModuleDefinition(CodeParser.ModuleDefinitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CodeParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(CodeParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CodeParser#assignmentStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentStatement(CodeParser.AssignmentStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CodeParser#functionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionDefinition(CodeParser.FunctionDefinitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CodeParser#functionBody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionBody(CodeParser.FunctionBodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link CodeParser#arguments}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArguments(CodeParser.ArgumentsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code expressionAdd}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionAdd(CodeParser.ExpressionAddContext ctx);
	/**
	 * Visit a parse tree produced by the {@code expressionMul}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionMul(CodeParser.ExpressionMulContext ctx);
	/**
	 * Visit a parse tree produced by the {@code expressionNumber}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionNumber(CodeParser.ExpressionNumberContext ctx);
	/**
	 * Visit a parse tree produced by the {@code expressionNested}
	 * labeled alternative in {@link CodeParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionNested(CodeParser.ExpressionNestedContext ctx);
	/**
	 * Visit a parse tree produced by {@link CodeParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(CodeParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link CodeParser#assignmentType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentType(CodeParser.AssignmentTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link CodeParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(CodeParser.TypeContext ctx);
}