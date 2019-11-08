
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
            @x: list(Return(), Symbol())
            @func: FuncDecl() class
        '''
        if ast.returnType is FloatType:
            if not (x[1].mtype is FloatType or x[1].mtype is IntType):
                raise TypeMismatchInStatement(x[0])
        elif ast.returnType is ArrayPointerType:
            if x[1].mtype is ArrayType or x[1].mtype is ArrayPointerType:
                if not x[1].mtype.eleType is ast.returnType.eleType:
                    raise TypeMismatchInStatement(x[0])
        elif x[1].mtype != ast.returnType:
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
            if called == False:
                raise UnreachableFunction(name)

    def visitFuncDecl(self,ast, c): 
        # TODO: Control return STMT yet or not, control return Type
        # ! create function to check each Return with ast.returnType
        self.isReturn = False
        self.returnStmt = []

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
        if not self.isReturn and ast.returnType is not VoidType:
            raise FunctionNotReturn(ast.name.name)

    def visitBlock(self, ast, c):
        # ! Return list of list
        # body = functools.reduce(lambda env, member: [env[0] + [self.visit(member, env)]] + env[1:], ast.member, [[]] + c)
        env = [[]] + c
        blockMember = [[]]
        for x in ast.member:
            if isinstance(x, VarDecl):
                env = [env[0] + self.visit(x, env), env[1]]
            else:
                mem = self.visit(x, env)
                if isinstance(mem[0], Symbol):
                    blockMember = blockMember[:-1] + [blockMember[0] + mem]
                else:
                    blockMember = mem + blockMember 
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
        if not isinstance(self.visit(ast.expr,c), BoolType):
            raise TypeMismatchInStatement(ast)
        thenStmt = self.visit(ast.thenStmt, c)
        if isinstance(thenStmt[0], Symbol):
            if thenStmt[0].name == 'return':
                thenReturn = True
            else:
                thenReturn = False
        else:
            thenReturn = (self.lookup('return', self.flatten(thenStmt), lambda x: x.name) != None)

        if ast.elseStmt is not None:
            elseStmt = self.visit(ast.elseStmt, c)
            if isinstance(elseStmt[0], Symbol):
                if elseStmt[0].name == 'return':
                    elseReturn = True
                else:
                    elseReturn = False
            else:
                elseReturn = (self.lookup('return', self.flatten(elseStmt), lambda x: x.name) != None)
            if thenReturn == elseReturn == True:
                self.isReturn = True
            
        return [Symbol("if", None)]

    def visitFor(self, ast, c):
        if not isinstance(self.visit(ast.expr1, c), IntType):
            raise TypeMismatchInStatement(ast)
        if not isinstance(self.visit(ast.expr2, c), BoolType):
            raise TypeMismatchInStatement(ast)
        if not isinstance(self.visit(ast.expr3, c), IntType):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, [c[0] + [Symbol("loop", None)]] + c[1:]) 
        return [Symbol("0_loop", None)]

    def visitDowhile(self, ast, c):
        if not isinstance(self.visit(ast.exp, c), BoolType):
            raise TypeMismatchInStatement(ast)
        functools.reduce(lambda env, mem: self.visit(mem, env), ast.sl, [c[0] + [Symbol("loop", None)]] + c[1:])
        return [Symbol("0_loop", None)]

    def visitBreak(self, ast, c):
        # TODO: Check loop Symbol in previous scope (or all scope)
        if not self.lookup("0_loop", self.flatten(c), lambda x: x.name):
            raise BreakNotInLoop()

    def visitContinue(self, ast, c):
        if not self.lookup("0_loop", self.flatten(c), lambda x: x.name):
            raise ContinueNotInLoop()

    def visitReturn(self, ast, c):
        if ast.expr is None:
            retStmt = Symbol("return", VoidType())
        else:
            retStmt = Symbol("return", self.visit(ast.expr, c))
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

        if op in ['+', '-', '*', '/', '%']:
            if lhsType == IntType and rhsType == IntType:
                return IntType
            elif lhsType in [IntType, FloatType] and rhsType in [IntType, FloatType]:
                return FloatType
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['<', '>', '<=', '>=']:
            if lhsType in [IntType, FloatType] and rhsType in [IntType, FloatType]:
                return BoolType
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['==', '!=']:
            if lhsType == rhs and lhsType in [IntType, BoolType]:
                return BoolType
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['&&', '||']:
            if lhsType == BoolType and rhsType == BoolType:
                return BoolType
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '=':
            # ! If lhs not Id, ArrayCell -> No Left Value
            if isinstance(lhs, Symbol):
                # * Consider more with ArrayPointerType and some potential Error
                # ! Despite type = ArrayType, it's ArrayCell which use eleType in ArrayType
                if type(lhsType) == ArrayType:
                    if type(rhsType) == ArrayType:
                        if type(lhsType.eleType) == type(rhsType.eleType) or (type(lhsType.eleType) == FloatType and type(rhsType) == IntType):
                            return True
                        else:
                            return False
                    # rhs is Id or Literal
                    elif type(rhsType) == type(lhsType.eleType) or (type(lhsType.eleType) == FloatType and type(rhsType) == IntType):
                        return True
                    else:
                        raise TypeMismatchInExpression(ast)
                # * LHS is a Id because Symbol (has name) but not 2 kind of ArrayType
                elif type(lhsType) != ArrayPointerType:
                    # * RHS is ArrayCell
                    if type(rhsType) == ArrayType:
                        if type(lhsType) == type(rhsType.eleType) or (type(lhsType) == FloatType and type(rhsType) == IntType):
                            return True
                        else:
                            return False 
                    # * RHS is Id or Literal, can't be ArrayPointerType because it cause error from ASTGen
                    elif type(rhsType) == type(lhsType) or (type(lhsType) == FloatType and type(rhsType) == IntType):
                        return True
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
                return IntType
            elif type(body) == FloatType:
                return FloatType
            else:
                raise TypeMismatchInExpression(ast)
        elif op == '!':
            if type(body) == BoolType:
                return BoolType
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitId(self, ast, c):
        res = self.lookup(ast.name, self.flatten(c), lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier, ast.name)
        else:
            return res # Return Symbol(name, type)

    def visitArrayCell(self, ast, c):
        # * Handle Undeclared from visitId -> return Symbol(name, mtype) (type = ArrayType, ArrayPointerType)
        arrType = self.visit(ast.arr, c)
        if self.visit(ast.idx, c) != IntType:
            raise TypeMismatchInExpression(ast)
        elif type(arrType.mtype) == ArrayType or type(arrType.mtype) == ArrayPointerType:
            return arrType
        else: 
            raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c): 
        # TODO: Handle TypeMismatchInExp when different parameter in function declare c[-1]
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

# --------------------------------------------------------------------------------
    def visitIntLiteral(self,ast, c): 
        return IntType()
    
    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitIntType(self, param):
        return super().visitIntType(param)