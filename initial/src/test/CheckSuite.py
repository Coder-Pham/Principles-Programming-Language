import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    '''
    - 15 Redeclared (1 - 15)
    - 20 Undeclared (16 - 35)
    - 15 MismatchStatement (36 - 50)
    - 15 MismatchExp (51 - 65)
    - 10 Not return (66 - 75)
    - 5 Break/Continue in Loop (76 - 80)
    - 5 No entry (81 - 85)
    - 5 Unreachable function (86 - 90)
    - 10 Not Left Value (91 - 100)
    '''
# ------------------------------------------------------------------------------------
    def test_redeclare_local(self):
        input = '''void main(){
            int a;
            a = 1;
            float a;
        }'''
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclare_func(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl('a',IntType())])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl('b',IntType())]))])
        expect = 'Redeclared Function: main'
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclare_para(self):
        input = '''void main(int a, int b, float a){
            bool c;
        }'''
        expect = 'Redeclared Parameter: a'
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redecl_paralc(self):
        input = Program([FuncDecl(Id("main"),[VarDecl("argc", IntType())],VoidType(), Block([VarDecl("argc", IntType())]))])
        expect = 'Redeclared Variable: argc'
        self.assertTrue(TestChecker.test(input, expect, 404))

# -------------------------------------------------------------------------------------
    def test_undeclared_function(self):
        input = """int main() { foo(); }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclared_var(self):
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),IntLiteral(1))]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,417))

# -------------------------------------------------------------------------------
    def test_return_pointer(self):
        input = ''' int[] foo(int a[]) { return 1; }
        void main(){
            int a[3];
            foo(a);
        }'''
        expect = 'Type Mismatch In Statement: Return(IntLiteral(1))'
        self.assertTrue(TestChecker.test(input, expect, 436))

# ---------------------------------------------------------------------------------

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """int main () {
            putIntLn();
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """int main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[CallExpr(Id("getInt"),[IntLiteral(4)])])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_diff_numofparam_stmt_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_assign(self):
        input = '''int main() {
            int a;
            int b[3];
            a = b;
            return 0;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_condition_func(self):
        input = '''int foo() { return 1; }
        int main(){
            int a;
            if (foo() == 1)
            {
                a = 0;
            }
            return a;
        }'''
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 456))

# ------------------------------------------------------------------------------------    
    def test_no_return(self):
        input = '''int main(){ int a; }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_if_return(self):
        input = '''int main() {
            if (true)
            {
                int a;
                return 1;
            }
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 467))

    
    def test_assign(self):
        input = '''int[] main(int c[]){
            int a[4];
            return a;
        }'''
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 468))

# --------------------------------------------------------------------------------------
    def test_func_notcall(self):
        input = '''int foo() { return 0; }
        int main(){ return 1; }'''
        expect = 'Unreachable Function: foo'
        self.assertTrue(TestChecker.test(input, expect, 486))
