# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0194\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00a6\n\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!")
        buf.write("\7!\u00ee\n!\f!\16!\u00f1\13!\3!\3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\7\"\u00fc\n\"\f\"\16\"\u00ff\13\"\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3%\3%\3%\7%\u010a\n%\f%\16%\u010d\13%\3&\6&\u0110")
        buf.write("\n&\r&\16&\u0111\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\6")
        buf.write(",\u011f\n,\r,\16,\u0120\3,\3,\3-\3-\3.\3.\3/\3/\3\60\6")
        buf.write("\60\u012c\n\60\r\60\16\60\u012d\3\60\5\60\u0131\n\60\3")
        buf.write("\60\7\60\u0134\n\60\f\60\16\60\u0137\13\60\3\60\7\60\u013a")
        buf.write("\n\60\f\60\16\60\u013d\13\60\3\60\5\60\u0140\n\60\3\60")
        buf.write("\6\60\u0143\n\60\r\60\16\60\u0144\5\60\u0147\n\60\3\60")
        buf.write("\3\60\5\60\u014b\n\60\3\60\6\60\u014e\n\60\r\60\16\60")
        buf.write("\u014f\5\60\u0152\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0163")
        buf.write("\n\61\3\62\3\62\3\62\3\62\7\62\u0169\n\62\f\62\16\62\u016c")
        buf.write("\13\62\3\62\3\62\3\63\3\63\3\63\3\63\5\63\u0174\n\63\3")
        buf.write("\64\3\64\3\64\3\64\5\64\u017a\n\64\3\65\3\65\3\65\3\65")
        buf.write("\5\65\u0180\n\65\3\65\7\65\u0183\n\65\f\65\16\65\u0186")
        buf.write("\13\65\3\66\3\66\3\66\3\66\7\66\u018c\n\66\f\66\16\66")
        buf.write("\u018f\13\66\3\66\3\66\3\66\3\66\3\u00ef\2\67\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E\2G\2I$K%M&O\'Q(S)U*")
        buf.write("W+Y,[-]._/a\2c\60e\61g\62i\63k\64\3\2\f\4\2\f\f\17\17")
        buf.write("\5\2C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\4\2GGgg\4\2--/")
        buf.write("/\5\2\n\13\16\16^^\5\2\f\f\17\17$$\n\2$$))^^ddhhppttv")
        buf.write("v\6\2\n\f\16\17$$^^\2\u01b4\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\3m\3\2\2\2\5s\3\2\2\2\7|\3\2\2\2")
        buf.write("\t\177\3\2\2\2\13\u0085\3\2\2\2\r\u0088\3\2\2\2\17\u008d")
        buf.write("\3\2\2\2\21\u0091\3\2\2\2\23\u0098\3\2\2\2\25\u009d\3")
        buf.write("\2\2\2\27\u00a5\3\2\2\2\31\u00a7\3\2\2\2\33\u00a9\3\2")
        buf.write("\2\2\35\u00ab\3\2\2\2\37\u00ad\3\2\2\2!\u00af\3\2\2\2")
        buf.write("#\u00b1\3\2\2\2%\u00b4\3\2\2\2\'\u00b6\3\2\2\2)\u00b9")
        buf.write("\3\2\2\2+\u00bc\3\2\2\2-\u00bf\3\2\2\2/\u00c1\3\2\2\2")
        buf.write("\61\u00c4\3\2\2\2\63\u00c6\3\2\2\2\65\u00c9\3\2\2\2\67")
        buf.write("\u00cb\3\2\2\29\u00d3\3\2\2\2;\u00d7\3\2\2\2=\u00dc\3")
        buf.write("\2\2\2?\u00e2\3\2\2\2A\u00e9\3\2\2\2C\u00f7\3\2\2\2E\u0102")
        buf.write("\3\2\2\2G\u0104\3\2\2\2I\u0106\3\2\2\2K\u010f\3\2\2\2")
        buf.write("M\u0113\3\2\2\2O\u0115\3\2\2\2Q\u0117\3\2\2\2S\u0119\3")
        buf.write("\2\2\2U\u011b\3\2\2\2W\u011e\3\2\2\2Y\u0124\3\2\2\2[\u0126")
        buf.write("\3\2\2\2]\u0128\3\2\2\2_\u0146\3\2\2\2a\u0162\3\2\2\2")
        buf.write("c\u0164\3\2\2\2e\u0173\3\2\2\2g\u0179\3\2\2\2i\u017b\3")
        buf.write("\2\2\2k\u0187\3\2\2\2mn\7d\2\2no\7t\2\2op\7g\2\2pq\7c")
        buf.write("\2\2qr\7m\2\2r\4\3\2\2\2st\7e\2\2tu\7q\2\2uv\7p\2\2vw")
        buf.write("\7v\2\2wx\7k\2\2xy\7p\2\2yz\7w\2\2z{\7g\2\2{\6\3\2\2\2")
        buf.write("|}\7f\2\2}~\7q\2\2~\b\3\2\2\2\177\u0080\7y\2\2\u0080\u0081")
        buf.write("\7j\2\2\u0081\u0082\7k\2\2\u0082\u0083\7n\2\2\u0083\u0084")
        buf.write("\7g\2\2\u0084\n\3\2\2\2\u0085\u0086\7k\2\2\u0086\u0087")
        buf.write("\7h\2\2\u0087\f\3\2\2\2\u0088\u0089\7g\2\2\u0089\u008a")
        buf.write("\7n\2\2\u008a\u008b\7u\2\2\u008b\u008c\7g\2\2\u008c\16")
        buf.write("\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f\7q\2\2\u008f\u0090")
        buf.write("\7t\2\2\u0090\20\3\2\2\2\u0091\u0092\7t\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\u0094\7v\2\2\u0094\u0095\7w\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7p\2\2\u0097\22\3\2\2\2\u0098\u0099")
        buf.write("\7v\2\2\u0099\u009a\7t\2\2\u009a\u009b\7w\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\24\3\2\2\2\u009d\u009e\7h\2\2\u009e\u009f")
        buf.write("\7c\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1\7u\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\26\3\2\2\2\u00a3\u00a6\5\25\13\2\u00a4\u00a6")
        buf.write("\5\23\n\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6")
        buf.write("\30\3\2\2\2\u00a7\u00a8\7-\2\2\u00a8\32\3\2\2\2\u00a9")
        buf.write("\u00aa\7/\2\2\u00aa\34\3\2\2\2\u00ab\u00ac\7\61\2\2\u00ac")
        buf.write("\36\3\2\2\2\u00ad\u00ae\7,\2\2\u00ae \3\2\2\2\u00af\u00b0")
        buf.write("\7\'\2\2\u00b0\"\3\2\2\2\u00b1\u00b2\7(\2\2\u00b2\u00b3")
        buf.write("\7(\2\2\u00b3$\3\2\2\2\u00b4\u00b5\7#\2\2\u00b5&\3\2\2")
        buf.write("\2\u00b6\u00b7\7~\2\2\u00b7\u00b8\7~\2\2\u00b8(\3\2\2")
        buf.write("\2\u00b9\u00ba\7?\2\2\u00ba\u00bb\7?\2\2\u00bb*\3\2\2")
        buf.write("\2\u00bc\u00bd\7#\2\2\u00bd\u00be\7?\2\2\u00be,\3\2\2")
        buf.write("\2\u00bf\u00c0\7>\2\2\u00c0.\3\2\2\2\u00c1\u00c2\7>\2")
        buf.write("\2\u00c2\u00c3\7?\2\2\u00c3\60\3\2\2\2\u00c4\u00c5\7@")
        buf.write("\2\2\u00c5\62\3\2\2\2\u00c6\u00c7\7@\2\2\u00c7\u00c8\7")
        buf.write("?\2\2\u00c8\64\3\2\2\2\u00c9\u00ca\7?\2\2\u00ca\66\3\2")
        buf.write("\2\2\u00cb\u00cc\7d\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7q\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1")
        buf.write("\7c\2\2\u00d1\u00d2\7p\2\2\u00d28\3\2\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7v\2\2\u00d6:\3")
        buf.write("\2\2\2\u00d7\u00d8\7x\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7f\2\2\u00db<\3\2\2\2\u00dc\u00dd")
        buf.write("\7h\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7v\2\2\u00e1>\3\2\2\2\u00e2\u00e3")
        buf.write("\7u\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7i\2\2\u00e8@\3")
        buf.write("\2\2\2\u00e9\u00ea\7\61\2\2\u00ea\u00eb\7,\2\2\u00eb\u00ef")
        buf.write("\3\2\2\2\u00ec\u00ee\13\2\2\2\u00ed\u00ec\3\2\2\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7")
        buf.write(",\2\2\u00f3\u00f4\7\61\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6")
        buf.write("\b!\2\2\u00f6B\3\2\2\2\u00f7\u00f8\7\61\2\2\u00f8\u00f9")
        buf.write("\7\61\2\2\u00f9\u00fd\3\2\2\2\u00fa\u00fc\n\2\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fd\u00fe\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff\u00fd\3")
        buf.write("\2\2\2\u0100\u0101\b\"\2\2\u0101D\3\2\2\2\u0102\u0103")
        buf.write("\t\3\2\2\u0103F\3\2\2\2\u0104\u0105\t\4\2\2\u0105H\3\2")
        buf.write("\2\2\u0106\u010b\5E#\2\u0107\u010a\5E#\2\u0108\u010a\4")
        buf.write("\62;\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a\u010d")
        buf.write("\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c")
        buf.write("J\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u0110\5G$\2\u010f")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0111\u0112\3\2\2\2\u0112L\3\2\2\2\u0113\u0114\7*\2\2")
        buf.write("\u0114N\3\2\2\2\u0115\u0116\7+\2\2\u0116P\3\2\2\2\u0117")
        buf.write("\u0118\7}\2\2\u0118R\3\2\2\2\u0119\u011a\7\177\2\2\u011a")
        buf.write("T\3\2\2\2\u011b\u011c\7=\2\2\u011cV\3\2\2\2\u011d\u011f")
        buf.write("\t\5\2\2\u011e\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u0122\u0123\b,\2\2\u0123X\3\2\2\2\u0124\u0125\7.\2\2")
        buf.write("\u0125Z\3\2\2\2\u0126\u0127\7]\2\2\u0127\\\3\2\2\2\u0128")
        buf.write("\u0129\7_\2\2\u0129^\3\2\2\2\u012a\u012c\5G$\2\u012b\u012a")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u0131\7\60\2")
        buf.write("\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0135")
        buf.write("\3\2\2\2\u0132\u0134\5G$\2\u0133\u0132\3\2\2\2\u0134\u0137")
        buf.write("\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("\u0147\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u013a\5G$\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013e\u0140\7\60\2\2\u013f\u013e\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0142\3\2\2\2\u0141\u0143\5G$\2\u0142")
        buf.write("\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0142\3\2\2\2")
        buf.write("\u0144\u0145\3\2\2\2\u0145\u0147\3\2\2\2\u0146\u012b\3")
        buf.write("\2\2\2\u0146\u013b\3\2\2\2\u0147\u0151\3\2\2\2\u0148\u014a")
        buf.write("\t\6\2\2\u0149\u014b\t\7\2\2\u014a\u0149\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014e\5G$\2\u014d")
        buf.write("\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u0148\3")
        buf.write("\2\2\2\u0151\u0152\3\2\2\2\u0152`\3\2\2\2\u0153\u0163")
        buf.write("\3\2\2\2\u0154\u0155\7^\2\2\u0155\u0163\7$\2\2\u0156\u0157")
        buf.write("\7^\2\2\u0157\u0163\7^\2\2\u0158\u0159\7^\2\2\u0159\u0163")
        buf.write("\7d\2\2\u015a\u015b\7^\2\2\u015b\u0163\7h\2\2\u015c\u015d")
        buf.write("\7^\2\2\u015d\u0163\7p\2\2\u015e\u015f\7^\2\2\u015f\u0163")
        buf.write("\7t\2\2\u0160\u0161\7^\2\2\u0161\u0163\7v\2\2\u0162\u0153")
        buf.write("\3\2\2\2\u0162\u0154\3\2\2\2\u0162\u0156\3\2\2\2\u0162")
        buf.write("\u0158\3\2\2\2\u0162\u015a\3\2\2\2\u0162\u015c\3\2\2\2")
        buf.write("\u0162\u015e\3\2\2\2\u0162\u0160\3\2\2\2\u0163b\3\2\2")
        buf.write("\2\u0164\u016a\7$\2\2\u0165\u0169\t\b\2\2\u0166\u0169")
        buf.write("\n\t\2\2\u0167\u0169\7)\2\2\u0168\u0165\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2")
        buf.write("\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016d\3")
        buf.write("\2\2\2\u016c\u016a\3\2\2\2\u016d\u016e\7$\2\2\u016ed\3")
        buf.write("\2\2\2\u016f\u0174\5K&\2\u0170\u0174\5\27\f\2\u0171\u0174")
        buf.write("\5_\60\2\u0172\u0174\5c\62\2\u0173\u016f\3\2\2\2\u0173")
        buf.write("\u0170\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2")
        buf.write("\u0174f\3\2\2\2\u0175\u017a\13\2\2\2\u0176\u0177\5_\60")
        buf.write("\2\u0177\u0178\7\60\2\2\u0178\u017a\3\2\2\2\u0179\u0175")
        buf.write("\3\2\2\2\u0179\u0176\3\2\2\2\u017ah\3\2\2\2\u017b\u0184")
        buf.write("\7$\2\2\u017c\u017d\7^\2\2\u017d\u0180\t\n\2\2\u017e\u0180")
        buf.write("\n\13\2\2\u017f\u017c\3\2\2\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0183\3\2\2\2\u0181\u0183\7\f\2\2\u0182\u017f\3\2\2\2")
        buf.write("\u0182\u0181\3\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3")
        buf.write("\2\2\2\u0184\u0185\3\2\2\2\u0185j\3\2\2\2\u0186\u0184")
        buf.write("\3\2\2\2\u0187\u018d\7$\2\2\u0188\u0189\7^\2\2\u0189\u018c")
        buf.write("\t\n\2\2\u018a\u018c\n\13\2\2\u018b\u0188\3\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018e\u0190\3\2\2\2\u018f\u018d\3")
        buf.write("\2\2\2\u0190\u0191\7^\2\2\u0191\u0192\n\n\2\2\u0192\u0193")
        buf.write("\7$\2\2\u0193l\3\2\2\2\36\2\u00a5\u00ef\u00fd\u0109\u010b")
        buf.write("\u0111\u0120\u012d\u0130\u0135\u013b\u013f\u0144\u0146")
        buf.write("\u014a\u014f\u0151\u0162\u0168\u016a\u0173\u0179\u017f")
        buf.write("\u0182\u0184\u018b\u018d\3\b\2\2")
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
    TRUE = 9
    FALSE = 10
    BooleanLIT = 11
    ADD = 12
    SUB = 13
    DIV = 14
    MUL = 15
    MOD = 16
    AND = 17
    NOT = 18
    OR = 19
    EQ = 20
    NOTEQ = 21
    LT = 22
    LEQ = 23
    GT = 24
    GEQ = 25
    ASSIGN = 26
    BOOLTYPE = 27
    INTTYPE = 28
    VOIDTYPE = 29
    FLOATTYPE = 30
    STRINGTYPE = 31
    BLOCK_COMMENT = 32
    LINE_COMMENT = 33
    ID = 34
    IntLIT = 35
    LB = 36
    RB = 37
    LP = 38
    RP = 39
    SEMI = 40
    WS = 41
    COMMA = 42
    LS = 43
    RS = 44
    FloatLIT = 45
    StringLIT = 46
    LITs = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'do'", "'while'", "'if'", "'else'", 
            "'for'", "'return'", "'true'", "'false'", "'+'", "'-'", "'/'", 
            "'*'", "'%'", "'&&'", "'!'", "'||'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'='", "'boolean'", "'int'", "'void'", 
            "'float'", "'string'", "'('", "')'", "'{'", "'}'", "';'", "','", 
            "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "Break", "Continue", "Do", "While", "If", "Else", "For", "Return", 
            "TRUE", "FALSE", "BooleanLIT", "ADD", "SUB", "DIV", "MUL", "MOD", 
            "AND", "NOT", "OR", "EQ", "NOTEQ", "LT", "LEQ", "GT", "GEQ", 
            "ASSIGN", "BOOLTYPE", "INTTYPE", "VOIDTYPE", "FLOATTYPE", "STRINGTYPE", 
            "BLOCK_COMMENT", "LINE_COMMENT", "ID", "IntLIT", "LB", "RB", 
            "LP", "RP", "SEMI", "WS", "COMMA", "LS", "RS", "FloatLIT", "StringLIT", 
            "LITs", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "Break", "Continue", "Do", "While", "If", "Else", "For", 
                  "Return", "TRUE", "FALSE", "BooleanLIT", "ADD", "SUB", 
                  "DIV", "MUL", "MOD", "AND", "NOT", "OR", "EQ", "NOTEQ", 
                  "LT", "LEQ", "GT", "GEQ", "ASSIGN", "BOOLTYPE", "INTTYPE", 
                  "VOIDTYPE", "FLOATTYPE", "STRINGTYPE", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "LETTER", "DIGIT", "ID", "IntLIT", "LB", 
                  "RB", "LP", "RP", "SEMI", "WS", "COMMA", "LS", "RS", "FloatLIT", 
                  "Escapesequence", "StringLIT", "LITs", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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


