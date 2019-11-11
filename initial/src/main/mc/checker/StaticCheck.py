
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
import functools


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        # print(ast)
        # print(ast)
        # print()
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def flatten(self, lst):
        return [x for i in lst for x in i]

    def getType(self, ast):
        if isinstance(ast, VarDecl):
            return ast.varType
        else:
            listPara = list(map(lambda x: x.varType, ast.param))
            return MType(listPara, ast.returnType)

    def visitProgram(self, ast, c):
        # global_decl = []
        # for x in ast.decl:
        #     if self.getName(x) not in global_decl:
        #         global_decl.append(self.getName(x))
        #     else:
        #         raise Redeclared(Function(), self.getName(x))
        # self.scope.append(global_decl)

        # return functools.reduce(lambda env, decl: env.append(self.visit(decl, env)), ast.decl, self.scope)
        return functools.reduce(lambda env, decl: [env[0] + self.visit(decl, env)], ast.decl, [[]])

    def visitFuncDecl(self, ast, c):
        # if ast.name.name in c[0]:
        if self.lookup(ast.name.name, self.flatten(c), lambda x: x.name) != None:
            raise Redeclared(Function(), ast.name.name)
        glenv = [[Symbol(ast.name.name, self.getType(ast))] + c[0]]

        try:
            param = functools.reduce(
                lambda env, decl: [env[0] + self.visit(decl, env)], ast.param, [[]])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)
        env = param + glenv
        for x in ast.body.member:
            if type(x) == VarDecl:
                env = [env[0] + self.visit(x, env), env[1]]
            else:
                self.visit(x, env)
        # functools.reduce(lambda env, member: [env[0] + self.visit(member, env), env[1]] , ast.body.member , param + glenv)

        return [Symbol(ast.name.name, self.getType(ast))]

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable, self.flatten(c), lambda x: x.name) != None:
        # if ast.variable in c[0]:
            raise Redeclared(Variable(), ast.variable)
        return [Symbol(ast.variable, self.getType(ast))]

    # def visitCallExpr(self, ast, c):
    #     at = [self.visit(x, (c[0], False)) for x in ast.param]

    #     res = self.lookup(ast.method.name, c[0], lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(), ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype

    def visitBlock(self, ast, c):
        functools.reduce(lambda env, member: [env[0] + self.visit(member, env)], ast.member, [[]] + c)
        return []

    def visitId(self, ast, c):
        res = self.lookup(ast.name, self.flatten(c), lambda x: x.name)
        if res == None:
        # if not ast.name in self.flatten(c):
            raise Undeclared(Identifier(), ast.name)
        else:
            return res

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBinaryOp(self, ast, c):
        op = ast.op
        lhs = self.visit(ast.left, c)
        rhs = self.visit(ast.right, c)
        
        lhs = lhs.mtype if type(lhs) == Symbol else lhs
        rhs = rhs.mtype if type(rhs) == Symbol else rhs

        if op in ['+', '-', '*']:
            if lhs == rhs == IntType():
                return IntType()
            else:
                return FloatType()
        elif op == '=':
            if lhs == rhs == IntType():
                return IntType()
            elif lhs == FloatType() and rhs in [FloatType(), IntType()]:
                return FloatType()
            else:
                raise TypeMismatchInStatement(ast)
        else:
            raise TypeMismatchInExpression(ast)