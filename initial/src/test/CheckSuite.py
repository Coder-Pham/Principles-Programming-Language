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
    # ---------------------------------------------------------------------------------------------------------------------------

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
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_local_global(self):
        input = Program([VarDecl('a',IntType),FuncDecl(Id("main"),[],IntType(),Block([VarDecl('a',IntType),VarDecl('a',FloatType)]))])
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 406))

    # -------------------------------------------------------------------------------
    def test_redecl_para(self):
        input = Program([FuncDecl(Id('main'), [VarDecl(
            'argc', IntType), VarDecl('argc', IntType)], IntType, Block([]))])
        expect = 'Redeclared Parameter: argc'
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redecl_local(self):
        input = Program([FuncDecl(Id('main'), [VarDecl(
            'argc', IntType)], IntType, Block([VarDecl('argc', IntType)]))])
        expect = 'Redeclared Variable: argc'
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redecl_global(self):
        input = Program([VarDecl('argc', IntType), FuncDecl(Id('main'), [
                        VarDecl('argc', IntType)], IntType, Block([VarDecl('argc', IntType)]))])
        expect = 'Redeclared Variable: argc'
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redecl_multi(self):
        input = Program([VarDecl('b', IntType), FuncDecl(Id('main'), [VarDecl(
            'a', IntType), VarDecl('a', IntType)], IntType, Block([VarDecl('b', IntType)]))])
        expect = 'Redeclared Parameter: a'
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redecl_func(self):
        input = Program([FuncDecl(Id('main'), [VarDecl('argc', IntType)], IntType, Block([])), FuncDecl(
            Id('main'), [VarDecl('argc', IntType)], IntType, Block([VarDecl('argc', IntType)]))])
        expect = 'Redeclared Function: main'
        self.assertTrue(TestChecker.test(input, expect, 411))

# ------------------------------------------------------------------------------------------------------------------

    def test_undecl_main(self):
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([Id('a')]))])
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_undecl_para(self):
        input = Program([FuncDecl(Id("main"),[VarDecl('a',IntType())],IntType(),Block([Id('a'), Id('b')]))])
        expect = 'Undeclared Identifier: b'
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_undecl_global(self):
        input = Program([VarDecl('a',IntType()),FuncDecl(Id("main"),[VarDecl('a',IntType())],IntType(),Block([Id('a'), Id('b')]))])
        expect = 'Undeclared Identifier: b'
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_undecl_block(self):
        input = Program([VarDecl('a',IntType()),FuncDecl(Id("main"),[VarDecl('a',IntType())],IntType(),Block([VarDecl('m',IntType()),Block([VarDecl('b',IntType()), Id('a'),Id('d'),Id('m')])]))])
        expect = 'Undeclared Identifier: d'
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_undecl_block(self):
        input = Program([VarDecl('a',IntType()),FuncDecl(Id("main"),[VarDecl('a',IntType())],IntType(),Block([VarDecl('a',IntType()),Block([VarDecl('b',IntType()), Id('a'),Id('d'),Id('m')])]))])
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 416))