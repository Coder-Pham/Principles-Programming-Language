# Generated from d:\BK\HK191\PPL\Assignment1\Principles-Programming-Language\initial\src\main\mc\parser\MC.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u0161\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\7\2H\n\2\f\2")
        buf.write("\16\2K\13\2\3\2\3\2\3\3\3\3\5\3Q\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6b\n\6\3")
        buf.write("\7\3\7\3\7\7\7g\n\7\f\7\16\7j\13\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\5\13{\n\13")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u0081\n\f\3\r\3\r\3\r\7\r\u0086\n")
        buf.write("\r\f\r\16\r\u0089\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u009a")
        buf.write("\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\7\16\u00aa\n\16\f\16\16\16\u00ad")
        buf.write("\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b7")
        buf.write("\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u00c4\n\17\f\17\16\17\u00c7\13\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00d5\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\7\20\u00e2\n\20\f\20\16\20\u00e5\13\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\7\23")
        buf.write("\u00f1\n\23\f\23\16\23\u00f4\13\23\5\23\u00f6\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\5\25\u0105\n\25\3\26\7\26\u0108\n\26\f\26\16\26")
        buf.write("\u010b\13\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\5")
        buf.write("\31\u0115\n\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u0137\n\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\5\37\u0144\n\37\3 \6 \u0147")
        buf.write("\n \r \16 \u0148\3!\3!\7!\u014d\n!\f!\16!\u0150\13!\3")
        buf.write("\"\3\"\3\"\5\"\u0155\n\"\3\"\3\"\3\"\5\"\u015a\n\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\2\5\32\34\36$\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BD\2\t\3\2$%")
        buf.write("\3\2\30\33\3\2\26\27\4\2\17\17\24\24\3\2\20\22\3\2\16")
        buf.write("\17\4\2\35\36 !\2\u0172\2I\3\2\2\2\4P\3\2\2\2\6R\3\2\2")
        buf.write("\2\bW\3\2\2\2\na\3\2\2\2\fc\3\2\2\2\16k\3\2\2\2\20o\3")
        buf.write("\2\2\2\22t\3\2\2\2\24z\3\2\2\2\26|\3\2\2\2\30\u0082\3")
        buf.write("\2\2\2\32\u0099\3\2\2\2\34\u00b6\3\2\2\2\36\u00d4\3\2")
        buf.write("\2\2 \u00e6\3\2\2\2\"\u00eb\3\2\2\2$\u00f5\3\2\2\2&\u00f7")
        buf.write("\3\2\2\2(\u0104\3\2\2\2*\u0109\3\2\2\2,\u010c\3\2\2\2")
        buf.write(".\u010f\3\2\2\2\60\u0112\3\2\2\2\62\u0118\3\2\2\2\64\u011b")
        buf.write("\3\2\2\2\66\u0125\3\2\2\28\u0129\3\2\2\2:\u012f\3\2\2")
        buf.write("\2<\u0143\3\2\2\2>\u0146\3\2\2\2@\u014e\3\2\2\2B\u0154")
        buf.write("\3\2\2\2D\u015e\3\2\2\2FH\5\4\3\2GF\3\2\2\2HK\3\2\2\2")
        buf.write("IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LM\7\2\2\3M\3")
        buf.write("\3\2\2\2NQ\5B\"\2OQ\5\16\b\2PN\3\2\2\2PO\3\2\2\2Q\5\3")
        buf.write("\2\2\2RS\5D#\2ST\7-\2\2TU\7%\2\2UV\7.\2\2V\7\3\2\2\2W")
        buf.write("X\7$\2\2XY\7-\2\2YZ\t\2\2\2Z[\7.\2\2[\t\3\2\2\2\\]\7$")
        buf.write("\2\2]^\7-\2\2^_\7%\2\2_b\7.\2\2`b\7$\2\2a\\\3\2\2\2a`")
        buf.write("\3\2\2\2b\13\3\2\2\2ch\5\n\6\2de\7,\2\2eg\5\n\6\2fd\3")
        buf.write("\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2i\r\3\2\2\2jh\3\2")
        buf.write("\2\2kl\5D#\2lm\5\f\7\2mn\7*\2\2n\17\3\2\2\2op\5D#\2pq")
        buf.write("\7$\2\2qr\7-\2\2rs\7.\2\2s\21\3\2\2\2tu\5D#\2uv\7-\2\2")
        buf.write("vw\7.\2\2w\23\3\2\2\2x{\5\20\t\2y{\5\22\n\2zx\3\2\2\2")
        buf.write("zy\3\2\2\2{\25\3\2\2\2|}\5D#\2}\u0080\7$\2\2~\177\7-\2")
        buf.write("\2\177\u0081\7.\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2")
        buf.write("\u0081\27\3\2\2\2\u0082\u0087\5\26\f\2\u0083\u0084\7,")
        buf.write("\2\2\u0084\u0086\5\26\f\2\u0085\u0083\3\2\2\2\u0086\u0089")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\31\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008b\b\16\1\2\u008b")
        buf.write("\u008c\7&\2\2\u008c\u008d\5\32\16\2\u008d\u008e\7\'\2")
        buf.write("\2\u008e\u009a\3\2\2\2\u008f\u009a\5\34\17\2\u0090\u0091")
        buf.write("\5\34\17\2\u0091\u0092\t\3\2\2\u0092\u0093\5\34\17\2\u0093")
        buf.write("\u009a\3\2\2\2\u0094\u0095\5\36\20\2\u0095\u0096\t\4\2")
        buf.write("\2\u0096\u0097\5\36\20\2\u0097\u009a\3\2\2\2\u0098\u009a")
        buf.write("\5(\25\2\u0099\u008a\3\2\2\2\u0099\u008f\3\2\2\2\u0099")
        buf.write("\u0090\3\2\2\2\u0099\u0094\3\2\2\2\u0099\u0098\3\2\2\2")
        buf.write("\u009a\u00ab\3\2\2\2\u009b\u009c\f\6\2\2\u009c\u009d\7")
        buf.write("\23\2\2\u009d\u00aa\5\32\16\7\u009e\u009f\f\5\2\2\u009f")
        buf.write("\u00a0\7\25\2\2\u00a0\u00aa\5\32\16\6\u00a1\u00a2\f\4")
        buf.write("\2\2\u00a2\u00a3\7\34\2\2\u00a3\u00aa\5\32\16\4\u00a4")
        buf.write("\u00a5\f\n\2\2\u00a5\u00a6\7-\2\2\u00a6\u00a7\5\32\16")
        buf.write("\2\u00a7\u00a8\7.\2\2\u00a8\u00aa\3\2\2\2\u00a9\u009b")
        buf.write("\3\2\2\2\u00a9\u009e\3\2\2\2\u00a9\u00a1\3\2\2\2\u00a9")
        buf.write("\u00a4\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ab\u00ac\3\2\2\2\u00ac\33\3\2\2\2\u00ad\u00ab\3\2")
        buf.write("\2\2\u00ae\u00af\b\17\1\2\u00af\u00b0\7&\2\2\u00b0\u00b1")
        buf.write("\5\32\16\2\u00b1\u00b2\7\'\2\2\u00b2\u00b7\3\2\2\2\u00b3")
        buf.write("\u00b4\t\5\2\2\u00b4\u00b7\5\34\17\6\u00b5\u00b7\5(\25")
        buf.write("\2\u00b6\u00ae\3\2\2\2\u00b6\u00b3\3\2\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7\u00c5\3\2\2\2\u00b8\u00b9\f\5\2\2\u00b9")
        buf.write("\u00ba\t\6\2\2\u00ba\u00c4\5\34\17\6\u00bb\u00bc\f\4\2")
        buf.write("\2\u00bc\u00bd\t\7\2\2\u00bd\u00c4\5\34\17\5\u00be\u00bf")
        buf.write("\f\7\2\2\u00bf\u00c0\7-\2\2\u00c0\u00c1\5\34\17\2\u00c1")
        buf.write("\u00c2\7.\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00b8\3\2\2\2")
        buf.write("\u00c3\u00bb\3\2\2\2\u00c3\u00be\3\2\2\2\u00c4\u00c7\3")
        buf.write("\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\35")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\b\20\1\2\u00c9")
        buf.write("\u00ca\7&\2\2\u00ca\u00cb\5\32\16\2\u00cb\u00cc\7\'\2")
        buf.write("\2\u00cc\u00d5\3\2\2\2\u00cd\u00ce\t\5\2\2\u00ce\u00d5")
        buf.write("\5\36\20\7\u00cf\u00d0\5\34\17\2\u00d0\u00d1\t\3\2\2\u00d1")
        buf.write("\u00d2\5\34\17\2\u00d2\u00d5\3\2\2\2\u00d3\u00d5\5(\25")
        buf.write("\2\u00d4\u00c8\3\2\2\2\u00d4\u00cd\3\2\2\2\u00d4\u00cf")
        buf.write("\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\u00e3\3\2\2\2\u00d6")
        buf.write("\u00d7\f\6\2\2\u00d7\u00d8\t\7\2\2\u00d8\u00e2\5\36\20")
        buf.write("\7\u00d9\u00da\f\5\2\2\u00da\u00db\t\6\2\2\u00db\u00e2")
        buf.write("\5\36\20\6\u00dc\u00dd\f\b\2\2\u00dd\u00de\7-\2\2\u00de")
        buf.write("\u00df\5\36\20\2\u00df\u00e0\7.\2\2\u00e0\u00e2\3\2\2")
        buf.write("\2\u00e1\u00d6\3\2\2\2\u00e1\u00d9\3\2\2\2\u00e1\u00dc")
        buf.write("\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\37\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6")
        buf.write("\u00e7\5\32\16\2\u00e7\u00e8\7-\2\2\u00e8\u00e9\5\32\16")
        buf.write("\2\u00e9\u00ea\7.\2\2\u00ea!\3\2\2\2\u00eb\u00ec\5&\24")
        buf.write("\2\u00ec#\3\2\2\2\u00ed\u00f2\5\32\16\2\u00ee\u00ef\7")
        buf.write(",\2\2\u00ef\u00f1\5\32\16\2\u00f0\u00ee\3\2\2\2\u00f1")
        buf.write("\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2")
        buf.write("\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00ed\3")
        buf.write("\2\2\2\u00f5\u00f6\3\2\2\2\u00f6%\3\2\2\2\u00f7\u00f8")
        buf.write("\7$\2\2\u00f8\u00f9\7&\2\2\u00f9\u00fa\5$\23\2\u00fa\u00fb")
        buf.write("\7\'\2\2\u00fb\'\3\2\2\2\u00fc\u0105\7%\2\2\u00fd\u0105")
        buf.write("\7\f\2\2\u00fe\u0105\7\13\2\2\u00ff\u0105\7/\2\2\u0100")
        buf.write("\u0105\7\60\2\2\u0101\u0105\7$\2\2\u0102\u0105\5&\24\2")
        buf.write("\u0103\u0105\5\b\5\2\u0104\u00fc\3\2\2\2\u0104\u00fd\3")
        buf.write("\2\2\2\u0104\u00fe\3\2\2\2\u0104\u00ff\3\2\2\2\u0104\u0100")
        buf.write("\3\2\2\2\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2\u0104")
        buf.write("\u0103\3\2\2\2\u0105)\3\2\2\2\u0106\u0108\5\16\b\2\u0107")
        buf.write("\u0106\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2")
        buf.write("\u0109\u010a\3\2\2\2\u010a+\3\2\2\2\u010b\u0109\3\2\2")
        buf.write("\2\u010c\u010d\7\3\2\2\u010d\u010e\7*\2\2\u010e-\3\2\2")
        buf.write("\2\u010f\u0110\7\4\2\2\u0110\u0111\7*\2\2\u0111/\3\2\2")
        buf.write("\2\u0112\u0114\7\n\2\2\u0113\u0115\5\32\16\2\u0114\u0113")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0117\7*\2\2\u0117\61\3\2\2\2\u0118\u0119\5\32\16\2\u0119")
        buf.write("\u011a\7*\2\2\u011a\63\3\2\2\2\u011b\u011c\7\t\2\2\u011c")
        buf.write("\u011d\7&\2\2\u011d\u011e\5\32\16\2\u011e\u011f\7*\2\2")
        buf.write("\u011f\u0120\5\32\16\2\u0120\u0121\7*\2\2\u0121\u0122")
        buf.write("\5\32\16\2\u0122\u0123\7\'\2\2\u0123\u0124\5<\37\2\u0124")
        buf.write("\65\3\2\2\2\u0125\u0126\7(\2\2\u0126\u0127\5@!\2\u0127")
        buf.write("\u0128\7)\2\2\u0128\67\3\2\2\2\u0129\u012a\7\5\2\2\u012a")
        buf.write("\u012b\5> \2\u012b\u012c\7\6\2\2\u012c\u012d\5\32\16\2")
        buf.write("\u012d\u012e\7*\2\2\u012e9\3\2\2\2\u012f\u0130\7\7\2\2")
        buf.write("\u0130\u0131\7&\2\2\u0131\u0132\5\32\16\2\u0132\u0133")
        buf.write("\7\'\2\2\u0133\u0136\5<\37\2\u0134\u0135\7\b\2\2\u0135")
        buf.write("\u0137\5<\37\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2")
        buf.write("\u0137;\3\2\2\2\u0138\u0144\5:\36\2\u0139\u0144\58\35")
        buf.write("\2\u013a\u0144\5\64\33\2\u013b\u0144\5,\27\2\u013c\u0144")
        buf.write("\5.\30\2\u013d\u0144\5\60\31\2\u013e\u0144\5\62\32\2\u013f")
        buf.write("\u0144\5\66\34\2\u0140\u0141\5 \21\2\u0141\u0142\7*\2")
        buf.write("\2\u0142\u0144\3\2\2\2\u0143\u0138\3\2\2\2\u0143\u0139")
        buf.write("\3\2\2\2\u0143\u013a\3\2\2\2\u0143\u013b\3\2\2\2\u0143")
        buf.write("\u013c\3\2\2\2\u0143\u013d\3\2\2\2\u0143\u013e\3\2\2\2")
        buf.write("\u0143\u013f\3\2\2\2\u0143\u0140\3\2\2\2\u0144=\3\2\2")
        buf.write("\2\u0145\u0147\5<\37\2\u0146\u0145\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("?\3\2\2\2\u014a\u014d\5\16\b\2\u014b\u014d\5<\37\2\u014c")
        buf.write("\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2")
        buf.write("\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014fA\3\2\2")
        buf.write("\2\u0150\u014e\3\2\2\2\u0151\u0155\5D#\2\u0152\u0155\7")
        buf.write("\37\2\2\u0153\u0155\5\22\n\2\u0154\u0151\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0157\7$\2\2\u0157\u0159\7&\2\2\u0158\u015a\5\30")
        buf.write("\r\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b\u015c\7\'\2\2\u015c\u015d\5\66\34\2\u015d")
        buf.write("C\3\2\2\2\u015e\u015f\t\b\2\2\u015fE\3\2\2\2\36IPahz\u0080")
        buf.write("\u0087\u0099\u00a9\u00ab\u00b6\u00c3\u00c5\u00d4\u00e1")
        buf.write("\u00e3\u00f2\u00f5\u0104\u0109\u0114\u0136\u0143\u0148")
        buf.write("\u014c\u014e\u0154\u0159")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'continue'", "'do'", "'while'", 
                     "'if'", "'else'", "'for'", "'return'", "'true'", "'false'", 
                     "<INVALID>", "'+'", "'-'", "'/'", "'*'", "'%'", "'&&'", 
                     "'!'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'='", "'boolean'", "'int'", "'void'", "'float'", 
                     "'string'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "<INVALID>", 
                     "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "Break", "Continue", "Do", "While", "If", 
                      "Else", "For", "Return", "TRUE", "FALSE", "BooleanLIT", 
                      "ADD", "SUB", "DIV", "MUL", "MOD", "AND", "NOT", "OR", 
                      "EQ", "NOTEQ", "LT", "LEQ", "GT", "GEQ", "ASSIGN", 
                      "BOOLTYPE", "INTTYPE", "VOIDTYPE", "FLOATTYPE", "STRINGTYPE", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "ID", "IntLIT", "LB", 
                      "RB", "LP", "RP", "SEMI", "WS", "COMMA", "LS", "RS", 
                      "FloatLIT", "StringLIT", "LITs", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_array_type = 2
    RULE_element_of_array = 3
    RULE_variable = 4
    RULE_multi_var = 5
    RULE_var_declare = 6
    RULE_input_parameter = 7
    RULE_output_parameter = 8
    RULE_array_point = 9
    RULE_para_declare = 10
    RULE_multi_para = 11
    RULE_expression = 12
    RULE_assoc_expression = 13
    RULE_equality_expression = 14
    RULE_index_expression = 15
    RULE_invocation_expression = 16
    RULE_list_expression = 17
    RULE_function_call = 18
    RULE_operands = 19
    RULE_declare = 20
    RULE_break_stmt = 21
    RULE_continue_stmt = 22
    RULE_return_stmt = 23
    RULE_expression_stmt = 24
    RULE_for_stmt = 25
    RULE_block_stmt = 26
    RULE_dowhile_stmt = 27
    RULE_if_stmt = 28
    RULE_stmt = 29
    RULE_statement = 30
    RULE_body_block = 31
    RULE_func_declare = 32
    RULE_primitive_type = 33

    ruleNames =  [ "program", "declaration", "array_type", "element_of_array", 
                   "variable", "multi_var", "var_declare", "input_parameter", 
                   "output_parameter", "array_point", "para_declare", "multi_para", 
                   "expression", "assoc_expression", "equality_expression", 
                   "index_expression", "invocation_expression", "list_expression", 
                   "function_call", "operands", "declare", "break_stmt", 
                   "continue_stmt", "return_stmt", "expression_stmt", "for_stmt", 
                   "block_stmt", "dowhile_stmt", "if_stmt", "stmt", "statement", 
                   "body_block", "func_declare", "primitive_type" ]

    EOF = Token.EOF
    Break=1
    Continue=2
    Do=3
    While=4
    If=5
    Else=6
    For=7
    Return=8
    TRUE=9
    FALSE=10
    BooleanLIT=11
    ADD=12
    SUB=13
    DIV=14
    MUL=15
    MOD=16
    AND=17
    NOT=18
    OR=19
    EQ=20
    NOTEQ=21
    LT=22
    LEQ=23
    GT=24
    GEQ=25
    ASSIGN=26
    BOOLTYPE=27
    INTTYPE=28
    VOIDTYPE=29
    FLOATTYPE=30
    STRINGTYPE=31
    BLOCK_COMMENT=32
    LINE_COMMENT=33
    ID=34
    IntLIT=35
    LB=36
    RB=37
    LP=38
    RP=39
    SEMI=40
    WS=41
    COMMA=42
    LS=43
    RS=44
    FloatLIT=45
    StringLIT=46
    LITs=47
    ERROR_CHAR=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.VOIDTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 68
                self.declaration()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_declare(self):
            return self.getTypedRuleContext(MCParser.Func_declareContext,0)


        def var_declare(self):
            return self.getTypedRuleContext(MCParser.Var_declareContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_declaration




    def declaration(self):

        localctx = MCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.func_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.var_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def IntLIT(self):
            return self.getToken(MCParser.IntLIT, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_array_type




    def array_type(self):

        localctx = MCParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.primitive_type()
            self.state = 81
            self.match(MCParser.LS)
            self.state = 82
            self.match(MCParser.IntLIT)
            self.state = 83
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Element_of_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.ID)
            else:
                return self.getToken(MCParser.ID, i)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def IntLIT(self):
            return self.getToken(MCParser.IntLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_element_of_array




    def element_of_array(self):

        localctx = MCParser.Element_of_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_element_of_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(MCParser.ID)
            self.state = 86
            self.match(MCParser.LS)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==MCParser.ID or _la==MCParser.IntLIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 88
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def IntLIT(self):
            return self.getToken(MCParser.IntLIT, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_variable




    def variable(self):

        localctx = MCParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(MCParser.ID)
                self.state = 91
                self.match(MCParser.LS)
                self.state = 92
                self.match(MCParser.IntLIT)
                self.state = 93
                self.match(MCParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(MCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Multi_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VariableContext)
            else:
                return self.getTypedRuleContext(MCParser.VariableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_multi_var




    def multi_var(self):

        localctx = MCParser.Multi_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multi_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.variable()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 98
                self.match(MCParser.COMMA)
                self.state = 99
                self.variable()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def multi_var(self):
            return self.getTypedRuleContext(MCParser.Multi_varContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var_declare




    def var_declare(self):

        localctx = MCParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.primitive_type()
            self.state = 106
            self.multi_var()
            self.state = 107
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Input_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_input_parameter




    def input_parameter(self):

        localctx = MCParser.Input_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_input_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.primitive_type()
            self.state = 110
            self.match(MCParser.ID)
            self.state = 111
            self.match(MCParser.LS)
            self.state = 112
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Output_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_output_parameter




    def output_parameter(self):

        localctx = MCParser.Output_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_output_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.primitive_type()
            self.state = 115
            self.match(MCParser.LS)
            self.state = 116
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_pointContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def input_parameter(self):
            return self.getTypedRuleContext(MCParser.Input_parameterContext,0)


        def output_parameter(self):
            return self.getTypedRuleContext(MCParser.Output_parameterContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_array_point




    def array_point(self):

        localctx = MCParser.Array_pointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_point)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.input_parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.output_parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Para_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_para_declare




    def para_declare(self):

        localctx = MCParser.Para_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_para_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.primitive_type()
            self.state = 123
            self.match(MCParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 124
                self.match(MCParser.LS)
                self.state = 125
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Multi_paraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Para_declareContext)
            else:
                return self.getTypedRuleContext(MCParser.Para_declareContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_multi_para




    def multi_para(self):

        localctx = MCParser.Multi_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_multi_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.para_declare()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 129
                self.match(MCParser.COMMA)
                self.state = 130
                self.para_declare()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressionContext,i)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def assoc_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Assoc_expressionContext)
            else:
                return self.getTypedRuleContext(MCParser.Assoc_expressionContext,i)


        def LT(self):
            return self.getToken(MCParser.LT, 0)

        def LEQ(self):
            return self.getToken(MCParser.LEQ, 0)

        def GT(self):
            return self.getToken(MCParser.GT, 0)

        def GEQ(self):
            return self.getToken(MCParser.GEQ, 0)

        def equality_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Equality_expressionContext)
            else:
                return self.getTypedRuleContext(MCParser.Equality_expressionContext,i)


        def EQ(self):
            return self.getToken(MCParser.EQ, 0)

        def NOTEQ(self):
            return self.getToken(MCParser.NOTEQ, 0)

        def operands(self):
            return self.getTypedRuleContext(MCParser.OperandsContext,0)


        def AND(self):
            return self.getToken(MCParser.AND, 0)

        def OR(self):
            return self.getToken(MCParser.OR, 0)

        def ASSIGN(self):
            return self.getToken(MCParser.ASSIGN, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 137
                self.match(MCParser.LB)
                self.state = 138
                self.expression(0)
                self.state = 139
                self.match(MCParser.RB)
                pass

            elif la_ == 2:
                self.state = 141
                self.assoc_expression(0)
                pass

            elif la_ == 3:
                self.state = 142
                self.assoc_expression(0)
                self.state = 143
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LT) | (1 << MCParser.LEQ) | (1 << MCParser.GT) | (1 << MCParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.assoc_expression(0)
                pass

            elif la_ == 4:
                self.state = 146
                self.equality_expression(0)
                self.state = 147
                _la = self._input.LA(1)
                if not(_la==MCParser.EQ or _la==MCParser.NOTEQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.equality_expression(0)
                pass

            elif la_ == 5:
                self.state = 150
                self.operands()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 167
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 153
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 154
                        self.match(MCParser.AND)
                        self.state = 155
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 156
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 157
                        self.match(MCParser.OR)
                        self.state = 158
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 159
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 160
                        self.match(MCParser.ASSIGN)
                        self.state = 161
                        self.expression(2)
                        pass

                    elif la_ == 4:
                        localctx = MCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 162
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 163
                        self.match(MCParser.LS)
                        self.state = 164
                        self.expression(0)
                        self.state = 165
                        self.match(MCParser.RS)
                        pass

             
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Assoc_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def assoc_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Assoc_expressionContext)
            else:
                return self.getTypedRuleContext(MCParser.Assoc_expressionContext,i)


        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def NOT(self):
            return self.getToken(MCParser.NOT, 0)

        def operands(self):
            return self.getTypedRuleContext(MCParser.OperandsContext,0)


        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def MOD(self):
            return self.getToken(MCParser.MOD, 0)

        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_assoc_expression



    def assoc_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Assoc_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_assoc_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.LB]:
                self.state = 173
                self.match(MCParser.LB)
                self.state = 174
                self.expression(0)
                self.state = 175
                self.match(MCParser.RB)
                pass
            elif token in [MCParser.SUB, MCParser.NOT]:
                self.state = 177
                _la = self._input.LA(1)
                if not(_la==MCParser.SUB or _la==MCParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self.assoc_expression(4)
                pass
            elif token in [MCParser.TRUE, MCParser.FALSE, MCParser.ID, MCParser.IntLIT, MCParser.FloatLIT, MCParser.StringLIT]:
                self.state = 179
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 193
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.Assoc_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_assoc_expression)
                        self.state = 182
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 183
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.DIV) | (1 << MCParser.MUL) | (1 << MCParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 184
                        self.assoc_expression(4)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.Assoc_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_assoc_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 186
                        _la = self._input.LA(1)
                        if not(_la==MCParser.ADD or _la==MCParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 187
                        self.assoc_expression(3)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.Assoc_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_assoc_expression)
                        self.state = 188
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 189
                        self.match(MCParser.LS)
                        self.state = 190
                        self.assoc_expression(0)
                        self.state = 191
                        self.match(MCParser.RS)
                        pass

             
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Equality_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def equality_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Equality_expressionContext)
            else:
                return self.getTypedRuleContext(MCParser.Equality_expressionContext,i)


        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def NOT(self):
            return self.getToken(MCParser.NOT, 0)

        def assoc_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Assoc_expressionContext)
            else:
                return self.getTypedRuleContext(MCParser.Assoc_expressionContext,i)


        def LT(self):
            return self.getToken(MCParser.LT, 0)

        def LEQ(self):
            return self.getToken(MCParser.LEQ, 0)

        def GT(self):
            return self.getToken(MCParser.GT, 0)

        def GEQ(self):
            return self.getToken(MCParser.GEQ, 0)

        def operands(self):
            return self.getTypedRuleContext(MCParser.OperandsContext,0)


        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def MOD(self):
            return self.getToken(MCParser.MOD, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_equality_expression



    def equality_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Equality_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_equality_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 199
                self.match(MCParser.LB)
                self.state = 200
                self.expression(0)
                self.state = 201
                self.match(MCParser.RB)
                pass

            elif la_ == 2:
                self.state = 203
                _la = self._input.LA(1)
                if not(_la==MCParser.SUB or _la==MCParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 204
                self.equality_expression(5)
                pass

            elif la_ == 3:
                self.state = 205
                self.assoc_expression(0)
                self.state = 206
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LT) | (1 << MCParser.LEQ) | (1 << MCParser.GT) | (1 << MCParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 207
                self.assoc_expression(0)
                pass

            elif la_ == 4:
                self.state = 209
                self.operands()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 225
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 223
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.Equality_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equality_expression)
                        self.state = 212
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 213
                        _la = self._input.LA(1)
                        if not(_la==MCParser.ADD or _la==MCParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 214
                        self.equality_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.Equality_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equality_expression)
                        self.state = 215
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 216
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.DIV) | (1 << MCParser.MUL) | (1 << MCParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 217
                        self.equality_expression(4)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.Equality_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equality_expression)
                        self.state = 218
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 219
                        self.match(MCParser.LS)
                        self.state = 220
                        self.equality_expression(0)
                        self.state = 221
                        self.match(MCParser.RS)
                        pass

             
                self.state = 227
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Index_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressionContext,i)


        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_index_expression




    def index_expression(self):

        localctx = MCParser.Index_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_index_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.expression(0)
            self.state = 229
            self.match(MCParser.LS)
            self.state = 230
            self.expression(0)
            self.state = 231
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Invocation_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(MCParser.Function_callContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_invocation_expression




    def invocation_expression(self):

        localctx = MCParser.Invocation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_invocation_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.function_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_expression




    def list_expression(self):

        localctx = MCParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_list_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.TRUE) | (1 << MCParser.FALSE) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.ID) | (1 << MCParser.IntLIT) | (1 << MCParser.LB) | (1 << MCParser.FloatLIT) | (1 << MCParser.StringLIT))) != 0):
                self.state = 235
                self.expression(0)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.COMMA:
                    self.state = 236
                    self.match(MCParser.COMMA)
                    self.state = 237
                    self.expression(0)
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MCParser.List_expressionContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_function_call




    def function_call(self):

        localctx = MCParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(MCParser.ID)
            self.state = 246
            self.match(MCParser.LB)
            self.state = 247
            self.list_expression()
            self.state = 248
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntLIT(self):
            return self.getToken(MCParser.IntLIT, 0)

        def FALSE(self):
            return self.getToken(MCParser.FALSE, 0)

        def TRUE(self):
            return self.getToken(MCParser.TRUE, 0)

        def FloatLIT(self):
            return self.getToken(MCParser.FloatLIT, 0)

        def StringLIT(self):
            return self.getToken(MCParser.StringLIT, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MCParser.Function_callContext,0)


        def element_of_array(self):
            return self.getTypedRuleContext(MCParser.Element_of_arrayContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_operands




    def operands(self):

        localctx = MCParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_operands)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(MCParser.IntLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(MCParser.FALSE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.match(MCParser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.match(MCParser.FloatLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.match(MCParser.StringLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.match(MCParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
                self.function_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 257
                self.element_of_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(MCParser.Var_declareContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_declare




    def declare(self):

        localctx = MCParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 260
                self.var_declare()
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(MCParser.Break, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MCParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MCParser.Break)
            self.state = 267
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(MCParser.Continue, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MCParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MCParser.Continue)
            self.state = 270
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(MCParser.Return, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return_stmt




    def return_stmt(self):

        localctx = MCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MCParser.Return)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.TRUE) | (1 << MCParser.FALSE) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.ID) | (1 << MCParser.IntLIT) | (1 << MCParser.LB) | (1 << MCParser.FloatLIT) | (1 << MCParser.StringLIT))) != 0):
                self.state = 273
                self.expression(0)


            self.state = 276
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression_stmt




    def expression_stmt(self):

        localctx = MCParser.Expression_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.expression(0)
            self.state = 279
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For(self):
            return self.getToken(MCParser.For, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressionContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_stmt




    def for_stmt(self):

        localctx = MCParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(MCParser.For)
            self.state = 282
            self.match(MCParser.LB)
            self.state = 283
            self.expression(0)
            self.state = 284
            self.match(MCParser.SEMI)
            self.state = 285
            self.expression(0)
            self.state = 286
            self.match(MCParser.SEMI)
            self.state = 287
            self.expression(0)
            self.state = 288
            self.match(MCParser.RB)
            self.state = 289
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def body_block(self):
            return self.getTypedRuleContext(MCParser.Body_blockContext,0)


        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_block_stmt




    def block_stmt(self):

        localctx = MCParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(MCParser.LP)
            self.state = 292
            self.body_block()
            self.state = 293
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dowhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Do(self):
            return self.getToken(MCParser.Do, 0)

        def statement(self):
            return self.getTypedRuleContext(MCParser.StatementContext,0)


        def While(self):
            return self.getToken(MCParser.While, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_dowhile_stmt




    def dowhile_stmt(self):

        localctx = MCParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(MCParser.Do)
            self.state = 296
            self.statement()
            self.state = 297
            self.match(MCParser.While)
            self.state = 298
            self.expression(0)
            self.state = 299
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(MCParser.If, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def Else(self):
            return self.getToken(MCParser.Else, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_stmt




    def if_stmt(self):

        localctx = MCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(MCParser.If)
            self.state = 302
            self.match(MCParser.LB)
            self.state = 303
            self.expression(0)
            self.state = 304
            self.match(MCParser.RB)
            self.state = 305
            self.stmt()
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 306
                self.match(MCParser.Else)
                self.state = 307
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(MCParser.If_stmtContext,0)


        def dowhile_stmt(self):
            return self.getTypedRuleContext(MCParser.Dowhile_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MCParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MCParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MCParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MCParser.Return_stmtContext,0)


        def expression_stmt(self):
            return self.getTypedRuleContext(MCParser.Expression_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def index_expression(self):
            return self.getTypedRuleContext(MCParser.Index_expressionContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_stmt




    def stmt(self):

        localctx = MCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.dowhile_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 315
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 316
                self.expression_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 317
                self.block_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 318
                self.index_expression()
                self.state = 319
                self.match(MCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_statement




    def statement(self):

        localctx = MCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 323
                self.stmt()
                self.state = 326 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.Break) | (1 << MCParser.Continue) | (1 << MCParser.Do) | (1 << MCParser.If) | (1 << MCParser.For) | (1 << MCParser.Return) | (1 << MCParser.TRUE) | (1 << MCParser.FALSE) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.ID) | (1 << MCParser.IntLIT) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.FloatLIT) | (1 << MCParser.StringLIT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Body_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(MCParser.Var_declareContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_body_block




    def body_block(self):

        localctx = MCParser.Body_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_body_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.Break) | (1 << MCParser.Continue) | (1 << MCParser.Do) | (1 << MCParser.If) | (1 << MCParser.For) | (1 << MCParser.Return) | (1 << MCParser.TRUE) | (1 << MCParser.FALSE) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.ID) | (1 << MCParser.IntLIT) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.FloatLIT) | (1 << MCParser.StringLIT))) != 0):
                self.state = 330
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.BOOLTYPE, MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE]:
                    self.state = 328
                    self.var_declare()
                    pass
                elif token in [MCParser.Break, MCParser.Continue, MCParser.Do, MCParser.If, MCParser.For, MCParser.Return, MCParser.TRUE, MCParser.FALSE, MCParser.SUB, MCParser.NOT, MCParser.ID, MCParser.IntLIT, MCParser.LB, MCParser.LP, MCParser.FloatLIT, MCParser.StringLIT]:
                    self.state = 329
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def output_parameter(self):
            return self.getTypedRuleContext(MCParser.Output_parameterContext,0)


        def multi_para(self):
            return self.getTypedRuleContext(MCParser.Multi_paraContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_func_declare




    def func_declare(self):

        localctx = MCParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 335
                self.primitive_type()
                pass

            elif la_ == 2:
                self.state = 336
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.state = 337
                self.output_parameter()
                pass


            self.state = 340
            self.match(MCParser.ID)
            self.state = 341
            self.match(MCParser.LB)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 342
                self.multi_para()


            self.state = 345
            self.match(MCParser.RB)
            self.state = 346
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primitive_type




    def primitive_type(self):

        localctx = MCParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expression_sempred
        self._predicates[13] = self.assoc_expression_sempred
        self._predicates[14] = self.equality_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

    def assoc_expression_sempred(self, localctx:Assoc_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

    def equality_expression_sempred(self, localctx:Equality_expressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 6)
         




