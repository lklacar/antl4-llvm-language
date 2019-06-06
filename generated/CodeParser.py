# Generated from /home/luka/Projects/antl4-llvm-language/Code.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3\27\n\3\f\3\16\3\32")
        buf.write("\13\3\3\3\5\3\35\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\7\3(\n\3\f\3\16\3+\13\3\3\4\3\4\5\4/\n\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\2\3\4\b\2\4\6\b\n\f\2\5\3\2\7\b\3\2")
        buf.write("\t\n\3\2\13\r\2\66\2\16\3\2\2\2\4\34\3\2\2\2\6.\3\2\2")
        buf.write("\2\b\60\3\2\2\2\n\62\3\2\2\2\f\64\3\2\2\2\16\17\5\4\3")
        buf.write("\2\17\3\3\2\2\2\20\21\b\3\1\2\21\22\7\5\2\2\22\23\5\4")
        buf.write("\3\2\23\24\7\6\2\2\24\35\3\2\2\2\25\27\t\2\2\2\26\25\3")
        buf.write("\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\33")
        buf.write("\3\2\2\2\32\30\3\2\2\2\33\35\5\6\4\2\34\20\3\2\2\2\34")
        buf.write("\30\3\2\2\2\35)\3\2\2\2\36\37\f\7\2\2\37 \7\17\2\2 (\5")
        buf.write("\4\3\b!\"\f\6\2\2\"#\t\3\2\2#(\5\4\3\7$%\f\5\2\2%&\t\2")
        buf.write("\2\2&(\5\4\3\6\'\36\3\2\2\2\'!\3\2\2\2\'$\3\2\2\2(+\3")
        buf.write("\2\2\2)\'\3\2\2\2)*\3\2\2\2*\5\3\2\2\2+)\3\2\2\2,/\5\b")
        buf.write("\5\2-/\5\n\6\2.,\3\2\2\2.-\3\2\2\2/\7\3\2\2\2\60\61\7")
        buf.write("\4\2\2\61\t\3\2\2\2\62\63\7\3\2\2\63\13\3\2\2\2\64\65")
        buf.write("\t\4\2\2\65\r\3\2\2\2\7\30\34\').")
        return buf.getvalue()


class CodeParser ( Parser ):

    grammarFileName = "Code.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'='", "'.'", 
                     "'^'" ]

    symbolicNames = [ "<INVALID>", "VARIABLE", "SCIENTIFIC_NUMBER", "LPAREN", 
                      "RPAREN", "PLUS", "MINUS", "TIMES", "DIV", "GT", "LT", 
                      "EQ", "POINT", "POW", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_file = 0
    RULE_expression = 1
    RULE_atom = 2
    RULE_scientific = 3
    RULE_variable = 4
    RULE_relop = 5

    ruleNames =  [ "file", "expression", "atom", "scientific", "variable", 
                   "relop" ]

    EOF = Token.EOF
    VARIABLE=1
    SCIENTIFIC_NUMBER=2
    LPAREN=3
    RPAREN=4
    PLUS=5
    MINUS=6
    TIMES=7
    DIV=8
    GT=9
    LT=10
    EQ=11
    POINT=12
    POW=13
    WS=14
    COMMENT=15
    LINE_COMMENT=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CodeParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file(self):

        localctx = CodeParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.expression(0)
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

        def LPAREN(self):
            return self.getToken(CodeParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CodeParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(CodeParser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(CodeParser.AtomContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CodeParser.PLUS)
            else:
                return self.getToken(CodeParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CodeParser.MINUS)
            else:
                return self.getToken(CodeParser.MINUS, i)

        def POW(self):
            return self.getToken(CodeParser.POW, 0)

        def TIMES(self):
            return self.getToken(CodeParser.TIMES, 0)

        def DIV(self):
            return self.getToken(CodeParser.DIV, 0)

        def getRuleIndex(self):
            return CodeParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CodeParser.LPAREN]:
                self.state = 15
                self.match(CodeParser.LPAREN)
                self.state = 16
                self.expression(0)
                self.state = 17
                self.match(CodeParser.RPAREN)
                pass
            elif token in [CodeParser.VARIABLE, CodeParser.SCIENTIFIC_NUMBER, CodeParser.PLUS, CodeParser.MINUS]:
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CodeParser.PLUS or _la==CodeParser.MINUS:
                    self.state = 19
                    _la = self._input.LA(1)
                    if not(_la==CodeParser.PLUS or _la==CodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 25
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 28
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 29
                        self.match(CodeParser.POW)
                        self.state = 30
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = CodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 31
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 32
                        _la = self._input.LA(1)
                        if not(_la==CodeParser.TIMES or _la==CodeParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = CodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 34
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 35
                        _la = self._input.LA(1)
                        if not(_la==CodeParser.PLUS or _la==CodeParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        self.expression(4)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scientific(self):
            return self.getTypedRuleContext(CodeParser.ScientificContext,0)


        def variable(self):
            return self.getTypedRuleContext(CodeParser.VariableContext,0)


        def getRuleIndex(self):
            return CodeParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = CodeParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CodeParser.SCIENTIFIC_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.scientific()
                pass
            elif token in [CodeParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.variable()
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


    class ScientificContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCIENTIFIC_NUMBER(self):
            return self.getToken(CodeParser.SCIENTIFIC_NUMBER, 0)

        def getRuleIndex(self):
            return CodeParser.RULE_scientific

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScientific" ):
                listener.enterScientific(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScientific" ):
                listener.exitScientific(self)




    def scientific(self):

        localctx = CodeParser.ScientificContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_scientific)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(CodeParser.SCIENTIFIC_NUMBER)
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

        def VARIABLE(self):
            return self.getToken(CodeParser.VARIABLE, 0)

        def getRuleIndex(self):
            return CodeParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = CodeParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(CodeParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(CodeParser.EQ, 0)

        def GT(self):
            return self.getToken(CodeParser.GT, 0)

        def LT(self):
            return self.getToken(CodeParser.LT, 0)

        def getRuleIndex(self):
            return CodeParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)




    def relop(self):

        localctx = CodeParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CodeParser.GT) | (1 << CodeParser.LT) | (1 << CodeParser.EQ))) != 0)):
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
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




