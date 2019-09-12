import unittest
# from TestUtils import TestLexer
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_low_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme(
            "aCBbdc", "aCBbdc,<EOF>", 102))

    def test_begin_underscore(self):
        self.assertTrue(TestLexer.checkLexeme(
            "aAs_VN", "aAs_VN,<EOF>", 103))

    def test_single_id(self):
        self.assertTrue(TestLexer.checkLexeme("a", "a,<EOF>", 104))

    def test_underscore(self):
        self.assertTrue(TestLexer.checkLexeme("_b2b", "_b2b,<EOF>", 105))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            "aA?sVN", "aA,Error Token ?", 106))

    def test_unicode(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\u0042\u0050", "BP,<EOF>", 107))

    def test_hex_id(self):
        self.assertTrue(TestLexer.checkLexeme("\x42\x50", "BP,<EOF>", 108))

    def test_negative_int(self):
        self.assertTrue(TestLexer.checkLexeme("-42", "-,42,<EOF>", 109))

    def test_only_under(self):
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 190))

# -----------------------------------------------------------------------------------
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(
            "123a123", "123,a123,<EOF>", 110))

    def test_int_id(self):
        self.assertTrue(TestLexer.checkLexeme(
            "123_12a", "123,_12a,<EOF>", 111))

    def test_float_fix(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("12.3", "12.3,<EOF>", 112))

    def test_float_floating(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1.55e5", "1.55e5,<EOF>", 113))

    def test_1_side_decimal(self):
        self.assertTrue(TestLexer.checkLexeme("2.e7", "2.e7,<EOF>", 114))

    def test_float_int(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1.-5", "1.,-,5,<EOF>", 115))

    def test_after_decimal(self):
        """Test float with fraction part"""
        self.assertTrue(TestLexer.checkLexeme(".5e10", ".5e10,<EOF>", 116))

    def test_floating_simple(self):
        self.assertTrue(TestLexer.checkLexeme("12e5", "12e5,<EOF>", 117))

    def test_wrong_float(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1.55e34e45", "1.55e34,e45,<EOF>", 118))

    def test_negative_float(self):
        self.assertTrue(TestLexer.checkLexeme(
            "-45.6e45", "-,45.6e45,<EOF>", 119))

    def test_wrong_expo(self):
        self.assertTrue(TestLexer.checkLexeme(
            "45.1e45.1", "45.1e45,.1,<EOF>", 120))

    def test_cap_floating(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1.55E5", "1.55E5,<EOF>", 181))

    def test_1side_decimal_cap(self):
        self.assertTrue(TestLexer.checkLexeme("2.E7", "2.E7,<EOF>", 182))

    def test_after_decimal_cap(self):
        """Test float with fraction part"""
        self.assertTrue(TestLexer.checkLexeme(".5E10", ".5E10,<EOF>", 183))

    def test_floating_simple_cap(self):
        self.assertTrue(TestLexer.checkLexeme("12E5", "12E5,<EOF>", 184))

    def test_wrong_float_cap(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1.55E34E45", "1.55E34,E45,<EOF>", 185))

    def test_negative_float_cap(self):
        self.assertTrue(TestLexer.checkLexeme(
            "-45.6E45", "-,45.6E45,<EOF>", 186))

    def test_wrong_expo_cap(self):
        self.assertTrue(TestLexer.checkLexeme(
            "45.1E45.1", "45.1E45,.1,<EOF>", 187))

    def test_e_id(self):
        self.assertTrue(TestLexer.checkLexeme("e-", "e,-,<EOF>", 188))

    def test_E_id(self):
        self.assertTrue(TestLexer.checkLexeme("E - _", "E,-,_,<EOF>", 189))

# ------------------------------------------------------------------------------------
    """ TEST MISCELLANEOUS """

    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme("// Test comment", "<EOF>", 121))

    def test_block(self):
        block = """
        /* This is 
    block of 
    comment
    */"""
        self.assertTrue(TestLexer.checkLexeme(block, "<EOF>", 122))

    def test_block_id(self):
        block = """/* Block of 
        comment with id */
        array"""
        self.assertTrue(TestLexer.checkLexeme(block, "array,<EOF>", 123))

    def test_comment_unicode(self):
        self.assertTrue(TestLexer.checkLexeme(
            "// Comment: \u002B", "<EOF>", 124))

    def test_comment_hex(self):
        self.assertTrue(TestLexer.checkLexeme(
            "// Comment: \x2B", "<EOF>", 125))

    def test_unclosed(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\" Unclosed String", "Unclosed String: \" Unclosed String", 126))

    def test_string(self):
        quote = """"This is a string" """
        self.assertTrue(TestLexer.checkLexeme(
            quote, """"This is a string",<EOF>""", 127))

    def test_tab(self):
        quote = """"Tab: \t1" """
        self.assertTrue(TestLexer.checkLexeme(
            quote, """"Tab: \t1",<EOF>""", 128))

    def test_back(self):
        quote = """"Carriage sym:\b bol" """
        self.assertTrue(TestLexer.checkLexeme(
            quote, """"Carriage sym:\b bol",<EOF>""", 129))

    def test_formfeed(self):
        self.assertTrue(TestLexer.checkLexeme(
            """"Formfeed: \f this is" """, """"Formfeed: \f this is",<EOF>""", 130))

    def test_carriage(self):
        self.assertTrue(TestLexer.checkLexeme(
            """"Carriage:\rsym" """, """Unclosed String: "Carriage:""", 171))

    def test_backslash(self):
        self.assertTrue(TestLexer.checkLexeme(
            """"Backslash: \\ slash" """, """"Backslash: \\ slash",<EOF>""", 172))

    def test_newline(self):
        expect = """Unclosed String: "Newline: """
        self.assertTrue(TestLexer.checkLexeme(
            """"Newline: \n end lines" """, expect, 173))

    def test_carriage_line(self):
        self.assertTrue(TestLexer.checkLexeme(
            """"New carriage: \r\n here" """, """Unclosed String: "New carriage: """, 174))

    def test_esc_0(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "This \0 is \0" """, """"This \0 is \0",<EOF>""", 175))

    # TODO: Illegal Escape fix 176 178 179 200
    def test_illegal_esc(self):
        self.assertTrue(TestLexer.checkLexeme("""" abc \d " """, "", 176))

    def test_esc_forward(self):
        self.assertTrue(TestLexer.checkLexeme(""""Forward \/" """, "", 178))

    def test_esc_bracket(self):
        self.assertTrue(TestLexer.checkLexeme(
            """"Bracket this: \(" """, "", 179))

    def test_illegal_confuse(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\abc" """, "", 200))

    def test_esc_mix(self):
        self.assertTrue(TestLexer.checkLexeme(
            """var,foo(" \rstring") """, """var,,,foo,(,Unclosed String: " """, 180))

    def test_1_doublequote(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ \" """, """Unclosed String: " """, 177))

# ----------------------------------------------------------------------------------------------
    """ TEST KEYWORDS """

    def test_return(self):
        self.assertTrue(TestLexer.checkLexeme(
            "return 4;", "return,4,;,<EOF>", 131))

    def test_continue(self):
        self.assertTrue(TestLexer.checkLexeme(
            "continue;", "continue,;,<EOF>", 132))

    def test_break(self):
        self.assertTrue(TestLexer.checkLexeme(
            "break;", "break,;,<EOF>", 133))

    def test_do_while(self):
        self.assertTrue(TestLexer.checkLexeme("do {} while ()",
                                              "do,{,},while,(,),<EOF>", 134))

    def test_if(self):
        self.assertTrue(TestLexer.checkLexeme(
            "if ()", "if,(,),<EOF>", 135))

    def test_if_else(self):
        self.assertTrue(TestLexer.checkLexeme("if () else {}",
                                              "if,(,),else,{,},<EOF>", 136))

    def test_for_inf(self):
        self.assertTrue(TestLexer.checkLexeme(
            "for(;;)", "for,(,;,;,),<EOF>", 137))

    def test_for(self):
        self.assertTrue(TestLexer.checkLexeme("for(a = 0; a < n; a=a+2)",
                                              "for,(,a,=,0,;,a,<,n,;,a,=,a,+,2,),<EOF>", 138))

    def test_true(self):
        self.assertTrue(TestLexer.checkLexeme(
            "visited = true", "visited,=,true,<EOF>", 139))

    def test_false(self):
        self.assertTrue(TestLexer.checkLexeme(
            "visited = false", "visited,=,false,<EOF>", 140))

# -------------------------------------------------------------------------------------------------------------------------
    """ TEST EXPRESSIONS """

    def test_add(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a + b", "a,+,b,<EOF>", 141))

    def test_minus(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a- b", "a,-,b,<EOF>", 142))

    def test_multi(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a *b", "a,*,b,<EOF>", 143))

    def test_div(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a/b", "a,/,b,<EOF>", 144))

    def test_mod(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a % b", "a,%,b,<EOF>", 145))

    def test_and(self):
        self.assertTrue(TestLexer.checkLexeme("true && a == 2",
                                              "true,&&,a,==,2,<EOF>", 146))

    def test_or(self):
        self.assertTrue(TestLexer.checkLexeme("false || a != 2",
                                              "false,||,a,!=,2,<EOF>", 147))

    def test_lt(self):
        """ Test less than """
        self.assertTrue(TestLexer.checkLexeme(
            "a < b", "a,<,b,<EOF>", 148))

    def test_leq(self):
        """ Test less equal than """
        self.assertTrue(TestLexer.checkLexeme(
            "a <= b", "a,<=,b,<EOF>", 149))

    def test_gt(self):
        self.assertTrue(TestLexer.checkLexeme("a > b", "a,>,b,<EOF>", 150))

    def test_geq(self):
        self.assertTrue(TestLexer.checkLexeme("a >= b", "a,>=,b,<EOF>", 151))

    def test_lt_int(self):
        self.assertTrue(TestLexer.checkLexeme("a >2", "a,>,2,<EOF>", 152))

    def test_gt_float(self):
        self.assertTrue(TestLexer.checkLexeme("a< 2.3", "a,<,2.3,<EOF>", 153))

    def test_assign(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a = b= 26", "a,=,b,=,26,<EOF>", 154))

    def test_int_decl(self):
        self.assertTrue(TestLexer.checkLexeme("int a;", "int,a,;,<EOF>", 155))

    def test_int_multi(self):
        self.assertTrue(TestLexer.checkLexeme(
            "int a1, a2;", "int,a1,,,a2,;,<EOF>", 156))

    def test_int_array(self):
        self.assertTrue(TestLexer.checkLexeme(
            "int arr[2];", "int,arr,[,2,],;,<EOF>", 157))

    def test_arrayINT_multi(self):
        self.assertTrue(TestLexer.checkLexeme(
            "int a1, array[10];", "int,a1,,,array,[,10,],;,<EOF>", 158))

    def test_float_decl(self):
        self.assertTrue(TestLexer.checkLexeme(
            "float flt;", "float,flt,;,<EOF>", 159))

    def test_float_multi(self):
        self.assertTrue(TestLexer.checkLexeme(
            "float a1, a2;", "float,a1,,,a2,;,<EOF>", 160))

    def test_float_array(self):
        self.assertTrue(TestLexer.checkLexeme(
            "float sub[2];", "float,sub,[,2,],;,<EOF>", 161))

    def test_arrayFLT_multi(self):
        self.assertTrue(TestLexer.checkLexeme(
            "float a, sequence[i];", "float,a,,,sequence,[,i,],;,<EOF>", 162))

    def test_bool_decl(self):
        self.assertTrue(TestLexer.checkLexeme(
            "boolean visit;", "boolean,visit,;,<EOF>", 163))

    def test_bool_multi(self):
        self.assertTrue(TestLexer.checkLexeme(
            "boolean a1, a2;", "boolean,a1,,,a2,;,<EOF>", 164))

    def test_bool_array(self):
        self.assertTrue(TestLexer.checkLexeme(
            "boolean trace[2];", "boolean,trace,[,2,],;,<EOF>", 165))

    def test_arrayBOOL_multi(self):
        self.assertTrue(TestLexer.checkLexeme(
            "boolean a, sequence[i];", "boolean,a,,,sequence,[,i,],;,<EOF>", 166))

    def test_str_decl(self):
        self.assertTrue(TestLexer.checkLexeme(
            "string chr;", "string,chr,;,<EOF>", 167))

    def test_str_multi(self):
        self.assertTrue(TestLexer.checkLexeme(
            "string chr, ord;", "string,chr,,,ord,;,<EOF>", 168))

    def test_str_array(self):
        self.assertTrue(TestLexer.checkLexeme(
            "string lst[10];", "string,lst,[,10,],;,<EOF>", 169))

    def test_arraySTR_multi(self):
        self.assertTrue(TestLexer.checkLexeme(
            "string a, sequence[100];", "string,a,,,sequence,[,100,],;,<EOF>", 170))

    def test_bit_and(self):
        self.assertTrue(TestLexer.checkLexeme("1 & 2", "1,Error Token &", 191))

    def test_bit_or(self):
        self.assertTrue(TestLexer.checkLexeme("5 | 0", "5,Error Token |", 192))

    def test_bit_xor(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12 ^ 13", "12,Error Token ^", 193))

    def test_not(self):
        self.assertTrue(TestLexer.checkLexeme("!false", "!,false,<EOF>", 194))

    def test_not_true(self):
        self.assertTrue(TestLexer.checkLexeme(
            "!true==false", "!,true,==,false,<EOF>", 195))

    def test_bitwise_mix(self):
        self.assertTrue(TestLexer.checkLexeme(
            """s("\t string")|d+2""", """s,(,"\t string",),Error Token |""", 196))

    def test_short_if(self):
        self.assertTrue(TestLexer.checkLexeme("""a+b==c?print(a):print(b)""", """a,+,b,==,c,Error Token ?""", 197))

    def test_private_var(self):
        self.assertTrue(TestLexer.checkLexeme("""__init__+_gt_""", """__init__,+,_gt_,<EOF>""", 198))

    def test_another_case200(self):
        self.assertTrue(TestLexer.checkLexeme("""abc\abc""","""abc,Error Token \a""", 199))