import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    '''
    - 10 Redeclared (1 - 10)
    - 10 Undeclared (11 - 20)
    - 25 MismatchStatement (21 - 45)
    - 25 MismatchExp (46 - 70)
    - 10 Not return (71 - 80)
    - 5 Break/Continue in Loop (81 - 85)
    - 5 No entry (86 - 90)
    - 5 Unreachable function (91 - 95)
    - 5 Not Left Value (96 - 100)
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

    def test_builtin(self):
        input = '''void putLn(){}
        void main(){
            int a;
        }'''
        expect = 'Redeclared Function: putLn'
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redecl_block(self):
        input = '''void main() {
            int a;
            {
                float a;
                if (a >= 1)
                {
                    boolean a;
                    a = true;
                }
                int a;
            }
        }'''
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_func_diffType(self):
        input = '''int foo(){ int a; return a; }
        void main(){
            int foo;
        }
        float foo(int bar) { return bar; }'''
        expect = 'Redeclared Function: foo'
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redecl_var_after(self):
        input = '''int main(){
            main = 0;
            return main;
        }
        int main;'''
        expect = 'Redeclared Variable: main'
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_(self):
        input = '''int main;
        void main(){
            a = 0;
        }
        int a;'''
        expect = 'Redeclared Function: main'
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redecl_inblock(self):
        input = '''void main(){
            {   
                float a;
                a = getFloat();
                int a;
                a = getInt();
            }
        }'''
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 410))

# -------------------------------------------------------------------------------------
    def test_undeclared_function(self):
        input = """int main() { foo(); }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_var(self):
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),IntLiteral(1))]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_callexp_noBracket(self):
        input = '''int foo(){ return 3 ; }
        void main() { foo; foo(); }'''
        expect = 'Undeclared Identifier: foo'
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_call_id(self):
        input = '''int foo;
        void main(){
            foo();
        }'''
        expect = 'Undeclared Function: foo'
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_func_cell(self):
        input = '''float a(int b) 
        { 
            return b + 2.5;
        }
        void main() { 
            a[10] ; 
        }'''
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input, expect, 415))

# -------------------------------------------------------------------------------
    def test_return_pointer(self):
        input = ''' int[] foo(int a[]) { return 1; }
        void main(){
            int a[3];
            foo(a);
        }'''
        expect = 'Type Mismatch In Statement: Return(IntLiteral(1))'
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_return_void(self):
        input = '''void foo(){ return; }
        void main(){
            return foo();
        }'''
        expect = 'Type Mismatch In Statement: Return(CallExpr(Id(foo),[]))'
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_condition_func(self):
        input = '''int foo() { return 1; }
        int main(){
            int a;
            if (foo() + 1)
                return a = 0;
            return a;
        }'''
        expect = 'Type Mismatch In Statement: If(BinaryOp(+,CallExpr(Id(foo),[]),IntLiteral(1)),Return(BinaryOp(=,Id(a),IntLiteral(0))))'
        self.assertTrue(TestChecker.test(input, expect, 423))

# ---------------------------------------------------------------------------------

    def test_miss_para(self):
        input = """void foo(int a){ a = 1; }
        int main () {
            foo();
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_morethan_para(self):
        input = """int main () {
            int a;
            a = getInt(4);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_assign(self):
        input = '''int main() {
            int a;
            int b[3];
            a = b;
            return 0;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_assign(self):
        input = '''int[] foo(int c[]){ return c; }
        void main(){
            int a[3], b[5];
            b = foo(a);
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(b),CallExpr(Id(foo),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_pointer_assign(self):
        input = '''int[] foo(){ int a[3]; return a; }
        void main() {
            foo()[2] = 2;
        }'''
        expect = 'Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[]),IntLiteral(2))'
        self.assertTrue(TestChecker.test(input, expect, 451))

# ----------------------------------------------------------------------------------------
    def test_no_return(self):
        input = '''int main(){ int a; }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_if_return(self):
        input = '''int main() {
            if (true)
            {
                int a;
                return 1;
            }
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_multi_if(self):
        input = '''int main() {
            int a;
            if (a == 2)
                if (a < 4)
                    return 2;
                else 
                    return 1;
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_for_if(self):
        input = '''int main(){
            int a;
            for (a = 1; a < 5; a = a + 1)
                if (a > 3)
                    return 1;
                else
                    return 2;
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 474))

# --------------------------------------------------------------------------------------
    def test_func_notcall(self):
        input = '''int foo() { return 0; }
        int main(){ return 1; }'''
        expect = 'Unreachable Function: foo'
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_call_itself(self):
        input = """int[] foo(int a, int b[], int c[])
        {
            int arr[9];
            foo(3,arr,foo(12,arr,arr));
            return arr ;
        }
        void main(){
            return ; 
        }"""
        expect = 'Unreachable Function: foo'
        self.assertTrue(TestChecker.test(input, expect, 492))

# -----------------------------------------------------------------------------------

    def test_assign_void(self):
        input = '''void foo(){
            int a ;
        }
        void main(){
            float a ;
            foo() = a ;
        }'''
        expect = 'Not Left Value: BinaryOp(=,CallExpr(Id(foo),[]),Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_sth(self):
        input = '''int foo() {
            do
                return 1;
                continue;
            while(false);
        }

        int goo(){  
            do
                continue;
                return 1;
            while(false);
        }
        void main(){
            foo();
            goo();
        }'''
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 497))