# Generated from grammarJava.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,4,0,27,8,0,
        11,0,12,0,28,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,3,2,41,8,
        2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,49,8,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        5,4,58,8,4,10,4,12,4,61,9,4,1,5,1,5,1,6,1,6,3,6,67,8,6,4,6,69,8,
        6,11,6,12,6,70,1,7,1,7,1,7,3,7,76,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,3,9,85,8,9,1,9,1,9,1,9,5,9,90,8,9,10,9,12,9,93,9,9,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,11,0,1,18,12,0,2,4,6,8,10,12,14,16,
        18,20,22,0,2,1,0,4,5,1,0,6,9,102,0,26,1,0,0,0,2,30,1,0,0,0,4,37,
        1,0,0,0,6,44,1,0,0,0,8,54,1,0,0,0,10,62,1,0,0,0,12,68,1,0,0,0,14,
        75,1,0,0,0,16,77,1,0,0,0,18,84,1,0,0,0,20,94,1,0,0,0,22,97,1,0,0,
        0,24,27,3,6,3,0,25,27,3,2,1,0,26,24,1,0,0,0,26,25,1,0,0,0,27,28,
        1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,1,1,0,0,0,30,31,5,3,0,0,31,
        32,5,12,0,0,32,33,3,4,2,0,33,35,5,13,0,0,34,36,5,18,0,0,35,34,1,
        0,0,0,35,36,1,0,0,0,36,3,1,0,0,0,37,38,5,4,0,0,38,40,5,12,0,0,39,
        41,3,8,4,0,40,39,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,5,13,
        0,0,43,5,1,0,0,0,44,45,5,1,0,0,45,46,5,4,0,0,46,48,5,12,0,0,47,49,
        3,8,4,0,48,47,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,51,5,13,0,0,
        51,52,5,14,0,0,52,53,3,12,6,0,53,7,1,0,0,0,54,59,3,10,5,0,55,56,
        5,15,0,0,56,58,3,10,5,0,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,
        0,59,60,1,0,0,0,60,9,1,0,0,0,61,59,1,0,0,0,62,63,7,0,0,0,63,11,1,
        0,0,0,64,66,3,14,7,0,65,67,5,18,0,0,66,65,1,0,0,0,66,67,1,0,0,0,
        67,69,1,0,0,0,68,64,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,
        0,0,0,71,13,1,0,0,0,72,76,3,16,8,0,73,76,3,20,10,0,74,76,3,22,11,
        0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,15,1,0,0,0,77,78,
        5,4,0,0,78,79,5,10,0,0,79,80,3,18,9,0,80,17,1,0,0,0,81,82,6,9,-1,
        0,82,85,5,4,0,0,83,85,5,5,0,0,84,81,1,0,0,0,84,83,1,0,0,0,85,91,
        1,0,0,0,86,87,10,1,0,0,87,88,7,1,0,0,88,90,3,18,9,2,89,86,1,0,0,
        0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,19,1,0,0,0,93,91,
        1,0,0,0,94,95,5,2,0,0,95,96,3,18,9,0,96,21,1,0,0,0,97,98,5,3,0,0,
        98,99,5,12,0,0,99,100,3,18,9,0,100,101,5,13,0,0,101,23,1,0,0,0,11,
        26,28,35,40,48,59,66,70,75,84,91
    ]

class grammarJavaParser ( Parser ):

    grammarFileName = "grammarJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'='", "'=='", 
                     "'('", "')'", "':'", "','", "' '", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "IDCLASS", 
                      "NUMBERS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                      "ASIGNAN", "EQUAL", "LPAREN", "RPAREN", "COLON", "COMMA", 
                      "BLANKSPACE", "TAB", "RCAR" ]

    RULE_program = 0
    RULE_print = 1
    RULE_callfunction = 2
    RULE_function = 3
    RULE_parameters = 4
    RULE_parameter = 5
    RULE_block = 6
    RULE_statement = 7
    RULE_assignment = 8
    RULE_expression = 9
    RULE_returnStmt = 10
    RULE_printStmt = 11

    ruleNames =  [ "program", "print", "callfunction", "function", "parameters", 
                   "parameter", "block", "statement", "assignment", "expression", 
                   "returnStmt", "printStmt" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    IDCLASS=4
    NUMBERS=5
    PLUS=6
    MINUS=7
    MULTIPLY=8
    DIVIDE=9
    ASIGNAN=10
    EQUAL=11
    LPAREN=12
    RPAREN=13
    COLON=14
    COMMA=15
    BLANKSPACE=16
    TAB=17
    RCAR=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarJavaParser.FunctionContext)
            else:
                return self.getTypedRuleContext(grammarJavaParser.FunctionContext,i)


        def print_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarJavaParser.PrintContext)
            else:
                return self.getTypedRuleContext(grammarJavaParser.PrintContext,i)


        def getRuleIndex(self):
            return grammarJavaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = grammarJavaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 24
                    self.function()
                    pass
                elif token in [3]:
                    self.state = 25
                    self.print_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(grammarJavaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(grammarJavaParser.LPAREN, 0)

        def callfunction(self):
            return self.getTypedRuleContext(grammarJavaParser.CallfunctionContext,0)


        def RPAREN(self):
            return self.getToken(grammarJavaParser.RPAREN, 0)

        def RCAR(self):
            return self.getToken(grammarJavaParser.RCAR, 0)

        def getRuleIndex(self):
            return grammarJavaParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = grammarJavaParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(grammarJavaParser.PRINT)
            self.state = 31
            self.match(grammarJavaParser.LPAREN)
            self.state = 32
            self.callfunction()
            self.state = 33
            self.match(grammarJavaParser.RPAREN)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 34
                self.match(grammarJavaParser.RCAR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallfunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDCLASS(self):
            return self.getToken(grammarJavaParser.IDCLASS, 0)

        def LPAREN(self):
            return self.getToken(grammarJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(grammarJavaParser.RPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(grammarJavaParser.ParametersContext,0)


        def getRuleIndex(self):
            return grammarJavaParser.RULE_callfunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallfunction" ):
                listener.enterCallfunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallfunction" ):
                listener.exitCallfunction(self)




    def callfunction(self):

        localctx = grammarJavaParser.CallfunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_callfunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(grammarJavaParser.IDCLASS)
            self.state = 38
            self.match(grammarJavaParser.LPAREN)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==5:
                self.state = 39
                self.parameters()


            self.state = 42
            self.match(grammarJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(grammarJavaParser.DEF, 0)

        def IDCLASS(self):
            return self.getToken(grammarJavaParser.IDCLASS, 0)

        def LPAREN(self):
            return self.getToken(grammarJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(grammarJavaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(grammarJavaParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(grammarJavaParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(grammarJavaParser.ParametersContext,0)


        def getRuleIndex(self):
            return grammarJavaParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = grammarJavaParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(grammarJavaParser.DEF)
            self.state = 45
            self.match(grammarJavaParser.IDCLASS)
            self.state = 46
            self.match(grammarJavaParser.LPAREN)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==5:
                self.state = 47
                self.parameters()


            self.state = 50
            self.match(grammarJavaParser.RPAREN)
            self.state = 51
            self.match(grammarJavaParser.COLON)
            self.state = 52
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarJavaParser.ParameterContext)
            else:
                return self.getTypedRuleContext(grammarJavaParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarJavaParser.COMMA)
            else:
                return self.getToken(grammarJavaParser.COMMA, i)

        def getRuleIndex(self):
            return grammarJavaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = grammarJavaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.parameter()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 55
                self.match(grammarJavaParser.COMMA)
                self.state = 56
                self.parameter()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDCLASS(self):
            return self.getToken(grammarJavaParser.IDCLASS, 0)

        def NUMBERS(self):
            return self.getToken(grammarJavaParser.NUMBERS, 0)

        def getRuleIndex(self):
            return grammarJavaParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = grammarJavaParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarJavaParser.StatementContext,i)


        def RCAR(self, i:int=None):
            if i is None:
                return self.getTokens(grammarJavaParser.RCAR)
            else:
                return self.getToken(grammarJavaParser.RCAR, i)

        def getRuleIndex(self):
            return grammarJavaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = grammarJavaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 64
                    self.statement()
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==18:
                        self.state = 65
                        self.match(grammarJavaParser.RCAR)



                else:
                    raise NoViableAltException(self)
                self.state = 70 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(grammarJavaParser.AssignmentContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(grammarJavaParser.ReturnStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(grammarJavaParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return grammarJavaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = grammarJavaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.assignment()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.returnStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.printStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDCLASS(self):
            return self.getToken(grammarJavaParser.IDCLASS, 0)

        def ASIGNAN(self):
            return self.getToken(grammarJavaParser.ASIGNAN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return grammarJavaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = grammarJavaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(grammarJavaParser.IDCLASS)
            self.state = 78
            self.match(grammarJavaParser.ASIGNAN)
            self.state = 79
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDCLASS(self):
            return self.getToken(grammarJavaParser.IDCLASS, 0)

        def NUMBERS(self):
            return self.getToken(grammarJavaParser.NUMBERS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grammarJavaParser.ExpressionContext,i)


        def PLUS(self):
            return self.getToken(grammarJavaParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(grammarJavaParser.MINUS, 0)

        def DIVIDE(self):
            return self.getToken(grammarJavaParser.DIVIDE, 0)

        def MULTIPLY(self):
            return self.getToken(grammarJavaParser.MULTIPLY, 0)

        def getRuleIndex(self):
            return grammarJavaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grammarJavaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 82
                self.match(grammarJavaParser.IDCLASS)
                pass
            elif token in [5]:
                self.state = 83
                self.match(grammarJavaParser.NUMBERS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = grammarJavaParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 86
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 87
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 88
                    self.expression(2) 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(grammarJavaParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return grammarJavaParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = grammarJavaParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(grammarJavaParser.RETURN)
            self.state = 95
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(grammarJavaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(grammarJavaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarJavaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return grammarJavaParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)




    def printStmt(self):

        localctx = grammarJavaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(grammarJavaParser.PRINT)
            self.state = 98
            self.match(grammarJavaParser.LPAREN)
            self.state = 99
            self.expression(0)
            self.state = 100
            self.match(grammarJavaParser.RPAREN)
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
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




