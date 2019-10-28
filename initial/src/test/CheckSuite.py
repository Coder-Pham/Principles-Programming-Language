import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {foo();}"""
    #     expect = "['main']"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "['main']"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int foo () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "['foo']"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int a; """
    #     input = Program([VarDecl('a',IntType)])
    #     expect = "['a']"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([VarDecl('a',IntType),VarDecl('b',IntType)])
    #     expect = "['a', 'b']"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_redelared_func(self):
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("main"),[],IntType(),Block([]))])
        expect = 'Redeclared Function: main'
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclare_var(self):
        input = Program([VarDecl('a',IntType),VarDecl('a',IntType)])
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_redeclare_varfunc(self):
        input = Program([VarDecl('a',IntType),FuncDecl(Id("a"),[],IntType(),Block([]))])
        expect = 'Redeclared Function: a'
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclare_type(self):
        input = Program([VarDecl('a',IntType),VarDecl('a',FloatType)])
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclare_local(self):
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl('a',IntType),VarDecl('a',FloatType)]))])
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_local_global(self):
        input = Program([VarDecl('a',IntType),FuncDecl(Id("main"),[],IntType(),Block([VarDecl('a',IntType),VarDecl('a',FloatType)]))])
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 406))