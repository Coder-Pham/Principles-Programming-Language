import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([]))])'
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_more_complex_program(self):
        """Program with parameter"""
        input = """int main (int argc) {}"""
        expect = 'Program([FuncDecl(Id(main),[VarDecl(Id(argc),IntType)],IntType,Block([]))])'
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_multi_program(self):
        """Multi declare function"""
        input = """int main () {}
        int calc() {}"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([])),FuncDecl(Id(calc),[],IntType,Block([]))])'
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
   
    def test_output_para(self):
        input = """int[] main() {}"""
        expect = 'Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_var_declare(self):
        input = """int main() {
            int a;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),IntType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))