import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

# Simple function declare -----------------------------------------------------------------------------------------------------
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

    def test_func_array(self):
        input = '''int main(int argv[]){
            int a;
        }'''
        expect = 'Program([FuncDecl(Id(main),[VarDecl(Id(argv),ArrayTypePointer(IntType))],IntType,Block([VarDecl(Id(a),IntType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_pointer_func(self):
        input = '''int[] bar() {
            int c[3];
        }'''
        expect = 'Program([FuncDecl(Id(bar),[],ArrayTypePointer(IntType),Block([VarDecl(Id(c),ArrayType(IntType,IntLiteral(3)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_global_bool(self):
        input = '''boolean visited;'''
        expect = 'Program([VarDecl(Id(visited),BoolType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_declare_assign(self):
        input = '''int a;
        void main() {
            a = 2;
        }'''
        expect = 'Program([VarDecl(Id(a),IntType),FuncDecl(Id(main),[],None,Block([BinaryOp(=,Id(a),IntLiteral(2))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_local_global(self):
        input = ''' float a;
        int main() {
            int b;
        }'''
        expect = 'Program([VarDecl(Id(a),FloatType),FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(b),IntType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_bool_func(self):
        input = '''boolean foo(){}'''
        expect = 'Program([FuncDecl(Id(foo),[],BoolType,Block([]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

# Variable Manipulation -----------------------------------------------------------------------------------------------
    def test_var_declare(self):
        input = """int main() {
            int a;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),IntType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_multivar(self):
        input = """int main() {
            int a,b;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_floatvar(self):
        input = """int main() {
            float a;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),FloatType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_boolvar(self):
        input = """int main() {
            boolean a;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),BoolType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_strvar(self):
        input = """int main() {
            string a;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),StringType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_global_float(self):
        input = '''float var;'''
        expect = 'Program([VarDecl(Id(var),FloatType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_global_int(self):
        input = """int a;"""
        expect = 'Program([VarDecl(Id(a),IntType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_global_str(self):
        input = '''string a, b, c;'''
        expect = 'Program([VarDecl(Id(a),StringType),VarDecl(Id(b),StringType),VarDecl(Id(c),StringType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

# Statement ------------------------------------------------------------------------------------------------------------

    def test_2if(self):
        input = '''int main(){
            if (true)
                return 1;
            if (a)
                return 2;
            else 
                return 3;
            else 
                return 4;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([If(BooleanLiteral(true),Return(IntLiteral(1))),If(Id(a),Return(IntLiteral(2)),Return(IntLiteral(3))),Return(IntLiteral(4))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))


# Function call -------------------------------------------------------------------------------------------------------- 

    def test_funccall_nopara(self):
        input = '''int main() {
            flush();
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(flush),[])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_funccall_para(self):
        input = '''int main() {
            print(1);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[IntLiteral(1)])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_funccall_multipara(self):
        input = '''int main() {
            print(1,true);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[IntLiteral(1),BooleanLiteral(true)])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_funccall_assocpara(self):
        input = '''int main() {
            print(1 + 2);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[BinaryOp(+,IntLiteral(1),IntLiteral(2))])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_funccall_float(self):
        input = '''int main(){
            print(1.2);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[FloatLiteral(1.2)])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

# Expression -----------------------------------------------------------------------------------------------------

    def test_assign_bracket(self):
        input = '''int main() {
            n  = ((((((((((((((((((n))))))))))))))/2))));
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(2)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))