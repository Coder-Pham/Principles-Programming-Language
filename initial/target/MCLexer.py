# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0183\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u009c\n")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\7\37\u00e4\n\37\f\37\16\37\u00e7")
        buf.write("\13\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \7 \u00f2\n")
        buf.write(" \f \16 \u00f5\13 \3 \3 \3!\3!\3\"\3\"\3#\3#\3#\7#\u0100")
        buf.write("\n#\f#\16#\u0103\13#\3$\6$\u0106\n$\r$\16$\u0107\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\6*\u0115\n*\r*\16*\u0116")
        buf.write("\3*\3*\3+\3+\3,\3,\3-\3-\3.\6.\u0122\n.\r.\16.\u0123\3")
        buf.write(".\5.\u0127\n.\3.\7.\u012a\n.\f.\16.\u012d\13.\3.\7.\u0130")
        buf.write("\n.\f.\16.\u0133\13.\3.\5.\u0136\n.\3.\6.\u0139\n.\r.")
        buf.write("\16.\u013a\5.\u013d\n.\3.\3.\5.\u0141\n.\3.\6.\u0144\n")
        buf.write(".\r.\16.\u0145\5.\u0148\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/")
        buf.write("\3/\3/\3/\3/\3/\3/\3/\5/\u015a\n/\3\60\3\60\3\60\3\60")
        buf.write("\7\60\u0160\n\60\f\60\16\60\u0163\13\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\5\62\u016e\n\62\3\62\7")
        buf.write("\62\u0171\n\62\f\62\16\62\u0174\13\62\3\62\3\62\3\63\3")
        buf.write("\63\7\63\u017a\n\63\f\63\16\63\u017d\13\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\u00e5\2\64\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\2C\2E\"G#I$K%M&O\'Q(S)U*W+Y,[-]\2_.a/c\60e\61")
        buf.write("\3\2\16\4\2\f\f\17\17\5\2C\\aac|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^ddhhppt")
        buf.write("tvv\3\2$$\6\2\n\f\16\17$$^^\3\2^^\b\2$$))^^ddhhvv\2\u019e")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2")
        buf.write("\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write("\2\2Y\3\2\2\2\2[\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2")
        buf.write("\2\2\2e\3\2\2\2\3g\3\2\2\2\5m\3\2\2\2\7v\3\2\2\2\ty\3")
        buf.write("\2\2\2\13\177\3\2\2\2\r\u0082\3\2\2\2\17\u0087\3\2\2\2")
        buf.write("\21\u008b\3\2\2\2\23\u009b\3\2\2\2\25\u009d\3\2\2\2\27")
        buf.write("\u009f\3\2\2\2\31\u00a1\3\2\2\2\33\u00a3\3\2\2\2\35\u00a5")
        buf.write("\3\2\2\2\37\u00a7\3\2\2\2!\u00aa\3\2\2\2#\u00ac\3\2\2")
        buf.write("\2%\u00af\3\2\2\2\'\u00b2\3\2\2\2)\u00b5\3\2\2\2+\u00b7")
        buf.write("\3\2\2\2-\u00ba\3\2\2\2/\u00bc\3\2\2\2\61\u00bf\3\2\2")
        buf.write("\2\63\u00c1\3\2\2\2\65\u00c9\3\2\2\2\67\u00cd\3\2\2\2")
        buf.write("9\u00d2\3\2\2\2;\u00d8\3\2\2\2=\u00df\3\2\2\2?\u00ed\3")
        buf.write("\2\2\2A\u00f8\3\2\2\2C\u00fa\3\2\2\2E\u00fc\3\2\2\2G\u0105")
        buf.write("\3\2\2\2I\u0109\3\2\2\2K\u010b\3\2\2\2M\u010d\3\2\2\2")
        buf.write("O\u010f\3\2\2\2Q\u0111\3\2\2\2S\u0114\3\2\2\2U\u011a\3")
        buf.write("\2\2\2W\u011c\3\2\2\2Y\u011e\3\2\2\2[\u013c\3\2\2\2]\u0159")
        buf.write("\3\2\2\2_\u015b\3\2\2\2a\u0167\3\2\2\2c\u0169\3\2\2\2")
        buf.write("e\u0177\3\2\2\2gh\7d\2\2hi\7t\2\2ij\7g\2\2jk\7c\2\2kl")
        buf.write("\7m\2\2l\4\3\2\2\2mn\7e\2\2no\7q\2\2op\7p\2\2pq\7v\2\2")
        buf.write("qr\7k\2\2rs\7p\2\2st\7w\2\2tu\7g\2\2u\6\3\2\2\2vw\7f\2")
        buf.write("\2wx\7q\2\2x\b\3\2\2\2yz\7y\2\2z{\7j\2\2{|\7k\2\2|}\7")
        buf.write("n\2\2}~\7g\2\2~\n\3\2\2\2\177\u0080\7k\2\2\u0080\u0081")
        buf.write("\7h\2\2\u0081\f\3\2\2\2\u0082\u0083\7g\2\2\u0083\u0084")
        buf.write("\7n\2\2\u0084\u0085\7u\2\2\u0085\u0086\7g\2\2\u0086\16")
        buf.write("\3\2\2\2\u0087\u0088\7h\2\2\u0088\u0089\7q\2\2\u0089\u008a")
        buf.write("\7t\2\2\u008a\20\3\2\2\2\u008b\u008c\7t\2\2\u008c\u008d")
        buf.write("\7g\2\2\u008d\u008e\7v\2\2\u008e\u008f\7w\2\2\u008f\u0090")
        buf.write("\7t\2\2\u0090\u0091\7p\2\2\u0091\22\3\2\2\2\u0092\u0093")
        buf.write("\7v\2\2\u0093\u0094\7t\2\2\u0094\u0095\7w\2\2\u0095\u009c")
        buf.write("\7g\2\2\u0096\u0097\7h\2\2\u0097\u0098\7c\2\2\u0098\u0099")
        buf.write("\7n\2\2\u0099\u009a\7u\2\2\u009a\u009c\7g\2\2\u009b\u0092")
        buf.write("\3\2\2\2\u009b\u0096\3\2\2\2\u009c\24\3\2\2\2\u009d\u009e")
        buf.write("\7-\2\2\u009e\26\3\2\2\2\u009f\u00a0\7/\2\2\u00a0\30\3")
        buf.write("\2\2\2\u00a1\u00a2\7\61\2\2\u00a2\32\3\2\2\2\u00a3\u00a4")
        buf.write("\7,\2\2\u00a4\34\3\2\2\2\u00a5\u00a6\7\'\2\2\u00a6\36")
        buf.write("\3\2\2\2\u00a7\u00a8\7(\2\2\u00a8\u00a9\7(\2\2\u00a9 ")
        buf.write("\3\2\2\2\u00aa\u00ab\7#\2\2\u00ab\"\3\2\2\2\u00ac\u00ad")
        buf.write("\7~\2\2\u00ad\u00ae\7~\2\2\u00ae$\3\2\2\2\u00af\u00b0")
        buf.write("\7?\2\2\u00b0\u00b1\7?\2\2\u00b1&\3\2\2\2\u00b2\u00b3")
        buf.write("\7#\2\2\u00b3\u00b4\7?\2\2\u00b4(\3\2\2\2\u00b5\u00b6")
        buf.write("\7>\2\2\u00b6*\3\2\2\2\u00b7\u00b8\7>\2\2\u00b8\u00b9")
        buf.write("\7?\2\2\u00b9,\3\2\2\2\u00ba\u00bb\7@\2\2\u00bb.\3\2\2")
        buf.write("\2\u00bc\u00bd\7@\2\2\u00bd\u00be\7?\2\2\u00be\60\3\2")
        buf.write("\2\2\u00bf\u00c0\7?\2\2\u00c0\62\3\2\2\2\u00c1\u00c2\7")
        buf.write("d\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7n\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\64\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\u00cc\7v\2\2\u00cc\66\3\2\2\2\u00cd\u00ce")
        buf.write("\7x\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7f\2\2\u00d18\3\2\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4")
        buf.write("\7n\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7")
        buf.write("\7v\2\2\u00d7:\3\2\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\u00de\7i\2\2\u00de<\3\2\2\2\u00df\u00e0")
        buf.write("\7\61\2\2\u00e0\u00e1\7,\2\2\u00e1\u00e5\3\2\2\2\u00e2")
        buf.write("\u00e4\13\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e7\3\2\2")
        buf.write("\2\u00e5\u00e6\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e8")
        buf.write("\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9\7,\2\2\u00e9")
        buf.write("\u00ea\7\61\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\b\37\2")
        buf.write("\2\u00ec>\3\2\2\2\u00ed\u00ee\7\61\2\2\u00ee\u00ef\7\61")
        buf.write("\2\2\u00ef\u00f3\3\2\2\2\u00f0\u00f2\n\2\2\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f4\3\2\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f6\u00f7\b \2\2\u00f7@\3\2\2\2\u00f8\u00f9\t\3\2\2")
        buf.write("\u00f9B\3\2\2\2\u00fa\u00fb\t\4\2\2\u00fbD\3\2\2\2\u00fc")
        buf.write("\u0101\5A!\2\u00fd\u0100\5A!\2\u00fe\u0100\5C\"\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100\u0103\3\2\2\2")
        buf.write("\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102F\3\2\2")
        buf.write("\2\u0103\u0101\3\2\2\2\u0104\u0106\5C\"\2\u0105\u0104")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0105\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108H\3\2\2\2\u0109\u010a\7*\2\2\u010a")
        buf.write("J\3\2\2\2\u010b\u010c\7+\2\2\u010cL\3\2\2\2\u010d\u010e")
        buf.write("\7}\2\2\u010eN\3\2\2\2\u010f\u0110\7\177\2\2\u0110P\3")
        buf.write("\2\2\2\u0111\u0112\7=\2\2\u0112R\3\2\2\2\u0113\u0115\t")
        buf.write("\5\2\2\u0114\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0114")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("\u0119\b*\2\2\u0119T\3\2\2\2\u011a\u011b\7.\2\2\u011b")
        buf.write("V\3\2\2\2\u011c\u011d\7]\2\2\u011dX\3\2\2\2\u011e\u011f")
        buf.write("\7_\2\2\u011fZ\3\2\2\2\u0120\u0122\5C\"\2\u0121\u0120")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0121\3\2\2\2\u0123")
        buf.write("\u0124\3\2\2\2\u0124\u0126\3\2\2\2\u0125\u0127\7\60\2")
        buf.write("\2\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u012b")
        buf.write("\3\2\2\2\u0128\u012a\5C\"\2\u0129\u0128\3\2\2\2\u012a")
        buf.write("\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012c\u013d\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u0130\5")
        buf.write("C\"\2\u012f\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0135\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0134\u0136\7\60\2\2\u0135\u0134\3\2\2")
        buf.write("\2\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0139")
        buf.write("\5C\"\2\u0138\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d\3\2\2\2")
        buf.write("\u013c\u0121\3\2\2\2\u013c\u0131\3\2\2\2\u013d\u0147\3")
        buf.write("\2\2\2\u013e\u0140\t\6\2\2\u013f\u0141\t\7\2\2\u0140\u013f")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0143\3\2\2\2\u0142")
        buf.write("\u0144\5C\"\2\u0143\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148\3")
        buf.write("\2\2\2\u0147\u013e\3\2\2\2\u0147\u0148\3\2\2\2\u0148\\")
        buf.write("\3\2\2\2\u0149\u015a\3\2\2\2\u014a\u014b\7^\2\2\u014b")
        buf.write("\u015a\7$\2\2\u014c\u014d\7^\2\2\u014d\u015a\7^\2\2\u014e")
        buf.write("\u014f\7^\2\2\u014f\u015a\7d\2\2\u0150\u0151\7^\2\2\u0151")
        buf.write("\u015a\7h\2\2\u0152\u0153\7^\2\2\u0153\u015a\7p\2\2\u0154")
        buf.write("\u0155\7^\2\2\u0155\u015a\7t\2\2\u0156\u0157\7^\2\2\u0157")
        buf.write("\u015a\7v\2\2\u0158\u015a\7)\2\2\u0159\u0149\3\2\2\2\u0159")
        buf.write("\u014a\3\2\2\2\u0159\u014c\3\2\2\2\u0159\u014e\3\2\2\2")
        buf.write("\u0159\u0150\3\2\2\2\u0159\u0152\3\2\2\2\u0159\u0154\3")
        buf.write("\2\2\2\u0159\u0156\3\2\2\2\u0159\u0158\3\2\2\2\u015a^")
        buf.write("\3\2\2\2\u015b\u0161\7$\2\2\u015c\u0160\n\b\2\2\u015d")
        buf.write("\u015e\7^\2\2\u015e\u0160\t\t\2\2\u015f\u015c\3\2\2\2")
        buf.write("\u015f\u015d\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3")
        buf.write("\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0161")
        buf.write("\3\2\2\2\u0164\u0165\7$\2\2\u0165\u0166\b\60\3\2\u0166")
        buf.write("`\3\2\2\2\u0167\u0168\n\n\2\2\u0168b\3\2\2\2\u0169\u0172")
        buf.write("\7$\2\2\u016a\u016b\7^\2\2\u016b\u016e\t\t\2\2\u016c\u016e")
        buf.write("\n\13\2\2\u016d\u016a\3\2\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u0171\7\f\2\2\u0170\u016d\3\2\2\2")
        buf.write("\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3")
        buf.write("\2\2\2\u0172\u0173\3\2\2\2\u0173\u0175\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0175\u0176\b\62\4\2\u0176d\3\2\2\2\u0177\u017b")
        buf.write("\7$\2\2\u0178\u017a\n\f\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u017e\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\7")
        buf.write("^\2\2\u017f\u0180\n\r\2\2\u0180\u0181\3\2\2\2\u0181\u0182")
        buf.write("\b\63\5\2\u0182f\3\2\2\2\33\2\u009b\u00e5\u00f3\u00ff")
        buf.write("\u0101\u0107\u0116\u0123\u0126\u012b\u0131\u0135\u013a")
        buf.write("\u013c\u0140\u0145\u0147\u0159\u015f\u0161\u016d\u0170")
        buf.write("\u0172\u017b\6\b\2\2\3\60\2\3\62\3\3\63\4")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Break = 1
    Continue = 2
    Do = 3
    While = 4
    If = 5
    Else = 6
    For = 7
    Return = 8
    BooleanLIT = 9
    ADD = 10
    SUB = 11
    DIV = 12
    MUL = 13
    MOD = 14
    AND = 15
    NOT = 16
    OR = 17
    EQ = 18
    NOTEQ = 19
    LT = 20
    LEQ = 21
    GT = 22
    GEQ = 23
    ASSIGN = 24
    BOOLTYPE = 25
    INTTYPE = 26
    VOIDTYPE = 27
    FLOATTYPE = 28
    STRINGTYPE = 29
    BLOCK_COMMENT = 30
    LINE_COMMENT = 31
    ID = 32
    IntLIT = 33
    LB = 34
    RB = 35
    LP = 36
    RP = 37
    SEMI = 38
    WS = 39
    COMMA = 40
    LS = 41
    RS = 42
    FloatLIT = 43
    StringLIT = 44
    ERROR_CHAR = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'do'", "'while'", "'if'", "'else'", 
            "'for'", "'return'", "'+'", "'-'", "'/'", "'*'", "'%'", "'&&'", 
            "'!'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'='", "'boolean'", "'int'", "'void'", "'float'", "'string'", 
            "'('", "')'", "'{'", "'}'", "';'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "Break", "Continue", "Do", "While", "If", "Else", "For", "Return", 
            "BooleanLIT", "ADD", "SUB", "DIV", "MUL", "MOD", "AND", "NOT", 
            "OR", "EQ", "NOTEQ", "LT", "LEQ", "GT", "GEQ", "ASSIGN", "BOOLTYPE", 
            "INTTYPE", "VOIDTYPE", "FLOATTYPE", "STRINGTYPE", "BLOCK_COMMENT", 
            "LINE_COMMENT", "ID", "IntLIT", "LB", "RB", "LP", "RP", "SEMI", 
            "WS", "COMMA", "LS", "RS", "FloatLIT", "StringLIT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "Break", "Continue", "Do", "While", "If", "Else", "For", 
                  "Return", "BooleanLIT", "ADD", "SUB", "DIV", "MUL", "MOD", 
                  "AND", "NOT", "OR", "EQ", "NOTEQ", "LT", "LEQ", "GT", 
                  "GEQ", "ASSIGN", "BOOLTYPE", "INTTYPE", "VOIDTYPE", "FLOATTYPE", 
                  "STRINGTYPE", "BLOCK_COMMENT", "LINE_COMMENT", "LETTER", 
                  "DIGIT", "ID", "IntLIT", "LB", "RB", "LP", "RP", "SEMI", 
                  "WS", "COMMA", "LS", "RS", "FloatLIT", "Escapesequence", 
                  "StringLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.StringLIT_action 
            actions[48] = self.UNCLOSE_STRING_action 
            actions[49] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def StringLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
            		self.text = self.text[1:] 

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text[1:]

     


