import unittest
# from TestUtils import TestParser
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
        input = """int main () { return 0; }"""
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

    def test_global_var(self):
        input = """float a;"""
        self.assertTrue(TestParser.checkParser(input, success, 205))

    def test_var_int(self):
        input = """int main() { 
        float a; 
        }"""
        self.assertTrue(TestParser.checkParser(input, success, 206))