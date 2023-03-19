# Generated from d:\HK222-2023-BKHCM\PPL\assignment1-initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0274\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0115\n\f\f\f\16\f\u0118")
        buf.write("\13\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0120\n\f\f\f\16\f\u0123")
        buf.write("\13\f\5\f\u0125\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\7\"\u01a4\n\"\f\"\16\"\u01a7\13\"\3#\3#\3")
        buf.write("#\7#\u01ac\n#\f#\16#\u01af\13#\3#\5#\u01b2\n#\3$\3$\3")
        buf.write("$\7$\u01b7\n$\f$\16$\u01ba\13$\3$\3$\3$\3%\3%\3%\3%\5")
        buf.write("%\u01c3\n%\3&\3&\3&\3&\3&\3&\5&\u01cb\n&\3&\3&\3&\5&\u01d0")
        buf.write("\n&\3\'\3\'\3\'\7\'\u01d5\n\'\f\'\16\'\u01d8\13\'\5\'")
        buf.write("\u01da\n\'\3(\3(\6(\u01de\n(\r(\16(\u01df\3)\3)\5)\u01e4")
        buf.write("\n)\3)\6)\u01e7\n)\r)\16)\u01e8\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\5\66")
        buf.write("\u0209\n\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5")
        buf.write("\67\u0213\n\67\38\38\38\38\38\58\u021a\n8\39\39\59\u021e")
        buf.write("\n9\39\39\39\39\39\59\u0225\n9\59\u0227\n9\3:\3:\3:\3")
        buf.write(":\3:\5:\u022e\n:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3A\3B\3B\3B\3C\3C\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3")
        buf.write("G\3H\3H\3H\3I\6I\u0253\nI\rI\16I\u0254\3I\3I\3J\3J\3J")
        buf.write("\7J\u025c\nJ\fJ\16J\u025f\13J\3J\5J\u0262\nJ\3J\3J\3K")
        buf.write("\3K\3K\7K\u0269\nK\fK\16K\u026c\13K\3K\3K\3K\3K\3L\3L")
        buf.write("\3L\3\u0116\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I\2K&M\2O\2Q\2S\'U(W)Y*[+],_-a.c/e\60g\61i\62k\63")
        buf.write("m\2o\2q\2s\2u\64w\65y\66{\67}8\1779\u0081:\u0083;\u0085")
        buf.write("<\u0087=\u0089>\u008b?\u008d@\u008fA\u0091B\u0093C\u0095")
        buf.write("D\u0097E\3\2\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\4\2")
        buf.write("\62;aa\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\5\2\13\f\17\17\"\"\5\2\f\f$$^^\3\3\f\f\n")
        buf.write("\2$$))^^ddhhppttvv\2\u028a\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2K\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\3\u0099\3\2\2\2\5\u00a5\3\2\2\2\7\u00b2\3\2\2\2\t\u00bc")
        buf.write("\3\2\2\2\13\u00c7\3\2\2\2\r\u00d3\3\2\2\2\17\u00e0\3\2")
        buf.write("\2\2\21\u00eb\3\2\2\2\23\u00f7\3\2\2\2\25\u00fd\3\2\2")
        buf.write("\2\27\u0124\3\2\2\2\31\u0126\3\2\2\2\33\u012e\3\2\2\2")
        buf.write("\35\u0134\3\2\2\2\37\u013b\3\2\2\2!\u0143\3\2\2\2#\u0148")
        buf.write("\3\2\2\2%\u014e\3\2\2\2\'\u0151\3\2\2\2)\u0156\3\2\2\2")
        buf.write("+\u015b\3\2\2\2-\u0161\3\2\2\2/\u016a\3\2\2\2\61\u016e")
        buf.write("\3\2\2\2\63\u0171\3\2\2\2\65\u0178\3\2\2\2\67\u017e\3")
        buf.write("\2\2\29\u0183\3\2\2\2;\u0187\3\2\2\2=\u0190\3\2\2\2?\u0196")
        buf.write("\3\2\2\2A\u019e\3\2\2\2C\u01a1\3\2\2\2E\u01b1\3\2\2\2")
        buf.write("G\u01b3\3\2\2\2I\u01c2\3\2\2\2K\u01cf\3\2\2\2M\u01d9\3")
        buf.write("\2\2\2O\u01db\3\2\2\2Q\u01e1\3\2\2\2S\u01ea\3\2\2\2U\u01ec")
        buf.write("\3\2\2\2W\u01ee\3\2\2\2Y\u01f0\3\2\2\2[\u01f2\3\2\2\2")
        buf.write("]\u01f4\3\2\2\2_\u01f6\3\2\2\2a\u01f8\3\2\2\2c\u01fa\3")
        buf.write("\2\2\2e\u01fc\3\2\2\2g\u01fe\3\2\2\2i\u0200\3\2\2\2k\u0203")
        buf.write("\3\2\2\2m\u0212\3\2\2\2o\u0219\3\2\2\2q\u0226\3\2\2\2")
        buf.write("s\u022d\3\2\2\2u\u022f\3\2\2\2w\u0231\3\2\2\2y\u0233\3")
        buf.write("\2\2\2{\u0235\3\2\2\2}\u0237\3\2\2\2\177\u0239\3\2\2\2")
        buf.write("\u0081\u023b\3\2\2\2\u0083\u023e\3\2\2\2\u0085\u0241\3")
        buf.write("\2\2\2\u0087\u0243\3\2\2\2\u0089\u0245\3\2\2\2\u008b\u0248")
        buf.write("\3\2\2\2\u008d\u024b\3\2\2\2\u008f\u024e\3\2\2\2\u0091")
        buf.write("\u0252\3\2\2\2\u0093\u0258\3\2\2\2\u0095\u0265\3\2\2\2")
        buf.write("\u0097\u0271\3\2\2\2\u0099\u009a\7t\2\2\u009a\u009b\7")
        buf.write("g\2\2\u009b\u009c\7c\2\2\u009c\u009d\7f\2\2\u009d\u009e")
        buf.write("\7K\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1")
        buf.write("\7g\2\2\u00a1\u00a2\7i\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\4\3\2\2\2\u00a5\u00a6\7r\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7K\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7i\2\2\u00af\u00b0")
        buf.write("\7g\2\2\u00b0\u00b1\7t\2\2\u00b1\6\3\2\2\2\u00b2\u00b3")
        buf.write("\7t\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6")
        buf.write("\7f\2\2\u00b6\u00b7\7H\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7v\2\2\u00bb\b")
        buf.write("\3\2\2\2\u00bc\u00bd\7y\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2")
        buf.write("\7H\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7c\2\2\u00c5\u00c6\7v\2\2\u00c6\n\3\2\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7f\2\2\u00cb\u00cc\7D\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7q\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1")
        buf.write("\7c\2\2\u00d1\u00d2\7p\2\2\u00d2\f\3\2\2\2\u00d3\u00d4")
        buf.write("\7r\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7D\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7p\2\2\u00df\16")
        buf.write("\3\2\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7c\2\2\u00e3\u00e4\7f\2\2\u00e4\u00e5\7U\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7i\2\2\u00ea\20\3\2\2\2\u00eb\u00ec")
        buf.write("\7r\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7U\2\2\u00f1\u00f2")
        buf.write("\7v\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7i\2\2\u00f6\22\3\2\2\2\u00f7\u00f8")
        buf.write("\7u\2\2\u00f8\u00f9\7w\2\2\u00f9\u00fa\7r\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7t\2\2\u00fc\24\3\2\2\2\u00fd\u00fe")
        buf.write("\7r\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7x\2\2\u0101\u0102\7g\2\2\u0102\u0103\7p\2\2\u0103\u0104")
        buf.write("\7v\2\2\u0104\u0105\7F\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7h\2\2\u0107\u0108\7c\2\2\u0108\u0109\7w\2\2\u0109\u010a")
        buf.write("\7n\2\2\u010a\u010b\7v\2\2\u010b\26\3\2\2\2\u010c\u010d")
        buf.write("\7\61\2\2\u010d\u010e\7,\2\2\u010e\u010f\7,\2\2\u010f")
        buf.write("\u0125\7\61\2\2\u0110\u0111\7\61\2\2\u0111\u0112\7,\2")
        buf.write("\2\u0112\u0116\3\2\2\2\u0113\u0115\13\2\2\2\u0114\u0113")
        buf.write("\3\2\2\2\u0115\u0118\3\2\2\2\u0116\u0117\3\2\2\2\u0116")
        buf.write("\u0114\3\2\2\2\u0117\u0119\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0119\u011a\7,\2\2\u011a\u0125\7\61\2\2\u011b\u011c\7")
        buf.write("\61\2\2\u011c\u011d\7\61\2\2\u011d\u0121\3\2\2\2\u011e")
        buf.write("\u0120\13\2\2\2\u011f\u011e\3\2\2\2\u0120\u0123\3\2\2")
        buf.write("\2\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0125")
        buf.write("\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u010c\3\2\2\2\u0124")
        buf.write("\u0110\3\2\2\2\u0124\u011b\3\2\2\2\u0125\30\3\2\2\2\u0126")
        buf.write("\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write("\u012a\7g\2\2\u012a\u012b\7i\2\2\u012b\u012c\7g\2\2\u012c")
        buf.write("\u012d\7t\2\2\u012d\32\3\2\2\2\u012e\u012f\7h\2\2\u012f")
        buf.write("\u0130\7n\2\2\u0130\u0131\7q\2\2\u0131\u0132\7c\2\2\u0132")
        buf.write("\u0133\7v\2\2\u0133\34\3\2\2\2\u0134\u0135\7u\2\2\u0135")
        buf.write("\u0136\7v\2\2\u0136\u0137\7t\2\2\u0137\u0138\7k\2\2\u0138")
        buf.write("\u0139\7p\2\2\u0139\u013a\7i\2\2\u013a\36\3\2\2\2\u013b")
        buf.write("\u013c\7d\2\2\u013c\u013d\7q\2\2\u013d\u013e\7q\2\2\u013e")
        buf.write("\u013f\7n\2\2\u013f\u0140\7g\2\2\u0140\u0141\7c\2\2\u0141")
        buf.write("\u0142\7p\2\2\u0142 \3\2\2\2\u0143\u0144\7c\2\2\u0144")
        buf.write("\u0145\7w\2\2\u0145\u0146\7v\2\2\u0146\u0147\7q\2\2\u0147")
        buf.write("\"\3\2\2\2\u0148\u0149\7d\2\2\u0149\u014a\7t\2\2\u014a")
        buf.write("\u014b\7g\2\2\u014b\u014c\7c\2\2\u014c\u014d\7m\2\2\u014d")
        buf.write("$\3\2\2\2\u014e\u014f\7f\2\2\u014f\u0150\7q\2\2\u0150")
        buf.write("&\3\2\2\2\u0151\u0152\7g\2\2\u0152\u0153\7n\2\2\u0153")
        buf.write("\u0154\7u\2\2\u0154\u0155\7g\2\2\u0155(\3\2\2\2\u0156")
        buf.write("\u0157\7v\2\2\u0157\u0158\7t\2\2\u0158\u0159\7w\2\2\u0159")
        buf.write("\u015a\7g\2\2\u015a*\3\2\2\2\u015b\u015c\7h\2\2\u015c")
        buf.write("\u015d\7c\2\2\u015d\u015e\7n\2\2\u015e\u015f\7u\2\2\u015f")
        buf.write("\u0160\7g\2\2\u0160,\3\2\2\2\u0161\u0162\7h\2\2\u0162")
        buf.write("\u0163\7w\2\2\u0163\u0164\7p\2\2\u0164\u0165\7e\2\2\u0165")
        buf.write("\u0166\7v\2\2\u0166\u0167\7k\2\2\u0167\u0168\7q\2\2\u0168")
        buf.write("\u0169\7p\2\2\u0169.\3\2\2\2\u016a\u016b\7h\2\2\u016b")
        buf.write("\u016c\7q\2\2\u016c\u016d\7t\2\2\u016d\60\3\2\2\2\u016e")
        buf.write("\u016f\7k\2\2\u016f\u0170\7h\2\2\u0170\62\3\2\2\2\u0171")
        buf.write("\u0172\7t\2\2\u0172\u0173\7g\2\2\u0173\u0174\7v\2\2\u0174")
        buf.write("\u0175\7w\2\2\u0175\u0176\7t\2\2\u0176\u0177\7p\2\2\u0177")
        buf.write("\64\3\2\2\2\u0178\u0179\7y\2\2\u0179\u017a\7j\2\2\u017a")
        buf.write("\u017b\7k\2\2\u017b\u017c\7n\2\2\u017c\u017d\7g\2\2\u017d")
        buf.write("\66\3\2\2\2\u017e\u017f\7x\2\2\u017f\u0180\7q\2\2\u0180")
        buf.write("\u0181\7k\2\2\u0181\u0182\7f\2\2\u01828\3\2\2\2\u0183")
        buf.write("\u0184\7q\2\2\u0184\u0185\7w\2\2\u0185\u0186\7v\2\2\u0186")
        buf.write(":\3\2\2\2\u0187\u0188\7e\2\2\u0188\u0189\7q\2\2\u0189")
        buf.write("\u018a\7p\2\2\u018a\u018b\7v\2\2\u018b\u018c\7k\2\2\u018c")
        buf.write("\u018d\7p\2\2\u018d\u018e\7w\2\2\u018e\u018f\7g\2\2\u018f")
        buf.write("<\3\2\2\2\u0190\u0191\7c\2\2\u0191\u0192\7t\2\2\u0192")
        buf.write("\u0193\7t\2\2\u0193\u0194\7c\2\2\u0194\u0195\7{\2\2\u0195")
        buf.write(">\3\2\2\2\u0196\u0197\7k\2\2\u0197\u0198\7p\2\2\u0198")
        buf.write("\u0199\7j\2\2\u0199\u019a\7g\2\2\u019a\u019b\7t\2\2\u019b")
        buf.write("\u019c\7k\2\2\u019c\u019d\7v\2\2\u019d@\3\2\2\2\u019e")
        buf.write("\u019f\7q\2\2\u019f\u01a0\7h\2\2\u01a0B\3\2\2\2\u01a1")
        buf.write("\u01a5\t\2\2\2\u01a2\u01a4\t\3\2\2\u01a3\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3")
        buf.write("\2\2\2\u01a6D\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01b2")
        buf.write("\7\62\2\2\u01a9\u01ad\t\4\2\2\u01aa\u01ac\t\5\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01b0\u01b2\b#\2\2\u01b1\u01a8\3\2\2\2\u01b1\u01a9")
        buf.write("\3\2\2\2\u01b2F\3\2\2\2\u01b3\u01b8\7$\2\2\u01b4\u01b7")
        buf.write("\5I%\2\u01b5\u01b7\n\6\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01bb\u01bc\7$\2\2\u01bc\u01bd\b$\3\2\u01bdH\3\2\2\2")
        buf.write("\u01be\u01bf\7^\2\2\u01bf\u01c3\t\7\2\2\u01c0\u01c1\7")
        buf.write("^\2\2\u01c1\u01c3\7$\2\2\u01c2\u01be\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c3J\3\2\2\2\u01c4\u01c5\5M\'\2\u01c5\u01c6")
        buf.write("\5O(\2\u01c6\u01c7\b&\4\2\u01c7\u01d0\3\2\2\2\u01c8\u01ca")
        buf.write("\5M\'\2\u01c9\u01cb\5O(\2\u01ca\u01c9\3\2\2\2\u01ca\u01cb")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\5Q)\2\u01cd\u01ce")
        buf.write("\b&\5\2\u01ce\u01d0\3\2\2\2\u01cf\u01c4\3\2\2\2\u01cf")
        buf.write("\u01c8\3\2\2\2\u01d0L\3\2\2\2\u01d1\u01da\7\62\2\2\u01d2")
        buf.write("\u01d6\t\4\2\2\u01d3\u01d5\t\5\2\2\u01d4\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3")
        buf.write("\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01d1")
        buf.write("\3\2\2\2\u01d9\u01d2\3\2\2\2\u01daN\3\2\2\2\u01db\u01dd")
        buf.write("\7\60\2\2\u01dc\u01de\t\b\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0P\3\2\2\2\u01e1\u01e3\t\t\2\2\u01e2\u01e4\t\n\2")
        buf.write("\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e6")
        buf.write("\3\2\2\2\u01e5\u01e7\t\b\2\2\u01e6\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2")
        buf.write("\u01e9R\3\2\2\2\u01ea\u01eb\7*\2\2\u01ebT\3\2\2\2\u01ec")
        buf.write("\u01ed\7+\2\2\u01edV\3\2\2\2\u01ee\u01ef\7\60\2\2\u01ef")
        buf.write("X\3\2\2\2\u01f0\u01f1\7.\2\2\u01f1Z\3\2\2\2\u01f2\u01f3")
        buf.write("\7=\2\2\u01f3\\\3\2\2\2\u01f4\u01f5\7<\2\2\u01f5^\3\2")
        buf.write("\2\2\u01f6\u01f7\7}\2\2\u01f7`\3\2\2\2\u01f8\u01f9\7\177")
        buf.write("\2\2\u01f9b\3\2\2\2\u01fa\u01fb\7]\2\2\u01fbd\3\2\2\2")
        buf.write("\u01fc\u01fd\7_\2\2\u01fdf\3\2\2\2\u01fe\u01ff\7?\2\2")
        buf.write("\u01ffh\3\2\2\2\u0200\u0201\7<\2\2\u0201\u0202\7<\2\2")
        buf.write("\u0202j\3\2\2\2\u0203\u0208\5_\60\2\u0204\u0209\5m\67")
        buf.write("\2\u0205\u0209\5o8\2\u0206\u0209\5q9\2\u0207\u0209\5s")
        buf.write(":\2\u0208\u0204\3\2\2\2\u0208\u0205\3\2\2\2\u0208\u0206")
        buf.write("\3\2\2\2\u0208\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a")
        buf.write("\u020b\5a\61\2\u020b\u020c\b\66\6\2\u020cl\3\2\2\2\u020d")
        buf.write("\u020e\5G$\2\u020e\u020f\5Y-\2\u020f\u0210\5m\67\2\u0210")
        buf.write("\u0213\3\2\2\2\u0211\u0213\5G$\2\u0212\u020d\3\2\2\2\u0212")
        buf.write("\u0211\3\2\2\2\u0213n\3\2\2\2\u0214\u0215\5E#\2\u0215")
        buf.write("\u0216\5Y-\2\u0216\u0217\5o8\2\u0217\u021a\3\2\2\2\u0218")
        buf.write("\u021a\5E#\2\u0219\u0214\3\2\2\2\u0219\u0218\3\2\2\2\u021a")
        buf.write("p\3\2\2\2\u021b\u021e\5)\25\2\u021c\u021e\5+\26\2\u021d")
        buf.write("\u021b\3\2\2\2\u021d\u021c\3\2\2\2\u021e\u021f\3\2\2\2")
        buf.write("\u021f\u0220\5Y-\2\u0220\u0221\5q9\2\u0221\u0227\3\2\2")
        buf.write("\2\u0222\u0225\5)\25\2\u0223\u0225\5+\26\2\u0224\u0222")
        buf.write("\3\2\2\2\u0224\u0223\3\2\2\2\u0225\u0227\3\2\2\2\u0226")
        buf.write("\u021d\3\2\2\2\u0226\u0224\3\2\2\2\u0227r\3\2\2\2\u0228")
        buf.write("\u0229\5K&\2\u0229\u022a\5Y-\2\u022a\u022b\5s:\2\u022b")
        buf.write("\u022e\3\2\2\2\u022c\u022e\5K&\2\u022d\u0228\3\2\2\2\u022d")
        buf.write("\u022c\3\2\2\2\u022et\3\2\2\2\u022f\u0230\7-\2\2\u0230")
        buf.write("v\3\2\2\2\u0231\u0232\7,\2\2\u0232x\3\2\2\2\u0233\u0234")
        buf.write("\7\61\2\2\u0234z\3\2\2\2\u0235\u0236\7\'\2\2\u0236|\3")
        buf.write("\2\2\2\u0237\u0238\7#\2\2\u0238~\3\2\2\2\u0239\u023a\7")
        buf.write("/\2\2\u023a\u0080\3\2\2\2\u023b\u023c\7?\2\2\u023c\u023d")
        buf.write("\7?\2\2\u023d\u0082\3\2\2\2\u023e\u023f\7#\2\2\u023f\u0240")
        buf.write("\7?\2\2\u0240\u0084\3\2\2\2\u0241\u0242\7@\2\2\u0242\u0086")
        buf.write("\3\2\2\2\u0243\u0244\7>\2\2\u0244\u0088\3\2\2\2\u0245")
        buf.write("\u0246\7@\2\2\u0246\u0247\7?\2\2\u0247\u008a\3\2\2\2\u0248")
        buf.write("\u0249\7>\2\2\u0249\u024a\7?\2\2\u024a\u008c\3\2\2\2\u024b")
        buf.write("\u024c\7(\2\2\u024c\u024d\7(\2\2\u024d\u008e\3\2\2\2\u024e")
        buf.write("\u024f\7~\2\2\u024f\u0250\7~\2\2\u0250\u0090\3\2\2\2\u0251")
        buf.write("\u0253\t\13\2\2\u0252\u0251\3\2\2\2\u0253\u0254\3\2\2")
        buf.write("\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0256")
        buf.write("\3\2\2\2\u0256\u0257\bI\7\2\u0257\u0092\3\2\2\2\u0258")
        buf.write("\u025d\7$\2\2\u0259\u025c\n\f\2\2\u025a\u025c\5I%\2\u025b")
        buf.write("\u0259\3\2\2\2\u025b\u025a\3\2\2\2\u025c\u025f\3\2\2\2")
        buf.write("\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0261\3")
        buf.write("\2\2\2\u025f\u025d\3\2\2\2\u0260\u0262\t\r\2\2\u0261\u0260")
        buf.write("\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264\bJ\b\2\u0264")
        buf.write("\u0094\3\2\2\2\u0265\u026a\7$\2\2\u0266\u0269\n\f\2\2")
        buf.write("\u0267\u0269\5I%\2\u0268\u0266\3\2\2\2\u0268\u0267\3\2")
        buf.write("\2\2\u0269\u026c\3\2\2\2\u026a\u0268\3\2\2\2\u026a\u026b")
        buf.write("\3\2\2\2\u026b\u026d\3\2\2\2\u026c\u026a\3\2\2\2\u026d")
        buf.write("\u026e\7^\2\2\u026e\u026f\n\16\2\2\u026f\u0270\bK\t\2")
        buf.write("\u0270\u0096\3\2\2\2\u0271\u0272\13\2\2\2\u0272\u0273")
        buf.write("\bL\n\2\u0273\u0098\3\2\2\2 \2\u0116\u0121\u0124\u01a5")
        buf.write("\u01ad\u01b1\u01b6\u01b8\u01c2\u01ca\u01cf\u01d6\u01d9")
        buf.write("\u01df\u01e3\u01e8\u0208\u0212\u0219\u021d\u0224\u0226")
        buf.write("\u022d\u0254\u025b\u025d\u0261\u0268\u026a\13\3#\2\3$")
        buf.write("\3\3&\4\3&\5\3\66\6\b\2\2\3J\7\3K\b\3L\t")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    Comment = 11
    Inttype = 12
    Floattype = 13
    Stringtype = 14
    Booleantype = 15
    Autotype = 16
    Breakkey = 17
    Dokey = 18
    Else = 19
    Trueboolean = 20
    Falseboolean = 21
    Functionkey = 22
    Forkey = 23
    Ifkey = 24
    Returnkey = 25
    Whilekey = 26
    Voidtype = 27
    Outkey = 28
    Continuekey = 29
    Arraytype = 30
    Inheritkey = 31
    Ofkey = 32
    Identifiers = 33
    Int = 34
    String = 35
    FLOAT = 36
    LB = 37
    RB = 38
    DOT = 39
    COMMA = 40
    SEMI = 41
    COLON = 42
    LCB = 43
    RCB = 44
    LSB = 45
    RSB = 46
    ASS = 47
    Stringopr = 48
    Array = 49
    PLUS = 50
    MULT = 51
    DIV = 52
    MOD = 53
    NOT = 54
    MINUS = 55
    EQUAL = 56
    NOT_EQUAL = 57
    GT = 58
    LT = 59
    GTE = 60
    LTE = 61
    LOGICAL_AND = 62
    LOGICAL_OR = 63
    WS = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'integer'", "'float'", "'string'", 
            "'boolean'", "'auto'", "'break'", "'do'", "'else'", "'true'", 
            "'false'", "'function'", "'for'", "'if'", "'return'", "'while'", 
            "'void'", "'out'", "'continue'", "'array'", "'inherit'", "'of'", 
            "'('", "')'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'['", 
            "']'", "'='", "'::'", "'+'", "'*'", "'/'", "'%'", "'!'", "'-'", 
            "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>",
            "Comment", "Inttype", "Floattype", "Stringtype", "Booleantype", 
            "Autotype", "Breakkey", "Dokey", "Else", "Trueboolean", "Falseboolean", 
            "Functionkey", "Forkey", "Ifkey", "Returnkey", "Whilekey", "Voidtype", 
            "Outkey", "Continuekey", "Arraytype", "Inheritkey", "Ofkey", 
            "Identifiers", "Int", "String", "FLOAT", "LB", "RB", "DOT", 
            "COMMA", "SEMI", "COLON", "LCB", "RCB", "LSB", "RSB", "ASS", 
            "Stringopr", "Array", "PLUS", "MULT", "DIV", "MOD", "NOT", "MINUS", 
            "EQUAL", "NOT_EQUAL", "GT", "LT", "GTE", "LTE", "LOGICAL_AND", 
            "LOGICAL_OR", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "Comment", "Inttype", "Floattype", 
                  "Stringtype", "Booleantype", "Autotype", "Breakkey", "Dokey", 
                  "Else", "Trueboolean", "Falseboolean", "Functionkey", 
                  "Forkey", "Ifkey", "Returnkey", "Whilekey", "Voidtype", 
                  "Outkey", "Continuekey", "Arraytype", "Inheritkey", "Ofkey", 
                  "Identifiers", "Int", "String", "Escape_sequence", "FLOAT", 
                  "INTEGER_PART", "DECIMAL_PART", "EXPONENT_PART", "LB", 
                  "RB", "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "LSB", 
                  "RSB", "ASS", "Stringopr", "Array", "Stringlist", "Intlist", 
                  "Booleanlist", "Floatlist", "PLUS", "MULT", "DIV", "MOD", 
                  "NOT", "MINUS", "EQUAL", "NOT_EQUAL", "GT", "LT", "GTE", 
                  "LTE", "LOGICAL_AND", "LOGICAL_OR", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[33] = self.Int_action 
            actions[34] = self.String_action 
            actions[36] = self.FLOAT_action 
            actions[52] = self.Array_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def Int_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def String_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

        if actionIndex == 3:
            self.text = self.text.replace("_","")
     

    def Array_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace("_","")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	temp=str(self.text)
            	impossible='\n'
            	if temp[-1] in impossible:
            		raise UncloseString(temp[1:-1])
            	else:
            		raise UncloseString(temp[1:])


     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	raise IllegalEscape(str(self.text[1:]))

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


