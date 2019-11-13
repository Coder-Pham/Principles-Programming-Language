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

    def test_redcl_main(self):
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

    def test_undecl_inStmt(self):
        input = '''void main() {
            for (a = 1; a < 4; a = a + 1)
                break;
        }'''
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_varName_func(self):
        input = '''int foo() { return 1; }
        void main() {
            foo = 1;
        }'''
        expect = 'Undeclared Identifier: foo'
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_funcCall_in_builtin(self):
        input = '''int main() {
            putIntLn(toInt(4));
            return 0;
        }'''
        expect = 'Undeclared Function: toInt'
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_used_before_decl(self):
        input = '''int main(){
            if (true)
            {
                a = 1;
                {
                    float a;
                    a = 2.5;
                }
            }
            return 0;
        }'''
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_useBuilin_asVar(self):
        input = '''int main(){
            int a;
            a = getInt;
            return a;
        }'''
        expect = 'Undeclared Identifier: getInt'
        self.assertTrue(TestChecker.test(input, expect, 420))

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

    def test_for_startVal(self):
        input = '''int main(){
            int a;
            for (a == 1; a < 5; a = a + 1){
                putIntLn(a);
            }
            return 0;
        }'''
        expect = 'Type Mismatch In Statement: For(BinaryOp(==,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(5));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([CallExpr(Id(putIntLn),[Id(a)])]))'
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_for_noInitStart(self):
        input = '''int main(){
            int a;
            for (a ; a < 5; a = a * 2)
                putInt(a);
            return 0;
        }'''
        expect = 'Type Mismatch In Statement: For(Id(a);BinaryOp(<,Id(a),IntLiteral(5));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));CallExpr(Id(putInt),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_for_startUnary(self):
        input = '''int main(){
            float a;
            a = 1;
            for (-a; a < 5; a = a + 5)
                putFloat(a);
            return a;
        }'''
        expect = 'Type Mismatch In Statement: For(UnaryOp(-,Id(a));BinaryOp(<,Id(a),IntLiteral(5));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(5)));CallExpr(Id(putFloat),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_for_initFloat(self):
        input = '''void main(){
            float a;
            for (a = 0.25; a < 1; a = a + 0.05)
                putFloat(a);
        }'''
        expect = 'Type Mismatch In Statement: For(BinaryOp(=,Id(a),FloatLiteral(0.25));BinaryOp(<,Id(a),IntLiteral(1));BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(0.05)));CallExpr(Id(putFloat),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_for_assignCondition(self):
        input = '''int main() {
            int a;
            for (a = 1; a = 4; a = a - 1)
                putFloat(a);
            return 0;
        }'''
        expect = 'Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(=,Id(a),IntLiteral(4));BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1)));CallExpr(Id(putFloat),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_for_unOpexp2(self):
        input = '''void main() {
            int a;
            for (a = 1; -a; a = a - 1)
                putInt(a);
        }'''
        expect = 'Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));UnaryOp(-,Id(a));BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(1)));CallExpr(Id(putInt),[Id(a)]))'
        self.assertTrue(TestChecker.test(input, expect, 429))

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

    def test_not_int(self):
        input = '''void main(){
            int a;
            boolean b;
            b = !a;
        }'''
        expect = 'Type Mismatch In Expression: UnaryOp(!,Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_not_float(self):
        input = '''int main(){
            float a;
            boolean bar;
            bar = !a;
        }'''
        expect = 'Type Mismatch In Expression: UnaryOp(!,Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_FloatInt_reverse(self):
        input = '''void main() {
            float a; int b;
            b = a;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_negative_bool(self):
        input = '''int main(){
            boolean visited;
            return -visited;
        }'''
        expect = 'Type Mismatch In Expression: UnaryOp(-,Id(visited))'
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_plus_str(self):
        input = '''void main(){
            string a, b;
            a = "Hello";
            b = "PPL";
            a = a + b;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_comp_diff_type(self):
        input = '''void main() {
            float a;
            string b;
            a > b;
        }'''
        expect = 'Type Mismatch In Expression: BinaryOp(>,Id(a),Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 457))

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

    def test_if_for_if(self):
        input = '''int main(){
            int a;
            if (a > 1)
                for (a = 2; a < 5; a = a + 1) {
                    if (a < 5)
                        return 1;
                }
            else 
                return 0;
        }'''
        expect = 'Function main Not Return '
        self.assertTrue(TestChecker.test(input, expect, 475))

# ----------------------------------------------------------------------------------------
    def test_bool_main(self):
        input = '''boolean ex() {
            return main();
        }'''
        expect = 'No Entry Point'
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_only_decl(self):
        input = '''int a, b, c;'''
        expect = 'No Entry Point'
        self.assertTrue(TestChecker.test(input, expect, 487))
        
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

    def test_assign_func2func(self):
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
            foo() = goo();
        }'''
        expect = 'Not Left Value: BinaryOp(=,CallExpr(Id(foo),[]),CallExpr(Id(goo),[]))'
        self.assertTrue(TestChecker.test(input, expect, 497))