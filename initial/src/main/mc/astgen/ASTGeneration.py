from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *


class ASTGeneration(MCVisitor):
    def visitProgram(self, ctx: MCParser.ProgramContext):
        # return Program([FuncDecl(Id("main"),[],self.visit(ctx.mctype()),Block([self.visit(ctx.body())] if ctx.body() else []))])
        declList = []
        for decl in ctx.declaration():
            declare = self.visitDeclaration(decl)
            if isinstance(declare, list):
                declList.extend(declare)
            else:
                declList.append(declare)
        return Program(declList)

    def visitDeclaration(self, ctx: MCParser.DeclarationContext):
        return self.visitChildren(ctx)

    def visitFunc_declare(self, ctx: MCParser.Func_declareContext):
        name = Id(ctx.ID().getText())
        param = self.visitMulti_para(ctx.multi_para()) if ctx.multi_para() else []
        # returnType = Type(ctx.getChild(0).accept(self))
        returnType = self.visit(ctx.getChild(0))
        body = self.visit(ctx.block_stmt())
        return FuncDecl(name, param, returnType, body)

    def visitVar_declare(self, ctx: MCParser.Var_declareContext):
        # varType = ctx.primitive_type().accept(self)
        varType = self.visitPrimitive_type(ctx.primitive_type())
        varList = self.visit(ctx.multi_var())
        varDeclList = []
        for x in varList:
            if x[1] == "-1":
                varDeclList.append(VarDecl(Id(x[0]), varType))
            else:
                varDeclList.append(VarDecl(Id(x[0]), ArrayType(
                    IntLiteral(int(x[1])), varType)))
        return varDeclList

    def visitMulti_var(self, ctx: MCParser.Multi_varContext):
        varList = []
        for item in ctx.variable():
            var = self.visit(item)
            # if isinstance(var, list):
            #     varList.extend(var)
            # else:
            varList.append(var)
        return varList
        # return list(map(lambda x: x.accept(self), ctx.variable()))

    def visitVariable(self, ctx: MCParser.VariableContext):
        # Array
        if ctx.getChildCount() == 4:
            return [ctx.ID().getText(), ctx.IntLIT().getText()]
        # Variable
        else:
            return [ctx.ID().getText(), "-1"]

    # array_point -> input_para | output_para
    def visitArray_point(self, ctx: MCParser.Array_pointContext):
        return self.visitChild(ctx)

    def visitInput_parameter(self, ctx: MCParser.Input_parameterContext):
        # return ArrayPointerType(ctx.getChild(0).accept(self))
        return ArrayPointerType(self.visit(ctx.primitive_type()))

    def visitOutput_parameter(self, ctx: MCParser.Output_parameterContext):
        # return ArrayPointerType(ctx.getChild(0).accept(self))
        return ArrayPointerType(self.visit(ctx.primitive_type()))

    def visitArray_type(self, ctx: MCParser.Array_typeContext):
        return ArrayType(IntLiteral(int(ctx.IntLIT().getText())), self.visit(ctx.primitive_type()))

    def visitElement_of_array(self, ctx: MCParser.Element_of_arrayContext):
        arr = Id(ctx.ID(0).getText())
        if ctx.IntLIT():
            idx = IntLiteral(int(ctx.getChild(2).getText()))
        else:
            idx = Id(ctx.ID(1).getText())
        return ArrayCell(arr, idx)

    def visitPara_declare(self, ctx: MCParser.Para_declareContext):
        # paraType = Type(ctx.primitive_type().accept(self))
        paraType = self.visit(ctx.primitive_type())
        paraName = Id(ctx.ID().getText())
        if ctx.getChildCount() == 4:
            return VarDecl(paraName, ArrayPointerType(paraType))
        else:
            return VarDecl(paraName, paraType)

    # NOTE: Check dimension of list
    def visitMulti_para(self, ctx: MCParser.Multi_paraContext):
        paraList = []
        for item in ctx.para_declare():
            var = self.visitPara_declare(item)
            if isinstance(var, list):
                paraList.extend(var)
            else:
                paraList.append(var)
        return paraList
        # return list(map(lambda x: x.accept(self), ctx.para_declare()))


# -----------------------------------------------------------------------------------------

    def visitStatement(self, ctx: MCParser.StatementContext):
        # return list(map(lambda x: Stmt(x.accept(self)), ctx.stmt()))
        stmts = []
        for stmt in ctx.stmt():
            stmtItem = self.visitStmt(stmt)
            if isinstance(stmtItem, list):
                stmts.extend(stmtItem)
            else:
                stmts.append(stmtItem)
        return stmts

    def visitStmt(self, ctx: MCParser.StmtContext):
        return self.visitChildren(ctx)
        # return ctx.getChild(0).accept(self)

    def visitIf_stmt(self, ctx: MCParser.If_stmtContext):
        # expr = Expr(ctx.expression().accept(self))
        expr = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.stmt(0))
        if ctx.stmt(1):
            elseStmt = self.visit(ctx.stmt(1))
        else:
            elseStmt = None
        return If(expr, thenStmt, elseStmt)

    def visitDowhile_stmt(self, ctx: MCParser.Dowhile_stmtContext):
        sl = self.visit(ctx.statement())
        expr = self.visit(ctx.expression())
        return Dowhile(sl, expr)

    def visitFor_stmt(self, ctx: MCParser.For_stmtContext):
        expr1 = self.visit(ctx.expression(0))
        expr2 = self.visit(ctx.expression(1))
        expr3 = self.visit(ctx.expression(2))
        loop = self.visit(ctx.stmt())
        return For(expr1, expr2, expr3, loop)

    def visitBreak_stmt(self, ctx: MCParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: MCParser.Continue_stmtContext):
        return Continue()

    def visitReturn_stmt(self, ctx: MCParser.Return_stmtContext):
        if ctx.expression():
            res = self.visit(ctx.expression())
        else:
            res = None
        return Return(res)

    def visitBlock_stmt(self, ctx: MCParser.Block_stmtContext):
        items = []
        for item in ctx.body_block():
            blockItem = self.visitBody_block(item)
            if isinstance(blockItem, list):
                items.extend(blockItem)
            else:
                items.append(blockItem)
        return Block(items)

    def visitBody_block(self, ctx: MCParser.Body_blockContext):
        return self.visitChildren(ctx)

    def visitExpression_stmt(self, ctx: MCParser.Expression_stmtContext):
        return self.visit(ctx.expression())

# ----------------------------------------------------------------------------------------------

    def visitPrimitive_type(self, ctx: MCParser.Primitive_typeContext):
        if ctx.BOOLTYPE():
            return BoolType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.STRINGTYPE():
            return StringType()

# -----------------------------------------------------------------------------------------------

    def visitExpression(self, ctx: MCParser.ExpressionContext):
        if ctx.getChildCount() == 1 and ctx.operands():
            return self.visit(ctx.operands())
        elif ctx.getChildCount() == 1 and ctx.assoc_expression():
            return self.visit(ctx.assoc_expression(0))
        elif ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            return BinaryOp(op, left, right)

    def visitAssoc_expression(self, ctx: MCParser.Assoc_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        elif ctx.getChildCount() == 2:
            op = self.visit(ctx.getChild(0))
            body = self.visit(ctx.getChild(1))
            return UnaryOp(op, body)
        elif ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.assoc_expression(0)), self.visit(ctx.assoc_expression(1)))
        else:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.getChild(1))
            else:
                op = ctx.getChild(1).getText()
                left = self.visit(ctx.getChild(0))
                right = self.visit(ctx.getChild(2))
                return BinaryOp(op, left, right)
    
    def visitEquality_expression(self, ctx: MCParser.Equality_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        elif ctx.getChildCount() == 2:
            op = self.visit(ctx.getChild(0))
            body = self.visit(ctx.getChild(1))
            return UnaryOp(op, body)
        elif ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.equality_expression(0)), self.visit(ctx.equality_expression(1)))
        else:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.getChild(1))
            else:
                op = ctx.getChild(1).getText()
                left = self.visit(ctx.getChild(0))
                right = self.visit(ctx.getChild(2))
                return BinaryOp(op, left, right)

    def visitIndex_expression(self, ctx: MCParser.Index_expressionContext):
        arr = self.visit(ctx.expression(0))
        idx = self.visit(ctx.expression(1))
        return ArrayCell(arr, idx)

    def visitInvocation_expression(self, ctx: MCParser.Invocation_expressionContext):
        return self.visit(ctx.function_call())

    def visitList_expression(self, ctx: MCParser.List_expressionContext):
        items = []
        for item in ctx.expression():
            expItem = self.visitExpression(item)
            if isinstance(expItem, list):
                items.extend(expItem)
            else:
                items.append(expItem)
        return items

# ---------------------------------------------------------------------------------------------------

    def visitFunction_call(self, ctx: MCParser.Function_callContext):
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.list_expression())
        return CallExpr(method, param)

    def visitOperands(self, ctx: MCParser.OperandsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.getChild(0))

    def visitLiterals(self, ctx:MCParser.LiteralsContext):
        if ctx.IntLIT():
            return IntLiteral(int(ctx.IntLIT().getText()))
        elif ctx.FloatLIT():
            return FloatLiteral(float(ctx.FloatLIT().getText()))
        elif ctx.BooleanLIT():
            return BooleanLiteral(ctx.BooleanLIT().getText())
        else:
            return StringLiteral(ctx.StringLIT().getText())

    # def visitMctype(self,ctx:MCParser.MctypeContext):
    #     if ctx.INTTYPE():
    #         return IntType
    #     else:
    #         return VoidType

    # def visitBody(self,ctx:MCParser.BodyContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self,ctx:MCParser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self,ctx:MCParser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))
