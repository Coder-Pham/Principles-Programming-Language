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
        expect = 'Program([FuncDecl(Id(main),[VarDecl(argc,IntType)],IntType,Block([]))])'
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
        expect = 'Program([FuncDecl(Id(main),[VarDecl(argv,ArrayTypePointer(IntType))],IntType,Block([VarDecl(a,IntType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_pointer_func(self):
        input = '''int[] bar() {
            int c[3];
        }'''
        expect = 'Program([FuncDecl(Id(bar),[],ArrayTypePointer(IntType),Block([VarDecl(c,ArrayType(IntType,IntLiteral(3)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_global_bool(self):
        input = '''boolean visited;'''
        expect = 'Program([VarDecl(visited,BoolType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_declare_assign(self):
        input = '''int a;
        void main() {
            a = 2;
        }'''
        expect = 'Program([VarDecl(a,IntType),FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),IntLiteral(2))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_local_global(self):
        input = ''' float a;
        int main() {
            int b;
        }'''
        expect = 'Program([VarDecl(a,FloatType),FuncDecl(Id(main),[],IntType,Block([VarDecl(b,IntType)]))])'
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
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_multivar(self):
        input = """int main() {
            int a,b;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_floatvar(self):
        input = """int main() {
            float a;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,FloatType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_boolvar(self):
        input = """int main() {
            boolean a;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,BoolType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_strvar(self):
        input = """int main() {
            string a;
        }"""
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,StringType)]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_global_float(self):
        input = '''float var;'''
        expect = 'Program([VarDecl(var,FloatType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_global_int(self):
        input = """int a;"""
        expect = 'Program([VarDecl(a,IntType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_global_str(self):
        input = '''string a, b, c;'''
        expect = 'Program([VarDecl(a,StringType),VarDecl(b,StringType),VarDecl(c,StringType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_1d_global(self):
        input = '''int a[5];'''
        expect = 'Program([VarDecl(a,ArrayType(IntType,IntLiteral(5)))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_1d_local(self):
        input = '''int main(){ int a[5]; }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(IntType,IntLiteral(5)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

# Statement ------------------------------------------------------------------------------------------------------------

    def test_2if(self):
        input = '''int main(){
            if (true)
                if (a)
                    return 2;
                else 
                    return 3;
            else 
                return 4;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([If(BooleanLiteral(true),If(Id(a),Return(IntLiteral(2)),Return(IntLiteral(3))),Return(IntLiteral(4)))]))])'
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
        expect = 'Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),Continue())]))])'
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
        expect = 'Program([FuncDecl(Id(ass),[VarDecl(a,IntType),VarDecl(b,IntType)],VoidType,Block([Return(BinaryOp(=,Id(a),Id(b)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_return_1d(self):
        input = '''void arr(int a[]){ return a[3]; }'''
        expect = 'Program([FuncDecl(Id(arr),[VarDecl(a,ArrayTypePointer(IntType))],VoidType,Block([Return(ArrayCell(Id(a),IntLiteral(3)))]))])'
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
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([VarDecl(a,IntType),VarDecl(b,IntType),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])],BinaryOp(>,Id(a),Id(b)))]))])'
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

    def test_return_arrfunc(self):
        input = '''int main(){
            return foo(2)[3];
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),IntLiteral(3)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_loop_index(self):
        input = '''int main() {
            for (i[0]; j < i[1]; j=j+1)
                j = 1;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([For(ArrayCell(Id(i),IntLiteral(0));BinaryOp(<,Id(j),ArrayCell(Id(i),IntLiteral(1)));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));BinaryOp(=,Id(j),IntLiteral(1)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_and_loop(self):
        input = '''int main(){
            for(i = 0; i < 3 && i > -1; i *2)
                return 4;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(&&,BinaryOp(<,Id(i),IntLiteral(3)),BinaryOp(>,Id(i),UnaryOp(-,IntLiteral(1))));BinaryOp(*,Id(i),IntLiteral(2));Return(IntLiteral(4)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_not_loop(self):
        input = '''int main(){
            for (-i; !2; i = i+1)
                return 0;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([For(UnaryOp(-,Id(i));UnaryOp(!,IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Return(IntLiteral(0)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_or_loop(self):
        input = '''int bar(){
            for(i; i || j; i / 2)
                print(i);
        }'''
        expect = 'Program([FuncDecl(Id(bar),[],IntType,Block([For(Id(i);BinaryOp(||,Id(i),Id(j));BinaryOp(/,Id(i),IntLiteral(2));CallExpr(Id(print),[Id(i)]))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_andor(self):
        input = '''int bar(){
            for(i; i || 2 && j; i)
                print(i);
        }'''
        expect = 'Program([FuncDecl(Id(bar),[],IntType,Block([For(Id(i);BinaryOp(||,Id(i),BinaryOp(&&,IntLiteral(2),Id(j)));Id(i);CallExpr(Id(print),[Id(i)]))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

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
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([])),VarDecl(a,IntType)])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_loop_func(self):
        input = '''int main() {
            square(add(double(5)));
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(square),[CallExpr(Id(add),[CallExpr(Id(double),[IntLiteral(5)])])])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_add_func(self):
        input = '''int main(){
            return 12+dp(i);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(BinaryOp(+,IntLiteral(12),CallExpr(Id(dp),[Id(i)])))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_or_funccall(self):
        input = '''int main(){
            true || dp(i);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(||,BooleanLiteral(true),CallExpr(Id(dp),[Id(i)]))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_cmp_funccall(self):
        input = '''int foo(){
            dp(i) > 9;
        }'''
        expect = 'Program([FuncDecl(Id(foo),[],IntType,Block([BinaryOp(>,CallExpr(Id(dp),[Id(i)]),IntLiteral(9))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

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
        expect = 'Program([FuncDecl(Id(main),[],VoidType,Block([Return(CallExpr(Id(add),[BinaryOp(+,Id(a),IntLiteral(1)),BinaryOp(<,Id(b),IntLiteral(0))]))]))])'
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
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),Block([VarDecl(b,IntType),VarDecl(c,FloatType)])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_leq_lt(self):
        input = '''void foo() {
            a >= b;
        }'''
        expect = 'Program([FuncDecl(Id(foo),[],VoidType,Block([BinaryOp(>=,Id(a),Id(b))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_cmp_bracket(self):
        input = '''int main() {
            return (a == b) != c;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(BinaryOp(!=,BinaryOp(==,Id(a),Id(b)),Id(c)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_2d_assign(self):
        input = '''int main() {
            return (foo)[5] = 1;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(BinaryOp(=,ArrayCell(Id(foo),IntLiteral(5)),IntLiteral(1)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_2d_func_assign(self):
        input = '''int main() {
            foo(2)[3] = 1+1;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),IntLiteral(3)),BinaryOp(+,IntLiteral(1),IntLiteral(1)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_multi_not(self):
        input = '''void main(){
            return !!!!!!!!!!!!!!a;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],VoidType,Block([Return(UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,Id(a))))))))))))))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))
    
    def test_add_nega(self):
        input = '''int dp(int i){
            return dp(i+1) + -dp(i-1);
        }'''
        expect = 'Program([FuncDecl(Id(dp),[VarDecl(i,IntType)],IntType,Block([Return(BinaryOp(+,CallExpr(Id(dp),[BinaryOp(+,Id(i),IntLiteral(1))]),UnaryOp(-,CallExpr(Id(dp),[BinaryOp(-,Id(i),IntLiteral(1))]))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_multi_add(self):
        '''Test precede of multi add'''
        input = '''int main(){
            a = a + b * 2;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),BinaryOp(*,Id(b),IntLiteral(2))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_multi_addbracket(self):
        input = '''int main(){
            a = (a + b) * 2;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(*,BinaryOp(+,Id(a),Id(b)),IntLiteral(2)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_add_multi_nega(self):
        input = '''int main(){
            a =  1 + 2*-5;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,IntLiteral(1),BinaryOp(*,IntLiteral(2),UnaryOp(-,IntLiteral(5)))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_mix_cmp(self):
        input = '''int main() {
            return a > b != c <= d;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(BinaryOp(!=,BinaryOp(>,Id(a),Id(b)),BinaryOp(<=,Id(c),Id(d))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_cmp_and(self):
        input = '''int foo(){
            (a == 7) != true;
        }'''
        expect = 'Program([FuncDecl(Id(foo),[],IntType,Block([BinaryOp(!=,BinaryOp(==,Id(a),IntLiteral(7)),BooleanLiteral(true))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_or_para(self):
        input = '''int foo(){
            foo(a || b);
        }'''
        expect = 'Program([FuncDecl(Id(foo),[],IntType,Block([CallExpr(Id(foo),[BinaryOp(||,Id(a),Id(b))])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_para_expbracket(self):
        input = '''int bar(){
            foo((a + 2) * 5);
        }'''
        expect = 'Program([FuncDecl(Id(bar),[],IntType,Block([CallExpr(Id(foo),[BinaryOp(*,BinaryOp(+,Id(a),IntLiteral(2)),IntLiteral(5))])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_unary_funccall(self):
        input = '''int main(){
            return -dp(i);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Return(UnaryOp(-,CallExpr(Id(dp),[Id(i)])))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_exp_arrcell(self):
        input = '''int main(){
            dp[2 * x] = 1;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,ArrayCell(Id(dp),BinaryOp(*,IntLiteral(2),Id(x))),IntLiteral(1))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_funccall_if(self):
        input = '''int main(){
            if (accept(7*x))
                return 0;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([If(CallExpr(Id(accept),[BinaryOp(*,IntLiteral(7),Id(x))]),Return(IntLiteral(0)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_mix_unary(self):
        input = '''int main(){
            a = -!15;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),UnaryOp(-,UnaryOp(!,IntLiteral(15))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

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

    def test_assign_funcreturn(self):
        input = '''void foo(int a[]){
            foo()[(2+4)*3] = b+3;
        }'''
        expect = 'Program([FuncDecl(Id(foo),[VarDecl(a,ArrayTypePointer(IntType))],VoidType,Block([BinaryOp(=,ArrayCell(CallExpr(Id(foo),[]),BinaryOp(*,BinaryOp(+,IntLiteral(2),IntLiteral(4)),IntLiteral(3))),BinaryOp(+,Id(b),IntLiteral(3)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_2loop(self):
        input = '''int main(){
            for (i = 0; i < 5; i*2)
                for (j = 0; j < i; j + 1)
                    return 0;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(*,Id(i),IntLiteral(2));For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<,Id(j),Id(i));BinaryOp(+,Id(j),IntLiteral(1));Return(IntLiteral(0))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_2dowhile(self):
        input = '''int main(){
            do
                do
                    print(1);
                while (true);
            while(maybe);
        }'''
        expect = 'Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Dowhile([CallExpr(Id(print),[IntLiteral(1)])],BooleanLiteral(true))],Id(maybe))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_multi_block(self):
        input = '''void main(){{{{{{{
            print("Ok enough");
        }}}}}}}'''
        expect = 'Program([FuncDecl(Id(main),[],VoidType,Block([Block([Block([Block([Block([Block([Block([CallExpr(Id(print),[StringLiteral(Ok enough)])])])])])])])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_block_consecutive(self):
        input = '''void main(){ {}
        { print(1); }
        }'''
        expect = 'Program([FuncDecl(Id(main),[],VoidType,Block([Block([]),Block([CallExpr(Id(print),[IntLiteral(1)])])]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_exp_id(self):
        input = '''int foo() { foo[3] = ((a(c,c*d+false,10.99e1)[3])[10[1]])[c+2]; }'''
        expect = 'Program([FuncDecl(Id(foo),[],IntType,Block([BinaryOp(=,ArrayCell(Id(foo),IntLiteral(3)),ArrayCell(ArrayCell(ArrayCell(CallExpr(Id(a),[Id(c),BinaryOp(+,BinaryOp(*,Id(c),Id(d)),BooleanLiteral(false)),FloatLiteral(109.9)]),IntLiteral(3)),ArrayCell(IntLiteral(10),IntLiteral(1))),BinaryOp(+,Id(c),IntLiteral(2))))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_assign_cmp(self):
        input = '''void main(){
            a = foo(2,5)[a + b] == true;
        }'''
        expect = 'Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(==,ArrayCell(CallExpr(Id(foo),[IntLiteral(2),IntLiteral(5)]),BinaryOp(+,Id(a),Id(b))),BooleanLiteral(true)))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_esc_string(self):
        input = '''void main () {
            int a;
            a = "string \t 1 + a";
        }'''
        expect = 'Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),StringLiteral(string 	 1 + a))]))])'
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))