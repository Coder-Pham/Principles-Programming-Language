// Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2

    package mc.parser;

import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MCParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MCVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MCParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MCParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#array_point_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArray_point_type(MCParser.Array_point_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#element_of_array}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElement_of_array(MCParser.Element_of_arrayContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#input_parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInput_parameter(MCParser.Input_parameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#output_parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOutput_parameter(MCParser.Output_parameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#array_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArray_type(MCParser.Array_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaration(MCParser.DeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#variable_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable_decl(MCParser.Variable_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#many_variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMany_variable(MCParser.Many_variableContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable(MCParser.VariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#function_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_decl(MCParser.Function_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#parameter_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter_list(MCParser.Parameter_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#parameter_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter_decl(MCParser.Parameter_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#typeMC}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeMC(MCParser.TypeMCContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(MCParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#declaration_part}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaration_part(MCParser.Declaration_partContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#statement_part}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement_part(MCParser.Statement_partContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#if_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf_stmt(MCParser.If_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#block_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock_stmt(MCParser.Block_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#dowhile_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDowhile_stmt(MCParser.Dowhile_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#for_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFor_stmt(MCParser.For_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#break_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreak_stmt(MCParser.Break_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#continue_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinue_stmt(MCParser.Continue_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#return_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturn_stmt(MCParser.Return_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#expression_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression_stmt(MCParser.Expression_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(MCParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#assoc_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssoc_expression(MCParser.Assoc_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#expression_SB}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression_SB(MCParser.Expression_SBContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#relational_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelational_expression(MCParser.Relational_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#equality_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEquality_expression(MCParser.Equality_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#index_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndex_expression(MCParser.Index_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#invocation_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInvocation_expression(MCParser.Invocation_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#list_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitList_expression(MCParser.List_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#operands}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperands(MCParser.OperandsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#literals}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLiterals(MCParser.LiteralsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#function_call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_call(MCParser.Function_callContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#primitive_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitive_type(MCParser.Primitive_typeContext ctx);
}