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

    def test_if_float(self):
        input = '''int main() {
            if (a == 2)
                return 2;
        }'''
        self.assertTrue(TestParser.checkParser(input, success, 210))

    def test_if_float(self):
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
