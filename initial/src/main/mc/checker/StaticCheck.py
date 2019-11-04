
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

    def visitProgram(self, ast, c):
        return functools.reduce(lambda env, decl: env + [self.visit(decl, env)], ast.decl, [])

    def visitFuncDecl(self, ast, c):
        if ast.name.name in c:
            raise Redeclared(Function(), ast.name.name)

        try:
            param = functools.reduce(
                lambda env, decl: env + [self.visit(decl, env)], ast.param, [])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)

        body = functools.reduce(lambda env, decl: env + [self.visit(decl, env)], list(
            filter(lambda x: type(x) in [VarDecl,Id,Block], ast.body.member)), param)

        return ast.name.name

    def visitVarDecl(self, ast, c):
        if ast.variable in c:
            raise Redeclared(Variable(), ast.variable)
        return ast.variable

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
        return [self.visit(x, c) for x in ast.member]

    def visitId(self, ast, c):
        res = self.lookup(ast.name, c, lambda x: x)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        else:
            return ast.name

    def visitIntLiteral(self, ast, c):
        return IntType()
