import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     input = """void main() {
    #         putFloat(5.5);
    #     }"""
    #     expect = "5.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))
    
    # def test_int_ast(self):
    # 	input = Program([FuncDecl(Id("main"),[], VoidType(),Block([CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,502))
    
    # def test_global_decl(self):
    #     input = '''int a;
    #     void main(){
    #         a = 1;
    #         putInt(a);
    #     }'''
    #     expect = '1'
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))
    
    # def test_local_decl(self):
    #     input = '''void main() {
    #         int a;
    #         a = 5;
    #         putInt(a);
    #     }'''
    #     expect = '5'
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))

    # def test_mod(self):
    #     input = '''void main(){
    #         putInt(5 % 4);
    #     }'''
    #     expect = '1'
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    # def test_local_block(self):
    #     input = '''void main(){
    #         int a;
    #         {
    #             a = 2;
    #             putInt(a);
    #         }
    #         a = 5;
    #         putInt(a);
    #     }'''
    #     expect = '25'
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test_funcdecl(self):
    #     input = '''int cal(){
    #         return 1 + 1;
    #     }
    #     void main() {
    #         putInt(cal());
    #     }'''
    #     expect = '2'
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))

    # def test_put_cmp(self):
    #     input = '''void main() {
    #         boolean a;
    #         a = 1 > 2;
    #         putBool(a);
    #     }'''
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))

    # def test_not_bool(self):
    #     input = '''void main() {
    #         boolean a;
    #         a = true;
    #         putBoolLn(!a);
    #     }'''
    #     expect = 'false\n'
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))

    # def test_noAss_func(self):
    #     input = '''int sol (){
    #         return 1 + 1 * 5 / 2;
    #     }
    #     void main() {
    #         string a;
    #         sol();
    #         a = "sol";
    #         putString(a);
    #     }'''
    #     expect = 'sol'
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))

    # def test_callExp_void(self):
    #     input = '''int a;
    #     void cal(){
    #         a = 1;
    #     }
    #     void main(){
    #         cal();
    #         putInt(a);
    #     }'''
    #     expect = '1'
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))

    # def test_para_funcdecl(self):
    #     input = '''int sum(int a, int b, int c){
    #         return a + b +c;
    #     }
    #     void main(){
    #         putInt(sum(1, 2, 3));
    #     }'''
    #     expect = '6'
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))

    # def test_para_voidFunc(self):
    #     input = '''int a;
    #     void assign(int b, int c) {
    #         a = 1;
    #         b = 5;
    #     }
    #     void main(){
    #         int b;
    #         b = 1;
    #         assign(a, b);
    #         putInt(a);
    #     }'''
    #     expect = '1'
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))

    # def test_cmp_float(self):
    #     input = '''void main(){
    #         boolean result;
    #         result = 1.2 > 2.4;
    #         putBool(result);
    #     }'''
    #     expect = 'false'
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))

    # def test_complicate_cal(self):
    #     input = '''void main() { 
    #         int x, y; 
    #         x = 10; 
    #         y = 100; 
    #         float a, b, c; 
    #         a = x / 25.4; 
    #         b = y / 12.4; 
    #         c = (a * b + x) / y + y / (a*b + 2 / x);
    #         putFloat(c); 
    #     }'''
    #     expect = '31.627752'
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))

    # def test_simple_dowhile(self):
    #     input = '''void main(){
    #         int a;
    #         a = 1;
    #         do 
    #             a = 2 * a;
    #         while (a < 10);
    #         putInt(a);
    #     }'''
    #     expect = '16'
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test_break_in_dowhile(self):
    #     input = '''int cal(){
    #         int a;
    #         a = 1;
    #         do 
    #             a = 2 * a;
    #             break;
    #         while (true);
    #         return a;
    #     }
    #     void main(){
    #         putInt(cal());
    #     }'''
    #     expect = '2'
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))

    # # ! ERROR: return in IF in DOWHILE
    # def test_continue_in_dowhile(self):
    #     input = '''int cal() {
    #         int a;
    #         a = 1;
    #         do 
    #             a = a * 3;
    #             if (a >= 10)
    #                 break;
    #         while (true);
    #         return a;
    #     }
    #     void main(){
    #         putIntLn(cal());
    #     }'''
    #     expect = '27\n'
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test_break_continue(self):
    #     input = '''int cal() {
    #         int a;
    #         a = 1;
    #         do 
    #             a = a * 3;
    #             if (a > 10)
    #                 break;
    #             else 
    #                 continue;
    #         while (true);
    #         return a;
    #     }
    #     void main(){
    #         putIntLn(cal());
    #     }'''
    #     expect = '27\n'
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))

    # def test_if_stmt(self):
    #     input = '''void main(){
    #         int a;
    #         a = 1;
    #         if (a > 2)
    #             putInt(a);
    #         else
    #             putInt(1);
    #     }'''
    #     expect = '1'
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test_ifelse_dowhile(self):
    #     input = '''int cal(int a){
    #         do
    #             if (a <= -10)
    #                 break;
    #             else {
    #                 a = a + -2;
    #                 continue;
    #             }
    #         while (true);
    #         return a;
    #     }
    #     void main(){
    #         int a;
    #         a = 1;
    #         putInt(cal(a));
    #     }'''
    #     expect = '-11'
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # def test_for_loop(self):
    #     input = '''void main(){
    #         int a;
    #         for(a = 1; a < 5; a = a + 1)
    #             putInt(a);
    #     }'''
    #     expect = '1234'
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))

    # def test_true_loopExp1(self):
    #     input = '''void main() {
    #         int a;
    #         a = 1;
    #         for (true; a < 5; a = a + 2)
    #             continue;
    #         putInt(a + 1);
    #     }'''
    #     expect = '6'
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))

    # def test_return_float(self):
    #     input = '''float ff() { return 5.0; } 
    #     void main() { 
    #         putFloatLn(ff()); 
    #     }'''
    #     expect = '5.0\n'
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))

    # def test_return_str(self):
    #     input = '''string hello(){
    #         return "hello";
    #     }
    #     void main() {
    #         putString(hello());
    #     }'''
    #     expect = 'hello'
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))

    # def test_cmpl_literal_cal(self):
    #     input = '''void main(){
    #         putInt(1 * (2 + (3 - (4 / 2) % 3)));
    #         return;
    #     }'''
    #     expect = '3'
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))

    # def test_10_decimal(self):
    #     input = '''void main(){
    #         putFloat(1.0102030405);
    #     }'''
    #     expect = '1.010203'
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))

    # def test_putInt_bool(self):
    #     input = '''void main(){
    #         putInt(true);
    #         return;
    #     }'''
    #     expect = '1'
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))

    # def test_complicate_cmp(self):
    #     input = '''void main(){
    #         putBool((1 > 2) < ((1 < -2) <= 6));
    #     }'''
    #     expect = 'true'
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))

    # def test_mix_and(self):
    #     input = '''void main() {
    #         putBool(2 && (1.3 > 5));
    #     }'''
    #     expect = 'false'
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))

    # def test_mix_binOp(self):
    #     input = """void main(){
    #         putBool(2 && (1.3 > 5) == (true || false));
    #     }"""
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))

    # def test_floating_point(self):
    #     input = '''void main() {
    #         putFloat(1.3456789e5);
    #     }'''
    #     expect = '134567.89'
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))

    # def test_end_globalvar(self):
    #     input = '''void main() {
    #         putFloat(var = 2.1);
    #     }
    #     float var;'''
    #     expect = '2.1'
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))

    # def test_dowhile_block(self):
    #     input = '''void main(){ 
    #         int a; 
    #         float b; 
    #         b = 4+5 - (a = 3); 
    #         putIntLn(a);
    #         putFloat(b);
    #     }'''
    #     expect = '3\n6.0'
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))

    # def test_all_float_cmp(self):
    #     input = '''void main(){
    #         putBoolLn(1.3 > 2.4);
    #         putBoolLn(1.4 < 2.4);
    #         putBoolLn(1.3 >= 2.4);
    #         putBoolLn(1.4 <= 2.4);
    #     }'''
    #     expect = 'false\ntrue\nfalse\ntrue\n'
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))

    # def test_andor_bool(self):
    #     input = '''void main(){
    #         putBool(true||true||false&&true||false);
    #     }'''
    #     expect = 'true'
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))

    # def test_print_plus_assign(self):
    #     input = '''void main() {
    #         int a, b;
    #         a = 1;
    #         putInt(a = b = a + a + 1 );
    #         putInt(b);
    #     }'''
    #     expect = '33'
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))

    # def test_assign_before_add(self):
    #     input = '''float a;
    #     void main() {
    #         putFloat((a = 103) - 4);
    #     }'''
    #     expect = '99'
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))

    # def test_complex_assign_and_others(self):
    #     input = '''void main(){
    #         4*2;
    #         putBool((((a = 3) - 1) * 3.2) <= ((b = 2.2) + 3));
    #     }
    #     int a;
    #     float b;'''
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 539))

    # def test_not_op(self):
    #     input = '''void main() {
    #         putBool(!(3 > 2));
    #     }'''
    #     expect = 'false'
    #     self.assertTrue(TestCodeGen.test(input, expect, 540))

    # def test_not_0_int(self):
    #     input = '''void main() {
    #         putBool(!0);
    #     }'''
    #     expect = 'true'
    #     self.assertTrue(TestCodeGen.test(input, expect, 541))

    # def test_not_1_int(self):
    #     input = '''void main() {
    #         putBool(!1);
    #     }'''
    #     expect = 'false'
    #     self.assertTrue(TestCodeGen.test(input, expect, 542))

# ---------------------------------------------------------------------------------------------------------------
    def test_many_negative_op(self):
        input = """
        float fl;
        void main(){
            fl = 4.0/5*12/34.2 - 3 + 99/4 - -----4*7 - ----3 - ---- 13;
            putFloat(fl);
        }"""
        expect = "33.2807"
        self.assertTrue(TestCodeGen.test(input, expect, 543))
    
    def test_decl_in_func(self):
        input = """void main(){
            float fl;
            int i;
            i = 1;
            fl = -i;
            putFloatLn(fl);
            int a;
            a = 12%(i+4);
            putFloat(a);
        }
        float fl;"""
        expect = "-1.0\n2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_many_put_line(self):
        input = """void main(){
            putFloat(fl=2.1);
            putLn();
            putLn();
            putLn();
            putLn();
            putLn();
            putBool(fl>2);
            putLn();
            putLn();
        }
        float fl;"""
        expect = "2.1\n\n\n\n\ntrue\n\n"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_var_decl_in_block(self):
        input = """void main(){
            {
                int b;
                {
                    b = 4;
                    int a;
                    {
                        a = 5;
                        int i;
                        i = 3;
                        putFloatLn(5%3);
                        putFloat(b-a-i);
                    }
                }
            }
        }"""
        expect = "2.0\n-4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_call_func_and_return(self):
        input = """void main(){
            putInt(foo());
        }
        int foo(){
            return 12;
        }"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_simple_call_int_func(self):
        input = """void main(){
            putInt(foo(10));
        }
        int foo(int a){
            return a;
        }"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_string_call_func(self):
        input = """void main(){
            putString(foo("553"));
        }
        string foo(string a){
            return a;
        }"""
        expect = "553"
        self.assertTrue(TestCodeGen.test(input, expect, 549))
    
    def test_bool_call_func(self):
        input = """void main(){
            putBool(foo(1));
        }
        boolean foo(int a){
            return a;
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_many_call_func(self):
        input = """int foo1(){
            int a;
            a = 5;
            return a;
        }
        float foo2(int a){
            return foo1()+a;
        }
        void main(){
            putIntLn(foo3());
            putFloat(foo2(3));
        }
        boolean foo3(){
            return true;
        }"""
        expect = "1\n8.0"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_call_func_in_op(self):
        input = """void main(){
            int f;
            f = foo1();
            putFloat(foo2(5)*3+f);
        }
        int foo1(){
            int a;
            a = 5;
            return a;
        }
        float foo2(int a){
            return foo1()+a;
        }"""
        expect = "35.0"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_simple_if(self):
        input = """void main(){
            if(true)
                putFloat(12);
        }"""
        expect = """12.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_if_label_in_else(self):
        input = """void main(){
            if(false)
                putFloat(12);
            else
                putInt(1);
        }"""
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_relational_op_in_if_condi(self):
        input = """void main(){
            if(12>4)
                putFloatLn(3);
            putInt(3);
        }"""
        expect = """3.0\n3"""
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_var_relational_op_in_if(self):
        input = """
        float fl;
        void main(){
            fl = 2;
            if(fl == 2)
                putFloatLn(fl);
            else
                putIntLn(21);
            putInt(3);
        }"""
        expect = "2.0\n3"
        self.assertTrue(TestCodeGen.test(input, expect, 556))
    
    def test_many_stmt_in_if(self):
        input = """void main(){
            fl = 12; 
            if(-1.2>3){
                putInt(43);
                fl = fl - 33;
                putFloat(fl);
            } else {
                putFloatLn(fl);
                putInt(12);
            }
        }
        float fl;"""
        expect = "12.0\n12"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_many_block_in_if(self):
        input = """void main(){
            {
                int b;
                {
                    b = 4;
                    if(b != 0){
                        int a;
                        {
                            a = 5;
                            int i;
                            i = 3;
                            putFloatLn(5%3);
                            putFloat(b-a-i);
                        }
                    } else 
                        putInt(0);
                }
            }
        }"""
        expect = "2.0\n-4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_simple_dowhile(self):
        input = """void main(){
            do
                putInt(12);
            while(false);
        }"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_simple_for(self):
        input = """void main(){
            int i;
            for(i=0; i<5; i=i+1)
                putIntLn(i);
            putInt(i);
        }"""
        expect = "0\n1\n2\n3\n4\n5"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_many_block_in_for(self):
        input = """void main(){
            {
                int b;
                for(b=1; b<12; b=b*2){
                    putIntLn(b);
                    if(b != 0){
                        int a;
                        {
                            a = 5;
                            int i;
                            i = 3;
                            putFloatLn(5%3);
                            putFloatLn(-a-i);
                        }
                    } else 
                        putInt(0);
                }
            }
        }"""
        expect = "1\n2.0\n-8.0\n2\n2.0\n-8.0\n4\n2.0\n-8.0\n8\n2.0\n-8.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_complex_if(self):
        input = """void main(){
            int a, b;
            a = 2;
            if(a != 2){ 
                {
                    putInt(a); // 2
                }
            } else {
                b = 2;
                if(a>b)
                    putInt(b*a); // 4
                else
                    if(a < b)
                        putInt(a-b); // 0
                    else
                        putInt(a/b); // 1
            } 
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_more_complex_dowhile(self):
        input = """void main(){
            check = 12;
            int a;
            do{
                do
                    a = 2;
                    do
                        putIntLn(a = a*2 - 1);
                    while(a < 5);
                    break;
                while(a != 100);
                putLn();

                a = 2;
                do
                    putIntLn(a=a*2-1);
                while(a < 5);
                check = check + 1;
            }
            while(check < 15);
        }
        int check;"""
        expect = "3\n5\n\n3\n5\n3\n5\n\n3\n5\n3\n5\n\n3\n5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_complex_for(self):
        input = """void main(){
            int a, b;
            {
                {
                    {
                        for(a=0; a<10; a=a+1)
                            for(b=5; b<50; b=b+10){
                                putFloatLn(b-a);
                                a=b;
                                if(a > 30)
                                    break;
                            }
                    }
                }
                {
                    for(b=0; b<12; b=b*2){
                        int c;
                        c = 10;
                        a = (c+b)/2;
                        putIntLn(b=a);
                    }
                }
            }
        }"""
        expect = "5.0\n10.0\n10.0\n10.0\n5\n10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_dowhile_if_for(self):
        input = """void main(){
            check = 5;
            if(check) {
                int a;
                a = 5;
                if(a)
                    do
                        for(a=0; a<4; a=a+1)
                            putIntLn(a);
                        putString("end");
                        if(a > 0)
                            break;
                    while(true);
            }
        }
        int check;"""
        expect = "0\n1\n2\n3\nend"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_return_if_in_other_func(self):
        input = """void main(){
            int a;
            for(a=0; a<6; a=a+1){
                putIntLn(foo(a));
            }
        }
        int foo(int a){
            if(a>2)
                return 2;
            return 1;
        }"""
        expect = "1\n1\n1\n2\n2\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 566))
    
    def test_return_stop_dowhile_in_other_func(self):
        input = """void main(){
            putInt(foo());
        }
        int foo(){
            int b;
            b = 0;
            do
                b = b+1;
                if(b==3)
                    return b;
            while(b<5);
            return 1;
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_return_stop_for_in_other_func(self):
        input = """void main(){
            putInt(foo(12));
        }
        int foo(int a){
            for(a=0; a<5; a=a+1)
                if(a==3)
                    return a;
            return 1;
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_for_in_dowhile(self):
        input = """void main(){
            int a;
            a = -5;
            int b;
            do
                for(b=0; b<3; b=b+1){
                    a = a+b;
                    putIntLn(a);
                }
            while(a<5);
        }"""
        expect = "-5\n-4\n-2\n-2\n-1\n1\n1\n2\n4\n4\n5\n7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_complex_for_in_branch(self):
        input = """void main(){
            int a, b;
            a = 2;
            if(a != 2){ 
                {
                    putInt(a); // 2
                }
            } else {
                b = 2;
                if(a<=b)
                    for(a=2; a<=b; a=a+1){
                        b = 10;
                        putIntLn(b*a);
                    }
                else
                    if(a < b)
                        putInt(a-b); // 0
                    else
                        putInt(a/b); // 1
            } 
        }"""
        expect = "20\n30\n40\n50\n60\n70\n80\n90\n100\n"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_complex_func_call(self):
        input = """boolean boo() {
            a = 2;
            if(a==2)
                putStringLn(str());
            fl = 3;
            return flo() > fl;
        }
        int a;
        int foo(){
            a = 3;
            return a;
        }
        float flo(){ 
            putIntLn(foo());
            return fl+1;
        }
        void main(){ 
            putBool(boo()); 
        }
        string str() {
            return "hello";
        }
        float fl;"""
        expect = "hello\n3\ntrue"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_complex_mix_stmt(self):
        input = """void main(){ 
            int a,b;
            a = 2;
            b = 3;
            float fl;
            {
                fl = 3;
                if(a>b){
                    {
                        for(a=6; b<a; b=b+1){
                            if(fl>2.2)
                                a=b;
                        }
                    }
                } else {
                    do
                        fl = fl * a + b / fl;
                        if(a==b)
                            putFloatLn(fl); 
                        else 
                            putFloatLn(fl = fl - -1);
                    while(fl<12.2);
                }
            }
        }"""
        expect = "8.0\n17.375\n"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_multiple_not_func(self):
        input = """void main(){
            int i;
            for(i=0; i<5; i=i+1){
                if(i>3)
                    putBoolLn(!!!!!!boo(false));
                else
                    putBoolLn(!!!!boo(true));
            }
        }
        boolean boo(boolean boo){
            return boo;
        }"""
        expect = "true\ntrue\ntrue\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_return_true_via_odd_value(self):
        input = """void main(){
            int i;
            for(i=0; i<5; i=i+1){
                putBoolLn(boo(false, i));
            }
        }
        boolean boo(boolean boo, int i){
            if(i%2)
                return boo;
            else
                return !boo;
            return false;
        }"""
        expect = "true\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 574))
    
    def test_simple_recursive(self):
        input = """int i;
        void main(){
            i = 0;
            putInt(foo());
        }
        int foo(){
            if(i>3){
                return i;
            }
            i = i + 1;
            return foo();
        }"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_tail_call_optimal(self):
        input = """float foo(float a, float b){
            /* comment
            */
            if(a == 1 && a > 0)
                return b;
            return foo(a-1, a*b);
        }
        void main(){
            // tail call opt
            putFloat(foo(8, 1));
        }"""
        expect = "40320.0"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_factorial_prog(self):
        input = """int fact(int x){
            int fact, i;
            fact = 1;
            for(i=1; i<=x; i=i+1){
                fact = fact * i;
            }
            return fact;
        }
        void main(){
            for(a=2; a<15; a=a+1){
                putIntLn(fact(a));
            }
            putString("stop!");
        }
        int a;"""
        expect = "2\n6\n24\n120\n720\n5040\n40320\n362880\n3628800\n39916800\n479001600\n1932053504\n1278945280\nstop!"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_fibonacci_prog(self):
        input = """void main(){
            int i, n1, n2, next;
            n2 = (n1=next=0)+1;
            for (i = 1; i <= 25; i=i+1){
                if(i == 1){
                    putString("first:");
                    putIntLn(n1);
                    continue;
                }
                if(i == 2){
                    putString("second:");
                    putIntLn(n2);
                    continue;
                }
                next = n1 + n2;
                n1 = n2;
                n2 = next;
                putIntLn(next);
            }
            return;
        }"""
        expect = "first:0\nsecond:1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n89\n144\n233\n377\n610\n987\n1597\n2584\n4181\n6765\n10946\n17711\n28657\n46368\n"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_complex_program(self):
        input = """boolean boo(boolean bool) {
            a = 2;
            if(a==2) {
                {
                    if(bool) {
                        for(a=0; bool; a=a+1){
                            return bool;
                        }
                    }
                    return bool;
                }
            }
            else 
                return bool;
            return bool;
        }
        int a;
        float flo() {
            do
                fl = 5;
                a = a + 2;
                if(a==2) {
                    {
                        if(bool) {
                            for(a=0; bool; a=a+1){
                                return -----1111121;
                            }
                        }
                        return fl;
                    }
                }
                else {
                    if(bool) {
                        return fl*fl;
                    }
                }
            while(boo(bool));
            return fl;
        }
        void main() {
            bool = true;
            putBoolLn(boo(bool));
            putFloat(flo());
        }
        float fl;
        boolean bool;"""
        expect = "true\n-1111121.0"
        self.assertTrue(TestCodeGen.test(input, expect, 579))