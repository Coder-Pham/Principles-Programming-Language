import unittest
from TestUtils import TestParser

success = "successful"


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () { return 1; }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_var_int(self):
        input = """int main() { int a; }"""
        self.assertTrue(TestParser.checkParser(input, success, 204))

    def test_global_float(self):
        input = """float a;"""
        self.assertTrue(TestParser.checkParser(input, success, 205))

    def test_var_float(self):
        input = """int main() { 
        float a; 
        }"""
        self.assertTrue(TestParser.checkParser(input, success, 206))

    def test_while(self):
        input = '''int main() {
            do {
                continue;
            } while (false);
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 207))

    def test_assign(self):
        input = '''int a = 2;'''
        self.assertTrue(TestParser.checkParser(
            input, "Error on line 1 col 6: =", 208))

    def test_if_str(self):
        input = '''int main() {
            if (a == 2)
                return "2";
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 209))

    def test_if_expint(self):
        input = '''int main() {
            if (a == 2)
                return 2;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 210))

    def test_if_expfloat(self):
        input = '''int main() {
            if (a != 2)
                return 2.5;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 211))

    def test_if_bool(self):
        input = '''int main() {
            if (a % 2 == 0)
                return true;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 212))

    def test_global_int(self):
        input = """int a;"""
        self.assertTrue(TestParser.checkParser(input, success, 213))

    def test_global_str(self):
        input = '''string a, b, c;'''
        self.assertTrue(TestParser.checkParser(input, success, 214))

    def test_global_bool(self):
        input = '''boolean visited;'''
        self.assertTrue(TestParser.checkParser(input, success, 215))

    def test_declare_assign(self):
        input = '''int a;
        void main() {
            a = 2;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 216))

    def test_local_global(self):
        input = ''' float a;
        int main() {
            int b;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 217))

    def test_void(self):
        input = '''void main() {
            printf(1);
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 218))

    def test_array(self):
        input = '''int main() {
            int arr[5];
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 219))

    def test_wrong_array(self):
        input = '''int main() {
            int arr[];
        }'''
        self.assertTrue(TestParser.checkParser(input, '''Error on line 2 col 20: ]''', 220))

    def test_array_void(self):
        input = '''int main() {
            void arr[5];
        }'''
        self.assertTrue(TestParser.checkParser(input, 'Error on line 2 col 12: void', 221))

    def test_array_float(self):
        input = '''int main() {
            float arr[10];
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 222))

    def test_array_bool(self):
        input = '''void main() {
            boolean arr[100];
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 223))

    def test_pointer_func(self):
        input = '''int[] bar() {
            int c[3];
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 224))

    def test_pointer_para(self):
        input = '''int main(int argv[]){
            return 0;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 225))

    def test_pointer(self):
        input = '''int[] main(int argv[], int argc) {
            return 0;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 226))

    def test_missed_para(self):
        input = '''int main(int argv[], int ) {
            return 0;
        }'''
        self.assertTrue(TestParser.checkParser(input, 'Error on line 1 col 25: )', 227))

    def test_missed_outpara(self):
        input = '''int main(int argv[){
            print(1);
        }'''
        self.assertTrue(TestParser.checkParser(input, 'Error on line 1 col 18: )', 228))

    def test_return_arr(self):
        input = '''int main(int argc){
            return argv[3];
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 229))

    def test_missed_paratype(self):
        input = '''int main(int argc, argv[]){
            return 'OK';
        }'''
        self.assertTrue(TestParser.checkParser(input, 'Error on line 1 col 19: argv', 230))

    def test_2d_array(self):
        input = '''int main() {
            int foo[2][3];
        }'''
        self.assertTrue(TestParser.checkParser(input, 'Error on line 2 col 22: [', 231))

    def test_2d_assign(self):
        input = '''int main() {
            foo[5][5] = 1;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 232))

    def test_2d_func(self):
        input = '''int main(){
            return foo(2)[3];
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 233))

    def test_2d_func_assign(self):
        input = '''int main() {
            foo(2)[3] = 1+1;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 234))

    def test_func_call(self):
        input = '''void main () {
            int pain; 
            float train; 
            try();
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 235))

    def test_only_funccall(self):
        input = '''int main(){
            printf("OK");
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 236))

    def test_break_stmt(self):
        input = '''int main() {
            break;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 237))

    def test_wrong_break(self):
        input = '''void try() {
            break 1;
        }'''
        self.assertTrue(TestParser.checkParser(input, 'Error on line 2 col 18: 1', 238))

    def test_continue_stmt(self):
        input = '''void main() {
            if(true)
                continue;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 239))

    def test_wrong_continue(self):
        input = '''float main() {
            continue "here";
        }'''
        self.assertTrue(TestParser.checkParser(input, '''Error on line 2 col 21: here''', 240))

    def test_return_bool(self):
        input = '''int main() { return a == b;}'''
        self.assertTrue(TestParser.checkParser(input, success, 241))

    def test_return_not(self):
        input = '''int main() { return !a;}'''
        self.assertTrue(TestParser.checkParser(input, success, 242))

    def test_return_add(self):
        input = '''int man() { return 1 + 2;}'''
        self.assertTrue(TestParser.checkParser(input, success, 243))

    def test_return_add_id(self):
        input = '''int add() { return a + b;}'''
        self.assertTrue(TestParser.checkParser(input, success, 244))

    def test_return_or(self):
        input = '''int or() {
            return true || a;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 245))

    def test_return_assign(self):
        input = '''void ass(int a, int b){
            return a = b;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 246))

    def test_return_1d(self):
        input = '''void arr(int a[]){ return a[3]; }'''
        self.assertTrue(TestParser.checkParser(input, success, 247))

    def test_return_arrInarr(self):
        input = '''int main() { return a[b[3]]; }'''
        self.assertTrue(TestParser.checkParser(input, success, 248))

    def test_return_inverse(self):
        input = '''int main() { return -id; }'''
        self.assertTrue(TestParser.checkParser(input, success, 249))

    def test_return_func(self):
        input = '''int main() { return add(x, y); }'''
        self.assertTrue(TestParser.checkParser(input, success, 250))

    def test_return_enclosedBracket(self):
        input = '''int main() { return (a == b || a != b);}'''
        self.assertTrue(TestParser.checkParser(input, success, 251))

    def test_if_else(self):
        input = '''int main() { if (a < 2) return true; else return false;}'''
        self.assertTrue(TestParser.checkParser(input, success, 252))

    def test_if_block(self):
        input = '''int main(){
            if (a > 100){
                a = 101;
                b = 102;
            }
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 253))

    def test_elif(self):
        input = '''int main(){
            if (a > 10)
                return a;
            else if (a > 100)
                return 10;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 254))