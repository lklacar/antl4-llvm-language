# Generated from /home/luka/Projects/antl4-llvm-language-rewrite/Code.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\'\n")
        buf.write("\5\3\5\3\5\3\5\5\5,\n\5\3\5\3\5\3\5\7\5\61\n\5\f\5\16")
        buf.write("\5\64\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\7\6B\n\6\f\6\16\6E\13\6\3\7\3\7\3\7\3\7\3\7\3\7\7")
        buf.write("\7M\n\7\f\7\16\7P\13\7\3\7\5\7S\n\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\7\7[\n\7\f\7\16\7^\13\7\3\b\3\b\5\bb\n\b\3\t\3")
        buf.write("\t\3\t\2\4\n\f\n\2\4\6\b\n\f\16\20\2\5\3\2\20\21\3\2\16")
        buf.write("\17\3\2\7\b\2h\2\25\3\2\2\2\4\30\3\2\2\2\6\32\3\2\2\2")
        buf.write("\b\"\3\2\2\2\n\67\3\2\2\2\fR\3\2\2\2\16a\3\2\2\2\20c\3")
        buf.write("\2\2\2\22\24\5\b\5\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23")
        buf.write("\3\2\2\2\25\26\3\2\2\2\26\3\3\2\2\2\27\25\3\2\2\2\30\31")
        buf.write("\5\6\4\2\31\5\3\2\2\2\32\33\5\20\t\2\33\34\7\n\2\2\34")
        buf.write("\35\7\3\2\2\35\36\7\t\2\2\36\37\7\22\2\2\37 \5\f\7\2 ")
        buf.write("!\7\25\2\2!\7\3\2\2\2\"#\7\4\2\2#$\7\n\2\2$&\7\f\2\2%")
        buf.write("\'\5\n\6\2&%\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2(+\7\r\2\2)")
        buf.write("*\7\5\2\2*,\7\t\2\2+)\3\2\2\2+,\3\2\2\2,-\3\2\2\2-\62")
        buf.write("\7\23\2\2.\61\5\4\3\2/\61\5\f\7\2\60.\3\2\2\2\60/\3\2")
        buf.write("\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\65\3")
        buf.write("\2\2\2\64\62\3\2\2\2\65\66\7\24\2\2\66\t\3\2\2\2\678\b")
        buf.write("\6\1\289\7\n\2\29:\7\3\2\2:;\7\t\2\2;C\3\2\2\2<=\f\3\2")
        buf.write("\2=>\7\6\2\2>?\7\n\2\2?@\7\3\2\2@B\7\t\2\2A<\3\2\2\2B")
        buf.write("E\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\13\3\2\2\2EC\3\2\2\2FG")
        buf.write("\b\7\1\2GH\7\f\2\2HI\5\f\7\2IJ\7\r\2\2JS\3\2\2\2KM\t\2")
        buf.write("\2\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2")
        buf.write("PN\3\2\2\2QS\5\16\b\2RF\3\2\2\2RN\3\2\2\2S\\\3\2\2\2T")
        buf.write("U\f\6\2\2UV\t\3\2\2V[\5\f\7\7WX\f\5\2\2XY\t\2\2\2Y[\5")
        buf.write("\f\7\6ZT\3\2\2\2ZW\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2")
        buf.write("\2\2]\r\3\2\2\2^\\\3\2\2\2_b\7\13\2\2`b\7\n\2\2a_\3\2")
        buf.write("\2\2a`\3\2\2\2b\17\3\2\2\2cd\t\4\2\2d\21\3\2\2\2\r\25")
        buf.write("&+\60\62CNRZ\\a")
        return buf.getvalue()


class CodeParser ( Parser ):

    grammarFileName = "Code.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'fn'", "'->'", "','", "'const'", 
                     "'let'", "<INVALID>", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'*'", "'/'", "'+'", "'-'", "'='", "'{'", "'}'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TYPE", "ID", 
                      "Constant", "LPAREN", "RPAREN", "MUL", "DIV", "PLUS", 
                      "MINUS", "EQ", "LBRACKET", "RBRACKET", "SEMI", "WS", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignmentStatement = 2
    RULE_functionDefinition = 3
    RULE_arguments = 4
    RULE_expression = 5
    RULE_atom = 6
    RULE_assignmentType = 7

    ruleNames =  [ "program", "statement", "assignmentStatement", "functionDefinition", 
                   "arguments", "expression", "atom", "assignmentType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    TYPE=7
    ID=8
    Constant=9
    LPAREN=10
    RPAREN=11
    MUL=12
    DIV=13
    PLUS=14
    MINUS=15
    EQ=16
    LBRACKET=17
    RBRACKET=18
    SEMI=19
    WS=20
    COMMENT=21
    LINE_COMMENT=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(CodeParser.FunctionDefinitionContext,i)


        def getRuleIndex(self):
            return CodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = CodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CodeParser.T__1:
                self.state = 16
                self.functionDefinition()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def assignmentStatement(self):
            return self.getTypedRuleContext(CodeParser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return CodeParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.assignmentStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentType(self):
            return self.getTypedRuleContext(CodeParser.AssignmentTypeContext,0)


        def ID(self):
            return self.getToken(CodeParser.ID, 0)

        def TYPE(self):
            return self.getToken(CodeParser.TYPE, 0)

        def EQ(self):
            return self.getToken(CodeParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(CodeParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(CodeParser.SEMI, 0)

        def getRuleIndex(self):
            return CodeParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)




    def assignmentStatement(self):

        localctx = CodeParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.assignmentType()
            self.state = 25
            self.match(CodeParser.ID)
            self.state = 26
            self.match(CodeParser.T__0)
            self.state = 27
            self.match(CodeParser.TYPE)
            self.state = 28
            self.match(CodeParser.EQ)
            self.state = 29
            self.expression(0)
            self.state = 30
            self.match(CodeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CodeParser.RPAREN, 0)

        def LBRACKET(self):
            return self.getToken(CodeParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(CodeParser.RBRACKET, 0)

        def arguments(self):
            return self.getTypedRuleContext(CodeParser.ArgumentsContext,0)


        def TYPE(self):
            return self.getToken(CodeParser.TYPE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(CodeParser.StatementContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CodeParser.ExpressionContext,i)


        def getRuleIndex(self):
            return CodeParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = CodeParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(CodeParser.T__1)
            self.state = 33
            self.match(CodeParser.ID)
            self.state = 34
            self.match(CodeParser.LPAREN)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CodeParser.ID:
                self.state = 35
                self.arguments(0)


            self.state = 38
            self.match(CodeParser.RPAREN)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CodeParser.T__2:
                self.state = 39
                self.match(CodeParser.T__2)
                self.state = 40
                self.match(CodeParser.TYPE)


            self.state = 43
            self.match(CodeParser.LBRACKET)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CodeParser.T__4) | (1 << CodeParser.T__5) | (1 << CodeParser.ID) | (1 << CodeParser.Constant) | (1 << CodeParser.LPAREN) | (1 << CodeParser.PLUS) | (1 << CodeParser.MINUS))) != 0):
                self.state = 46
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CodeParser.T__4, CodeParser.T__5]:
                    self.state = 44
                    self.statement()
                    pass
                elif token in [CodeParser.ID, CodeParser.Constant, CodeParser.LPAREN, CodeParser.PLUS, CodeParser.MINUS]:
                    self.state = 45
                    self.expression(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(CodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CodeParser.ID, 0)

        def TYPE(self):
            return self.getToken(CodeParser.TYPE, 0)

        def arguments(self):
            return self.getTypedRuleContext(CodeParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return CodeParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)



    def arguments(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CodeParser.ArgumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(CodeParser.ID)
            self.state = 55
            self.match(CodeParser.T__0)
            self.state = 56
            self.match(CodeParser.TYPE)
            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CodeParser.ArgumentsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arguments)
                    self.state = 58
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 59
                    self.match(CodeParser.T__3)
                    self.state = 60
                    self.match(CodeParser.ID)
                    self.state = 61
                    self.match(CodeParser.T__0)
                    self.state = 62
                    self.match(CodeParser.TYPE) 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CodeParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExpressionAddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CodeParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(CodeParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(CodeParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionAdd" ):
                listener.enterExpressionAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionAdd" ):
                listener.exitExpressionAdd(self)


    class ExpressionMulContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CodeParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(CodeParser.MUL, 0)
        def DIV(self):
            return self.getToken(CodeParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionMul" ):
                listener.enterExpressionMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionMul" ):
                listener.exitExpressionMul(self)


    class ExpressionNumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionNumber" ):
                listener.enterExpressionNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionNumber" ):
                listener.exitExpressionNumber(self)


    class ExpressionNestedContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CodeParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(CodeParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(CodeParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionNested" ):
                listener.enterExpressionNested(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionNested" ):
                listener.exitExpressionNested(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CodeParser.LPAREN]:
                localctx = CodeParser.ExpressionNestedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                self.match(CodeParser.LPAREN)
                self.state = 70
                self.expression(0)
                self.state = 71
                self.match(CodeParser.RPAREN)
                pass
            elif token in [CodeParser.ID, CodeParser.Constant, CodeParser.PLUS, CodeParser.MINUS]:
                localctx = CodeParser.ExpressionNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CodeParser.PLUS or _la==CodeParser.MINUS:
                    self.state = 73
                    _la = self._input.LA(1)
                    if not(_la==CodeParser.PLUS or _la==CodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 79
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 88
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = CodeParser.ExpressionMulContext(self, CodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 82
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 83
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CodeParser.MUL or _la==CodeParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 84
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = CodeParser.ExpressionAddContext(self, CodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 85
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 86
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CodeParser.PLUS or _la==CodeParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expression(4)
                        pass

             
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            self.op = None # Token

        def Constant(self):
            return self.getToken(CodeParser.Constant, 0)

        def ID(self):
            return self.getToken(CodeParser.ID, 0)

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
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CodeParser.Constant]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                localctx.op = self.match(CodeParser.Constant)
                pass
            elif token in [CodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                localctx.op = self.match(CodeParser.ID)
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


    class AssignmentTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CodeParser.RULE_assignmentType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentType" ):
                listener.enterAssignmentType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentType" ):
                listener.exitAssignmentType(self)




    def assignmentType(self):

        localctx = CodeParser.AssignmentTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignmentType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==CodeParser.T__4 or _la==CodeParser.T__5):
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
        self._predicates[4] = self.arguments_sempred
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arguments_sempred(self, localctx:ArgumentsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




