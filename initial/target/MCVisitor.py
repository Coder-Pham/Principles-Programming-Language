# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declaration.
    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_type.
    def visitArray_type(self, ctx:MCParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#element_of_array.
    def visitElement_of_array(self, ctx:MCParser.Element_of_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#multi_var.
    def visitMulti_var(self, ctx:MCParser.Multi_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_declare.
    def visitVar_declare(self, ctx:MCParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#input_parameter.
    def visitInput_parameter(self, ctx:MCParser.Input_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#output_parameter.
    def visitOutput_parameter(self, ctx:MCParser.Output_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_point.
    def visitArray_point(self, ctx:MCParser.Array_pointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_declare.
    def visitPara_declare(self, ctx:MCParser.Para_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#multi_para.
    def visitMulti_para(self, ctx:MCParser.Multi_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression.
    def visitExpression(self, ctx:MCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assoc_expression.
    def visitAssoc_expression(self, ctx:MCParser.Assoc_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_SB.
    def visitExpression_SB(self, ctx:MCParser.Expression_SBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#relational_expression.
    def visitRelational_expression(self, ctx:MCParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#equality_expression.
    def visitEquality_expression(self, ctx:MCParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#index_expression.
    def visitIndex_expression(self, ctx:MCParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#invocation_expression.
    def visitInvocation_expression(self, ctx:MCParser.Invocation_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_expression.
    def visitList_expression(self, ctx:MCParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_call.
    def visitFunction_call(self, ctx:MCParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declare.
    def visitDeclare(self, ctx:MCParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_stmt.
    def visitExpression_stmt(self, ctx:MCParser.Expression_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_stmt.
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:MCParser.Dowhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_declare.
    def visitFunc_declare(self, ctx:MCParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        return self.visitChildren(ctx)



del MCParser