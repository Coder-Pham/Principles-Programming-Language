
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
        if ast.name.name in c[0]:
            raise Redeclared(Function(), ast.name.name)
        glenv = [[ast.name.name] + c[0]]

        try:
            param = functools.reduce(
                lambda env, decl: [env[0] + self.visit(decl, env)], ast.param, [[]])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)

        functools.reduce(lambda env, member: [env[0] + self.visit(member, env), env[1]] , ast.body.member , param + glenv)

        return [ast.name.name]

    def visitVarDecl(self, ast, c):
        if ast.variable in c[0]:
            raise Redeclared(Variable(), ast.variable)
        return [ast.variable]

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
        if not ast.name in self.flatten(c):
            raise Undeclared(Identifier(), ast.name)
        else:
            return []

    def visitIntLiteral(self, ast, c):
        return IntType()
