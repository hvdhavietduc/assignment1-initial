import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_case_1(self):
        input = """/* comment block*/"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 1))

    def test_case_2(self):
        input = """/*comment \n block*/"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 2))

    def test_case_3(self):
        input = """/*alo*//*alo*/"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 3))

    def test_case_4(self):
        input = """/*how //are you*/"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 4))

    def test_case_5(self):
        input = """//nguyenleminhbao"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 5))

    
    def test_case_6(self):
        """testcase 6""" 
        input ="""Counter_1"""
        expect ="""Counter_1,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 6))
    def test_case_7(self):
        """testcase 7""" 
        input ="""invalid-identifier"""
        expect ="""invalid,-,identifier,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 7))
    def test_case_8(self):
        """testcase 8""" 
        input ="""0"""
        expect ="""0,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 8))
    def test_case_9(self):
        """testcase 9""" 
        input ="""123"""
        expect ="""123,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 9))
    def test_case_10(self):
        """testcase 10""" 
        input ="""1_234"""
        expect ="""1234,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 10))
    def test_case_11(self):
        """testcase 11""" 
        input ="""0_123"""
        expect ="""0,_123,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 11))
    def test_case_12(self):
        """testcase 12""" 
        input ="""1_234_567"""
        expect ="""1234567,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 12))
    def test_case_13(self):
        """testcase 13""" 
        input ="""0.123"""
        expect ="""0.123,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 13))
    def test_case_14(self):
        """testcase 14""" 
        input ="""0.123"""
        expect ="""0.123,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 14))
    def test_case_15(self):
        """testcase 15""" 
        input ="""3.14159265359"""
        expect ="""3.14159265359,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 15))
    def test_case_16(self):
        """testcase 16""" 
        input ="""1e2"""
        expect ="""1e2,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 16))
    def test_case_17(self):
        """testcase 17""" 
        input ="""2.5e-1"""
        expect ="""2.5e-1,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 17))
    def test_case_18(self):
        """testcase 18""" 
        input ="""1_000e+10"""
        expect ="""1000e+10,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 18))
    def test_case_19(self):
        """testcase 19""" 
        input ="""0.1_2E3"""
        expect ="""0.1,_2E3,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 19))
    def test_case_20(self):
        """testcase 20""" 
        input ="""5.7e-0_1"""
        expect ="""5.7e-0,_1,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 20))
    def test_case_21(self):
        """testcase 21""" 
        input =""".1e"""
        expect =""".,1,e,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 21))
    def test_case_22(self):
        """testcase 22""" 
        input ="""_1.e2"""
        expect ="""_1,.,e2,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 22))
    def test_case_23(self): 
        """testcase 23""" 
        input ="abc\"" 
        expect ="""abc,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expect, 23))  
    def test_case_24(self): 
        """testcase 24""" 
        input =	""" "hello world" """
        expect ="hello world,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 24))
    def test_case_25(self): 
        """testcase 25""" 
        input =	""" "It's a beautiful day" """
        expect ="It's a beautiful day,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 25))
    def test_case_26(self): 
        """testcase 26""" 
        input =	""" "I am a \\"chatbot\\"" """
        expect ="""I am a \\"chatbot\\",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 26))
    def test_case_27(self): 
        """testcase 27"""   
        input =	""" "\\n\\t\\r" """
        expect ="""\\n\\t\\r,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 27))
    def test_case_28(self): 
        """testcase 28"""     
        input = """ "mixed escape\" sequences: \n\t " """
        expect ="mixed escape,sequences,:,Unclosed String:  "
        self.assertTrue(TestLexer.test(input,expect, 28))
    def test_case_29(self):
        input = "1_000_000.12345"
        expect = """1000000.12345,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 29))

    def test_case_30(self):
        input = "100_000_000.00001e-6"
        expect = """100000000.00001e-6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 30))

    def test_case_31(self):
        input ="0.00000123E-10"
        expect = """0.00000123E-10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 31))

    def test_case_32(self):
        input = """1.234_5E+1_0"""
        expect = """1.234,_5E,+,10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 32))

    def test_case_33(self):
        input = """0.1_2_3_4E-10"""
        expect = """0.1,_2_3_4E,-,10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 33))

    def test_case_34(self):
        input = """1_234_567.8e+9"""
        expect = """1234567.8e+9,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 34))

    def test_case_35(self):
        input = """11."""
        expect = """11.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 35))

    def test_case_36(self):
        input = """3_000.1_23e-4"""
        expect = """3000.1,_23e,-,4,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 36))

    def test_case_37(self):
        input = """123456.7890E-123_4"""
        expect = """123456.7890E-123,_4,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 37))

    def test_case_38(self):
        input = """1_0_0_0_0.1_2_3_4E-1_0"""
        expect = """10000.1,_2_3_4E,-,10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 38))

    def test_case_39(self):
        input = """123."""
        expect = """123.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 39))

    def test_case_40(self):
        input = """1_2.3e4_5"""
        expect = """12.3e4,_5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 40))

    def test_case_41(self):
        input = "Double quote: \""
        expect = """Double,quote,:,Unclosed String: """
        self.assertTrue(TestLexer.test(input, expect, 41))

    def test_case_42(self):
        input = """ "Single quote: '\''"  """
        expect = """Single quote: ''',<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 42))

    def test_case_43(self):
        input = """ "Line 1\nLine 2" """
        expect = """Unclosed String: Line 1\n"""
        self.assertTrue(TestLexer.test(input, expect, 43))

    def test_case_44(self):
        input = """ "Tab:\tTab\t" """
        expect = """Tab:\tTab\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 44))

    def test_case_45(self):
        input = """ "Bell: \a" """
        expect = """Bell: \a,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 45))

    def test_case_46(self):
        input = """ "Form feed: \f" """
        expect = """Form feed: \f,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 46))

    def test_case_47(self):
        input = """ "Carriage return:Return" """
        expect = """Carriage return:Return,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 47))

    def test_case_48(self):
        input = """ "Backspace:\bSpace" """
        expect = """Backspace:\bSpace,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 48))

    def test_case_49(self):
        input = """ "Unicode: \\u2764" """
        expect = """Illegal Escape In String: Unicode: \\u"""
        self.assertTrue(TestLexer.test(input, expect, 49))

    def test_case_50(self):
        input = """ "Unicode: \\u0939\" """
        expect = """Illegal Escape In String: Unicode: \\u"""
        self.assertTrue(TestLexer.test(input, expect, 50))

    def test_case_51(self):
        input = """ "Escaped backslash: \\" """
        expect = """Unclosed String: Escaped backslash: \\" """
        self.assertTrue(TestLexer.test(input, expect, 51))

    def test_case_52(self):
        input = """ "Escaped single quote: '\''" """
        expect = """Escaped single quote: ''',<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 52))

    def test_case_53(self):
        input = """ "Multiple escape characters: \t\n\r" """
        expect = """Unclosed String: Multiple escape characters: \t\n"""
        self.assertTrue(TestLexer.test(input, expect, 53))

    def test_case_54(self):
        input = """ "Multiple lines:\nLine 1\nLine 2\nLine 3" """
        expect = """Unclosed String: Multiple lines:\n"""
        self.assertTrue(TestLexer.test(input, expect, 54))

    def test_case_55(self):
        input = """ "Hexadecimal escape: \\t x" """
        expect = """Hexadecimal escape: \\t x,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 55))

    def test_case_56(self):
        input = """ "Mixed Unicode and escape: \c" """
        expect = """Illegal Escape In String: Mixed Unicode and escape: \c"""
        self.assertTrue(TestLexer.test(input, expect, 56))

    def test_case_57(self):
        input = """ "Multi-line and escapes: \n\t\"Hello, 'world'!\"\\nGoodbye." """
        expect = """Unclosed String: Multi-line and escapes: \n"""
        self.assertTrue(TestLexer.test(input, expect, 57))

    def test_case_58(self):
        input = """ "Octal escape: \064" """
        expect = """Octal escape: 4,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 58))

    def test_case_59(self):
        input = """string"""
        expect = """string,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 59))

    def test_case_60(self):
        input = """ "Unicode plane 2: " """
        expect = """Unicode plane 2: ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 60))

    def test_case_61(self):
        input = """ "" """
        expect = """,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 61))

    def test_case_62(self):
        input = """
        // One
        // True
        /* Three */
        """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 62))

    def test_case_63(self):
        input = """ func: function integer(){}
        }"""
        expect = """func,:,function,integer,(,),{,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 63))

    def test_case_64(self):
        input = """ integer """
        expect = """integer,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 64))

    def test_case_65(self):
        input = """add: function integer (a: integer, b: integer) {
            return a+b;
        }"""
        expect = """add,:,function,integer,(,a,:,integer,,,b,:,integer,),{,return,a,+,b,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 65))

    def test_case_66(self):
        input = """
        a: integer = 1;
        """
        expect = """a,:,integer,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 66))

    def test_case_67(self):
        input = """ a: float = 1; """
        expect = """a,:,float,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 67))

    def test_case_68(self):
        input = """ a: boolean = 1; """
        expect = """a,:,boolean,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 68))

    def test_case_69(self):
        input = """
        printf("I LOVE YOU");"""
        expect = """printf,(,I LOVE YOU,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 69))

    def test_case_70(self):
        input = """ "THAY CHO EM 10 DIEM" """
        expect = """THAY CHO EM 10 DIEM,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 70))

    def test_case_71(self):
        input = """ "THAY CHO EM 10 DIEM integer" """
        expect = """THAY CHO EM 10 DIEM integer,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 71))

    def test_case_72(self):
        input = """ if(n == 0 ) return 1; """
        expect = """if,(,n,==,0,),return,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 72))
    def test_case_73(self):
        input = """// THAY CHO EM 10 DIEM"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 73))

    def test_case_74(self):
        input = """matrix: array [4, 4] of integer = {
            {1, 2, 3, 4}
        };"""
        expect = """matrix,:,array,[,4,,,4,],of,integer,=,{,{,1,,,2,,,3,,,4,},},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 74))

    def test_case_75(self):
        input = """
        printf("bool: %s\n", bool ? "true" : "false");
        printf("string: %s\n", string);"""
        expect = """printf,(,Unclosed String: bool: %s\n"""
        self.assertTrue(TestLexer.test(input, expect, 75))

    def test_case_76(self):
        input = """* + > / %"""
        expect = """*,+,>,/,%,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 76))
  

    def test_case_77(self):
        input = """! && || ?"""
        expect = """!,&&,||,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 77))

    def test_case_78(self):
        input = """== != < > <= >="""
        expect = """==,!=,<,>,<=,>=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 78))


    def test_case_79(self):
        input = """::"""
        expect = """::,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 79))


    def test_case_80(self):
        input = """{ [] }"""
        expect = """{,[,],},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 80))

    def test_case_81(self):
        input = """[ ]"""
        expect = """[,],<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 81))

    def test_case_82(self):
        input = """( {} )"""
        expect = """(,{,},),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 82))

    def test_case_83(self):
        input = ""","""
        expect = """,,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 83))

    def test_case_84(self):
        input = """;"""
        expect = """;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 84))

    def test_case_85(self):
        input = """."""
        expect = """.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 85))

    def test_case_86(self):
        input = """:"""
        expect = """:,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 86))


    def test_case_87(self):
        input = """ "XIN $&@^!\{\}[]#%CHAO" """
        expect = """Illegal Escape In String: XIN $&@^!\{"""
        self.assertTrue(TestLexer.test(input, expect, 87))

    def test_case_88(self):
        input = """ (3 + 4)"""
        expect = """(,3,+,4,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 88))

    def test_case_89(self):
        input = """a && b || c - 1"""
        expect = """a,&&,b,||,c,-,1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 89))

    def test_case_90(self):
        input = """ z > w >="""
        expect = """z,>,w,>=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 90))

    def test_case_91(self):
        input = """(a && b) ? (c - d)"""
        expect = """(,a,&&,b,),Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 91))

    def test_case_92(self):
        input = """if x == y then x = x * y else x ++"""
        expect = """if,x,==,y,then,x,=,x,*,y,else,x,+,+,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 92))

    def test_case_93(self):
        input = """for i = 1 to 10 do print(i)"""
        expect = """for,i,=,1,to,10,do,print,(,i,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 93))

    def test_case_94(self):
        input = """A = 100 // This is a comment"""
        expect = """A,=,100,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 94))

    def test_case_95(self):
        input = """/* THAY CHO\nEM 10 \n*/ DIEM"""
        expect = """DIEM,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 95))

    def test_case_96(self):
        input = """"/* THAY CHO /* EM */ 10 DIEM */"""
        expect = """Unclosed String: /* THAY CHO /* EM */ 10 DIEM */"""
        self.assertTrue(TestLexer.test(input, expect, 96))

    def test_case_97(self):
        input = """ ""THAY CHO EM 10 DIEM """
        expect = """,THAY,CHO,EM,10,DIEM,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 97))

    def test_case_98(self):
        input = """{}"""
        expect = """{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 98))

    def test_case_99(self):
        input = """ /* This is a multiline comment // int z = 20; */  """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 99))

    def test_case_100(self):
        input = """ /* This is a comment that should be ignored */ """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 100))
  
    
    
    
    
    
    
    


    

