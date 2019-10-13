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

    def test_1d_global(self):
        input = '''int a[5];'''
        expect = 'Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_1d_local(self):
        input = '''int main(){ int a[5]; }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

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

    def test_break_stmt(self):
        input = '''int main() {
            break;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Break()]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_continue_stmt(self):
        input = '''void main() {
            if(true)
                continue;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],None,Block([If(BooleanLiteral(true),Continue())]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_return_bool(self):
        input = '''int main() { return a == b;}'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(BinaryOp(==,Id(a),Id(b)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_return_not(self):
        input = '''int main() { return !a;}'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(UnaryOp(!,Id(a)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_return_add(self):
        input = '''int man() { return 1 + 2;}'''
        expect = 'Program([FuncDecl(Id(man),[],IntType,Block([Return(BinaryOp(+,IntLiteral(1),IntLiteral(2)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_return_add_id(self):
        input = '''int add() { return a + b;}'''
        expect = 'Program([FuncDecl(Id(add),[],IntType,Block([Return(BinaryOp(+,Id(a),Id(b)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_return_or(self):
        input = '''int or() {
            return true || a;
        }'''
        expect = 'Program([FuncDecl(Id(or),[],IntType,Block([Return(BinaryOp(||,BooleanLiteral(true),Id(a)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_return_assign(self):
        input = '''void ass(int a, int b){
            return a = b;
        }'''
        expect = 'Program([FuncDecl(Id(ass),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],None,Block([Return(BinaryOp(=,Id(a),Id(b)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_return_1d(self):
        input = '''void arr(int a[]){ return a[3]; }'''
        expect = 'Program([FuncDecl(Id(arr),[VarDecl(Id(a),ArrayTypePointer(IntType))],None,Block([Return(ArrayCell(Id(a),IntLiteral(3)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_return_arrInarr(self):
        input = '''int main() { return a[b[3]]; }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(ArrayCell(Id(a),ArrayCell(Id(b),IntLiteral(3))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_return_inverse(self):
        input = '''int main() { return -id; }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(UnaryOp(-,Id(id)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_return_func(self):
        input = '''int main() { return add(x, y); }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(CallExpr(Id(add),[Id(x),Id(y)]))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_return_enclosedBracket(self):
        input = '''int main() { return (a == b || a != b);}'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(a),Id(b))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_if_else(self):
        input = '''int main() { if (a < 2) return true; else return false;}'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(2)),Return(BooleanLiteral(true)),Return(BooleanLiteral(false)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_if_block(self):
        input = '''int main(){
            if (a > 100){
                a = 101;
                b = 102;
            }
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(a),IntLiteral(100)),Block([BinaryOp(=,Id(a),IntLiteral(101)),BinaryOp(=,Id(b),IntLiteral(102))]))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_elif(self):
        input = '''int main(){
            if (a > 10)
                return a;
            else if (a > 100)
                return 10;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(a),IntLiteral(10)),Return(Id(a)),If(BinaryOp(>,Id(a),IntLiteral(100)),Return(IntLiteral(10))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_do_while_block(self):
        input = '''int main() {
            do {
            print("1"); }
            while (true);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([CallExpr(Id(print),[StringLiteral(1)])])],BooleanLiteral(true))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_dowhile_stmt(self):
        input = '''int main() {
            do print("2");
            while (false);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([CallExpr(Id(print),[StringLiteral(2)])],BooleanLiteral(false))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_dowhile_bracketless(self):
        input = '''int main() {
            do 
                a = a + 1;
                b = b - 1;
            while a < b;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(b),BinaryOp(-,Id(b),IntLiteral(1)))],BinaryOp(<,Id(a),Id(b)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_dowhile_varblock(self):
        input = '''int main() { 
            do { int a, b; a = a + 1;} while (a > b);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])],BinaryOp(>,Id(a),Id(b)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_for(self):
        input = '''int main() {
            for (i = 0; i < n; i = i + 2)
                ok = true;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(2)));BinaryOp(=,Id(ok),BooleanLiteral(true)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_or_mix(self):
        input = '''int main() {
            if (ok || it || done || yet)
                return;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(||,BinaryOp(||,BinaryOp(||,Id(ok),Id(it)),Id(done)),Id(yet)),Return())]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_and_mix(self):
        input = '''int main() {
            if (ok && now && it && done)
                return true;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,Id(ok),Id(now)),Id(it)),Id(done)),Return(BooleanLiteral(true)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))


# Function call -------------------------------------------------------------------------------------------------------- 

    def test_funccall_nopara(self):
        input = '''int main() {
            flush();
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(flush),[])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_funccall_para(self):
        input = '''int main() {
            print(1);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[IntLiteral(1)])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_funccall_multipara(self):
        input = '''int main() {
            print(1,true);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[IntLiteral(1),BooleanLiteral(true)])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_funccall_assocpara(self):
        input = '''int main() {
            print(1 + 2);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[BinaryOp(+,IntLiteral(1),IntLiteral(2))])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_funccall_float(self):
        input = '''int main(){
            print(1.2);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(print),[FloatLiteral(1.2)])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_declare_after_func(self):
        input = '''int main() {}
        int a;'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([])),VarDecl(Id(a),IntType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

# Expression -----------------------------------------------------------------------------------------------------

    def test_assign_bracket(self):
        input = '''int main() {
            n  = ((((((((((((((((((n))))))))))))))/2))));
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(2)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_infinite_neg(self):
        input = '''int main(){
            a = --------a;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(a))))))))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_mod(self):
        input = '''int mod (){ return a % b; }'''
        expect = 'Program([FuncDecl(Id(mod),[],IntType,Block([Return(BinaryOp(%,Id(a),Id(b)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_div(self):
        input = '''int div() { return a / b/ c;}'''
        expect = 'Program([FuncDecl(Id(div),[],IntType,Block([Return(BinaryOp(/,BinaryOp(/,Id(a),Id(b)),Id(c)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_bool_not(self):
        input = '''int main() { ok = !false;}'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(ok),UnaryOp(!,BooleanLiteral(false)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_reverse_ass(self):
        input = '''int main() { z + y+ x = a + b; }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,BinaryOp(+,BinaryOp(+,Id(z),Id(y)),Id(x)),BinaryOp(+,Id(a),Id(b)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_multi_assign(self):
        input = '''int main() {a = b = c;}'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(=,Id(b),Id(c)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))
    
    def test_not_exp(self):
        input = '''int main() {
            return !false;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(UnaryOp(!,BooleanLiteral(false)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_list_exp(self):
        input = '''void main() {
            return add(a + 1, b < 0);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],None,Block([Return(CallExpr(Id(add),[BinaryOp(+,Id(a),IntLiteral(1)),BinaryOp(<,Id(b),IntLiteral(0))]))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_exp_stmt(self):
        input = '''int main() {
            a + 1;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,Id(a),IntLiteral(1))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_or_stmt(self):
        input = '''int main() {
            stmt1 / stmt2 || false;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(||,BinaryOp(/,Id(stmt1),Id(stmt2)),BooleanLiteral(false))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_geq_not(self):
        input = '''int main() {
            return 3 > !2;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(BinaryOp(>,IntLiteral(3),UnaryOp(!,IntLiteral(2))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_block_var(self):
        input = '''int main() {
            int a;
            {int b; float c;}
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),IntType),Block([VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType)])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_cmp_bracket(self):
        input = '''int main() {
            return (a == b) != c;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(BinaryOp(!=,BinaryOp(==,Id(a),Id(b)),Id(c)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

# Odd program ------------------------------------------------------------------------------------------

    def test_empty(self):
        input = ''''''
        expect = 'Program([])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_recursion(self):
        input = '''int main(){
            return add(add(x, y), add(u, v));
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(CallExpr(Id(add),[CallExpr(Id(add),[Id(x),Id(y)]),CallExpr(Id(add),[Id(u),Id(v)])]))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))