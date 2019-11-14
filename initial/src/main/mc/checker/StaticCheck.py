
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
import functools

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType())),
    Symbol("putInt",MType([IntType()],VoidType())),
    Symbol("getFloat",MType([],FloatType())),
    Symbol("putFloat",MType([FloatType()],VoidType())),
    Symbol("putFloatLn",MType([FloatType()],VoidType())),
    Symbol("putBool",MType([BoolType()],VoidType())),
    Symbol("putBoolLn",MType([BoolType()],VoidType())),
    Symbol("putString",MType([StringType()],VoidType())),
    Symbol("putStringLn",MType([StringType()],VoidType())),
    Symbol("putLn",MType([],VoidType()))
    ]
            
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def flatten(self, lst):
        return [x for i in lst for x in i]

    def getName(self, ast):
        if isinstance(ast, VarDecl):
            return ast.variable
        else:
            return ast.name.name

    def getType(self, ast):
        if isinstance(ast, VarDecl):
            return ast.varType
        else:
            listPara = list(map(lambda x: x.varType, ast.param))
            return MType(listPara, ast.returnType)

    def getKind(self, ast):
        if isinstance(ast, VarDecl):
            return Variable()
        else:
            return Function()

    def checkType(self, x, func):
        '''
            @x: list(Return_AST_node, Symbol("return", Symbol_x))
                Symbol_x.mtype: Type -> Literal
                Symbol_x.mtype: Symbol -> Id, ArrayType (Cell), ArrayPointerType
                    -> Symbol_x.mtype.mtype: Type
            @func: FuncDecl() class
        NOTE: if function need to return IntType, but we return Id of ArrayType (First address of array) -> OK
        '''
        # If return a ID, ArrayCell, ArrayPointer
        if type(x[1].mtype) == Symbol:
            if type(func.returnType) == FloatType:
                # Return arrayCell OR first address of Array
                if type(x[1].mtype.mtype) in [ArrayPointerType, ArrayType] and type(x[1].mtype.mtype.eleType) not in [FloatType, IntType]:
                    raise TypeMismatchInStatement(x[0])
                if not isinstance(x[1].mtype.mtype, IntType) and not isinstance(x[1].mtype.mtype, FloatType):
                    raise TypeMismatchInStatement(x[0])
            elif type(func.returnType) == ArrayPointerType and type(x[1].mtype.mtype) in [ArrayPointerType, ArrayType]: 
                stmtType = type(x[1].mtype.mtype.eleType)
                if type(func.returnType.eleType) == FloatType:
                    if stmtType not in [IntType, FloatType]:
                        raise TypeMismatchInStatement(x[0])
                else:
                    if stmtType != type(func.returnType.eleType):
                        raise TypeMismatchInStatement(x[0])
            elif type(func.returnType) != type(x[1].mtype.mtype):
                raise TypeMismatchInStatement(x[0]) 
        # If return a Literal
        else:
            if type(func.returnType) == FloatType:
                if not x[1].mtype in [FloatType(), IntType()]:
                    raise TypeMismatchInStatement(x[0])
            elif type(func.returnType) == VoidType:
                if not isinstance(x[1].mtype, VoidType):
                    raise TypeMismatchInStatement(x[0])
            elif func.returnType != x[1].mtype :
                raise TypeMismatchInStatement(x[0])

# ------------------------------------------------------------------------------------

    def visitProgram(self,ast, c): 
        glenv = [self.global_envi.copy()]
        self.funcCall = dict()
        for x in ast.decl:
            exist = self.lookup(self.getName(x), glenv[0], lambda x: x.name)
            # TODO: all global declaration
            if exist == None:
                glenv[0] = [Symbol(self.getName(x), self.getType(x))] + glenv[0]
            else:
                raise Redeclared(self.getKind(x), self.getName(x))

            if isinstance(x, FuncDecl):
                self.funcCall[self.getName(x)] = False
        
        # TODO: No Entry Point
        if not self.lookup('main', glenv[0], lambda x: x.name):
            raise NoEntryPoint()

        for x in ast.decl: 
            if isinstance(x, FuncDecl):
                self.visit(x, glenv)

        # TODO: Unreachable function
        for name, called in self.funcCall.items():
            if called == False and name != 'main':
                raise UnreachableFunction(name)

    def visitFuncDecl(self,ast, c): 
        # TODO: Control return STMT yet or not, control return Type
        # ! create function to check each Return with ast.returnType
        self.isReturn = False
        self.returnStmt = []
        self.currentFuncName = ast.name.name

        # TODO: Redeclare parameter
        try:
            param = functools.reduce(lambda env, decl: [env[0] + self.visit(decl, env)], ast.param, [[]])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)

        # TODO: env = only check declare
        env = param + c
        for x in ast.body.member:
            if isinstance(x, Return):
                self.visit(x, env)
                self.isReturn = True
            elif isinstance(x, Break):
                raise BreakNotInLoop()
            elif isinstance(x, Continue):
                raise ContinueNotInLoop()
            elif isinstance(x, VarDecl):
                # env = list of list, env[0] is local 
                env = [env[0] + self.visit(x, env), env[1]]
            else:
                # Check in everything else but dont need to add to list
                # * RETURN a list of list BUT we dont use it here
                self.visit(x, env)
        # member = functools.reduce(lambda env, mem: [env[0] + self.visit(mem, env), env[1]], ast.body.member, param + c)
        # ! TODO: Handle error wrong ReturnType
        for x in self.returnStmt:
            self.checkType(x, ast)

        # ! TODO: Handle error FunctionNotReturn (maybe cant handle in case return in 1 path of IF-ELSE)
        if not self.isReturn and type(ast.returnType) is not VoidType:
            raise FunctionNotReturn(ast.name.name)

    def visitBlock(self, ast, c):
        # ! Return list of list
        # body = functools.reduce(lambda env, member: [env[0] + [self.visit(member, env)]] + env[1:], ast.member, [[]] + c)
        env = [[]] + c
        blockMember = [[]]
        for x in ast.member:
            if isinstance(x, VarDecl):
                env = [env[0] + self.visit(x, env)] + env[1:]
            else:
                mem = self.visit(x, env)
                # If mem = list of list of statement | List of Symbol
                if isinstance(mem, list): 
                    if isinstance(mem[0], Symbol):
                        blockMember = [blockMember[0] + mem] + blockMember[1:] 
                    else:
                        blockMember = mem + blockMember
                # If mem = Expression
                elif type(mem) in [IntType, FloatType, BoolType, StringType]:
                    pass
        return blockMember

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable, c[0], lambda x: x.name):
            raise Redeclared(Variable(), ast.variable)
        return [Symbol(ast.variable, ast.varType)]

    def visitIf(self, ast, c):
        # ! May not need to RETURN
        '''
        - If thenStmt is Return -> thenReturn = True
            + is Block -> lookup('return') -> thenReturn = ?
        - If elseStmt is Return -> elseReturn = True
            + is Block -> lookup('return') -> elseReturn = ?
        - thenReturn == elseReturn == True -> isReturn = true
        '''
        if not type(self.visit(ast.expr,c)) == BoolType:
            raise TypeMismatchInStatement(ast)

        lc_env = [[Symbol("if", None)]]
        thenReturn = elseReturn = False

        thenStmt = self.visit(ast.thenStmt, c)
        # If thenStmt = Expression = Type()
        if type(thenStmt) in [IntType, FloatType, BoolType, StringType]:
            pass
        # If thenStmt = stmt
        elif isinstance(thenStmt[0], Symbol):
            if thenStmt[0].name == 'return':
                lc_env = [thenStmt + lc_env[0]]
                thenReturn = True
            else:
                thenReturn = False
        else:
            lc_env = thenStmt + lc_env
            thenReturn = (self.lookup('return', self.flatten(thenStmt), lambda x: x.name) != None)

        if ast.elseStmt is not None:
            elseStmt = self.visit(ast.elseStmt, c)
            if type(elseStmt) in [IntType, FloatType, BoolType, StringType]:
                pass
            elif isinstance(elseStmt[0], Symbol):
                if elseStmt[0].name == 'return':
                    lc_env = [elseStmt + lc_env[0]]
                    elseReturn = True
                else:
                    elseReturn = False
            else:
                lc_env = elseStmt + lc_env
                elseReturn = (self.lookup('return', self.flatten(elseStmt), lambda x: x.name) != None)

            # ! If has then-else clause, also have return Stmt
            if thenReturn == elseReturn == True:
                self.isReturn = True
            elif thenReturn != elseReturn: 
                self.isReturn = False
        # ! No Else statement & RETURN exists in thenStmt
        elif thenReturn == True:
            self.isReturn = False

        return lc_env

    def visitFor(self, ast, c):
        if not type(self.visit(ast.expr1, c)) == IntType:
            raise TypeMismatchInStatement(ast)
        if not type(self.visit(ast.expr2, c)) == BoolType:
            raise TypeMismatchInStatement(ast)
        if not type(self.visit(ast.expr3, c)) == IntType:
            raise TypeMismatchInStatement(ast)

        # ! If inside loop has RETURN -> Ignore it
        # * If only RETURN in it -> Function No return
        prevReturn = self.isReturn

        self.visit(ast.loop, [c[0] + [Symbol("0_loop", None)]] + c[1:])
        
        self.isReturn = prevReturn
        return [Symbol("0_loop", None)]

    def visitDowhile(self, ast, c):
        if not type(self.visit(ast.exp, c)) == BoolType:
            raise TypeMismatchInStatement(ast)

        doMember = [[]]
        for x in ast.sl:
            mem = self.visit(x, [c[0] + [Symbol("0_loop", None)]] + c[1:])
            if isinstance(mem, list):
                if isinstance(mem[0], list):
                   doMember = mem + doMember
                elif isinstance(mem[0], Symbol):
                    doMember = doMember[:-1] + [[mem[0]] + doMember[-1]]
        # functools.reduce(lambda env, mem: self.visit(mem, env), ast.sl, [c[0] + [Symbol("0_loop", None)]] + c[1:])
        return doMember

    def visitBreak(self, ast, c):
        # TODO: Check loop Symbol in previous scope (or all scope)
        if not self.lookup("0_loop", self.flatten(c), lambda x: x.name):
            raise BreakNotInLoop()

    def visitContinue(self, ast, c):
        if not self.lookup("0_loop", self.flatten(c), lambda x: x.name):
            raise ContinueNotInLoop()

    def visitReturn(self, ast, c):
        self.isReturn = True
        if ast.expr is None:
            retStmt = Symbol("return", VoidType())
        else:
            expr = self.visit(ast.expr, c)
            # Sth is VoidType -> Replace with something else
            # ! SHOULD refactor this
            if isinstance(expr, VoidType):
                retStmt = Symbol("return", IntType)
            else:
                retStmt = Symbol("return", expr)
        self.returnStmt.append([ast, retStmt])
        return [retStmt]

# ------------------------------------------------------------------------------------------------------------------
    def visitBinaryOp(self, ast, c):
        op = ast.op
        # ! Return Type (need more test) or Symbol with Type
        lhs = self.visit(ast.left, c)
        rhs = self.visit(ast.right, c)
        # ! Handle if hand-side not a Literal but a Id (ArrayCell)
        lhsType = lhs.mtype if type(lhs) == Symbol else lhs
        rhsType = rhs.mtype if type(rhs) == Symbol else rhs

        ''' 
        ! Literal -> type(lhsType) == IntType()
        ! Id -> type(lhsType) == IntType()
        ''' 
        
        if op in ['+', '-', '*', '/', '%']:
            if type(lhsType) == type(rhsType) and type(lhsType) == IntType:
                return IntType()
            elif type(lhsType) in [IntType, FloatType] and type(rhsType) in [IntType, FloatType]:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['<', '>', '<=', '>=']:
            if type(lhsType) in [IntType, FloatType] and type(rhsType) in [IntType, FloatType]:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['==', '!=']:
            if type(lhsType) == type(rhsType) and type(lhsType) in [IntType, BoolType]:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['&&', '||']:
            if type(lhsType) == type(rhsType) and type(lhsType) == BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '=':
            # ! If lhs not Id, ArrayCell -> No Left Value
            if isinstance(lhs, Symbol):
                # * Consider more with ArrayPointerType and some potential Error
                # ! Despite type = ArrayType, it's ArrayCell which use eleType in ArrayType
                if type(lhsType) == ArrayType:
                    if type(rhsType) == ArrayType:
                        # * both are ArrayType -> get eleType
                        if type(lhsType.eleType) == type(rhsType.eleType) or (type(lhsType.eleType) == FloatType and type(rhsType.eleType) == IntType):
                            return lhsType.eleType
                        else:
                            raise TypeMismatchInExpression(ast)
                    else:
                        raise TypeMismatchInExpression(ast)
                # * LHS is a Id because Symbol (has name) but not 2 kind of ArrayType
                elif type(lhsType) != ArrayPointerType:
                    # * RHS is ArrayType or ArrayPointerType
                    if type(rhsType) == ArrayType or type(rhsType) == ArrayPointerType:
                        raise TypeMismatchInExpression(ast)
                    # * RHS is Id or ArrayCell or Literal, can't be ArrayPointerType because it cause error from ASTGen
                    elif type(rhsType) == type(lhsType) or (type(lhsType) == FloatType and type(rhsType) == IntType):
                        return lhsType
                    else:
                        raise TypeMismatchInExpression(ast)
            else:
                raise NotLeftValue(ast)
        else:
            raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast, c):
        op = ast.op
        body = self.visit(ast.body, c)
        # * If body is a Id, ArrayCell -> Symbol -> get Type
        body = body.mtype if type(body) == Symbol else body
        # * If body type is a ArrayCell -> get eleType
        if type(body) == ArrayType:
                body = body.eleType
        if op == '-':
            if type(body) == IntType:
                return IntType()
            elif type(body) == FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '!':
            if type(body) == BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitId(self, ast, c):
        # res = self.lookup(ast.name, filter(lambda x: type(x.mtype) != MType, self.flatten(c)), lambda x: x.name)
        res = self.lookup(ast.name, self.flatten(c), lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        else:
            return res # Return Symbol(name, Type)

    def visitArrayCell(self, ast, c):
        # * Handle Undeclared from visitId -> return Symbol(name, mtype) (type = ArrayType, ArrayPointerType)
        arrType = self.visit(ast.arr, c)
        if type(self.visit(ast.idx, c)) != IntType:
            raise TypeMismatchInExpression(ast)

        # * Get ArrayPointerType from function return
        if type(arrType) == ArrayPointerType:
            return Symbol(ast.arr, arrType.eleType)
        # * Get cell from array parameter or arrayType
        elif type(arrType.mtype) == ArrayType or type(arrType.mtype) == ArrayPointerType:
            return Symbol(arrType.name, arrType.mtype.eleType)  # Symbol(name, Type)
        else: 
            raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c): 
        # TODO: Handle TypeMismatchInExp when different parameter in function declare c[-1]
        # * at = [Symbol(name, Type), Symbol(name, ArrayType), Symbol(name, ArrayPointerType)]
        at = [self.visit(x,c) for x in ast.param]
        
        res = self.lookup(ast.method.name, filter(lambda x: type(x.mtype) == MType, c[-1]), lambda x: x.name)
        # * res = Symbol(name, MType([], rettype)) -> res.mtype.partype -> ArrayPointerType.eleType, Type
        if res != None:
            if len(res.mtype.partype) == len(at):
                for i in range(len(at)):
                    lhs = res.mtype.partype[i]
                    rhs = at[i].mtype if type(at[i]) == Symbol else at[i]

                    if type(lhs) == ArrayPointerType:
                        if type(rhs) in [ArrayPointerType, ArrayType] and type(lhs.eleType) == type(rhs.eleType):
                            pass
                        else:
                            raise TypeMismatchInExpression(ast)
                    # * lhs is Type -> rhs is ArrayCell, Id
                    else:
                        if type(rhs) == ArrayType and type(rhs.eleType) == type(lhs):
                            pass 
                        elif type(rhs) == type(lhs):
                            pass
                        else:
                            raise TypeMismatchInExpression(ast)
                # ! Mark that this function has been called at least 1 from another
                if ast.method.name != self.currentFuncName:
                    self.funcCall[ast.method.name] = True
                return res.mtype.rettype
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise Undeclared(Function(), ast.method.name)

# --------------------------------------------------------------------------------
    def visitIntLiteral(self,ast, c): 
        return IntType()
    
    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitIntType(self, ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()
    
    def visitBoolType(self, ast, c):
        return BoolType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitArrayType(self, ast, c):
        return ast
    
    def visitArrayPointerType(self, ast, c):
        return ast