# Generated from LTL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"")
        buf.write("E\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\5\2\25\n\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2>\n\2\f\2\16\2A\13\2\3\3")
        buf.write("\3\3\3\3\2\3\2\4\2\4\2\r\3\2\3\4\3\2\5\6\3\2\7\b\3\2\t")
        buf.write("\n\3\2\13\f\3\2\r\16\3\2\17\20\3\2\21\22\3\2\31\32\3\2")
        buf.write("\33\34\3\2\35\36\2T\2\24\3\2\2\2\4B\3\2\2\2\6\7\b\2\1")
        buf.write("\2\7\b\t\2\2\2\b\25\5\2\2\25\t\n\t\3\2\2\n\25\5\2\2\24")
        buf.write("\13\f\t\4\2\2\f\25\5\2\2\23\r\16\t\5\2\2\16\25\5\2\2\22")
        buf.write("\17\20\7\37\2\2\20\21\5\2\2\2\21\22\7 \2\2\22\25\3\2\2")
        buf.write("\2\23\25\5\4\3\2\24\6\3\2\2\2\24\t\3\2\2\2\24\13\3\2\2")
        buf.write("\2\24\r\3\2\2\2\24\17\3\2\2\2\24\23\3\2\2\2\25?\3\2\2")
        buf.write("\2\26\27\f\21\2\2\27\30\t\6\2\2\30>\5\2\2\22\31\32\f\20")
        buf.write("\2\2\32\33\t\7\2\2\33>\5\2\2\21\34\35\f\17\2\2\35\36\t")
        buf.write("\b\2\2\36>\5\2\2\20\37 \f\16\2\2 !\t\t\2\2!>\5\2\2\17")
        buf.write("\"#\f\r\2\2#$\7\23\2\2$>\5\2\2\16%&\f\f\2\2&\'\7\24\2")
        buf.write("\2\'>\5\2\2\r()\f\13\2\2)*\7\25\2\2*>\5\2\2\f+,\f\n\2")
        buf.write("\2,-\7\26\2\2->\5\2\2\13./\f\t\2\2/\60\7\27\2\2\60>\5")
        buf.write("\2\2\n\61\62\f\b\2\2\62\63\7\30\2\2\63>\5\2\2\t\64\65")
        buf.write("\f\7\2\2\65\66\t\n\2\2\66>\5\2\2\b\678\f\6\2\289\t\13")
        buf.write("\2\29>\5\2\2\7:;\f\5\2\2;<\t\f\2\2<>\5\2\2\6=\26\3\2\2")
        buf.write("\2=\31\3\2\2\2=\34\3\2\2\2=\37\3\2\2\2=\"\3\2\2\2=%\3")
        buf.write("\2\2\2=(\3\2\2\2=+\3\2\2\2=.\3\2\2\2=\61\3\2\2\2=\64\3")
        buf.write("\2\2\2=\67\3\2\2\2=:\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2")
        buf.write("\2\2@\3\3\2\2\2A?\3\2\2\2BC\7!\2\2C\5\3\2\2\2\5\24=?")
        return buf.getvalue()


class LTLParser ( Parser ):

    grammarFileName = "LTL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'not'", "'next'", "'X'", "'eventually'", 
                     "'F'", "'always'", "'G'", "'until'", "'U'", "'release'", 
                     "'R'", "'*'", "'/'", "'+'", "'-'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'&&'", "'and'", "'||'", 
                     "'or'", "'->'", "'implies'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ATOM", "WS" ]

    RULE_ltlExpr = 0
    RULE_atomExpr = 1

    ruleNames =  [ "ltlExpr", "atomExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    ATOM=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LtlExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LTLParser.RULE_ltlExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EvaluationContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # AtomExprContext
            self.copyFrom(ctx)

        def atomExpr(self):
            return self.getTypedRuleContext(LTLParser.AtomExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluation" ):
                listener.enterEvaluation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluation" ):
                listener.exitEvaluation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluation" ):
                return visitor.visitEvaluation(self)
            else:
                return visitor.visitChildren(self)


    class SumSubEqContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.op = None # Token
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumSubEq" ):
                listener.enterSumSubEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumSubEq" ):
                listener.exitSumSubEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumSubEq" ):
                return visitor.visitSumSubEq(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class GreaterEqContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterEq" ):
                listener.enterGreaterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterEq" ):
                listener.exitGreaterEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterEq" ):
                return visitor.visitGreaterEq(self)
            else:
                return visitor.visitChildren(self)


    class GroupingContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrouping" ):
                listener.enterGrouping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrouping" ):
                listener.exitGrouping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouping" ):
                return visitor.visitGrouping(self)
            else:
                return visitor.visitChildren(self)


    class MultDivEqContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.op = None # Token
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDivEq" ):
                listener.enterMultDivEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDivEq" ):
                listener.exitMultDivEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultDivEq" ):
                return visitor.visitMultDivEq(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq" ):
                listener.enterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq" ):
                listener.exitEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class LessEqContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessEq" ):
                listener.enterLessEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessEq" ):
                listener.exitLessEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessEq" ):
                return visitor.visitLessEq(self)
            else:
                return visitor.visitChildren(self)


    class DisjunctionContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunction" ):
                return visitor.visitDisjunction(self)
            else:
                return visitor.visitChildren(self)


    class ImpliesContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplies" ):
                listener.enterImplies(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplies" ):
                listener.exitImplies(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplies" ):
                return visitor.visitImplies(self)
            else:
                return visitor.visitChildren(self)


    class NextContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext" ):
                listener.enterNext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext" ):
                listener.exitNext(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext" ):
                return visitor.visitNext(self)
            else:
                return visitor.visitChildren(self)


    class EventuallyContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventually" ):
                listener.enterEventually(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventually" ):
                listener.exitEventually(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventually" ):
                return visitor.visitEventually(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)


    class GreaterContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreater" ):
                listener.enterGreater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreater" ):
                listener.exitGreater(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreater" ):
                return visitor.visitGreater(self)
            else:
                return visitor.visitChildren(self)


    class AlwaysContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.child = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self):
            return self.getTypedRuleContext(LTLParser.LtlExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlways" ):
                listener.enterAlways(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlways" ):
                listener.exitAlways(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlways" ):
                return visitor.visitAlways(self)
            else:
                return visitor.visitChildren(self)


    class NEqContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNEq" ):
                listener.enterNEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNEq" ):
                listener.exitNEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNEq" ):
                return visitor.visitNEq(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess" ):
                listener.enterLess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess" ):
                listener.exitLess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)


    class ReleaseContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelease" ):
                listener.enterRelease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelease" ):
                listener.exitRelease(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelease" ):
                return visitor.visitRelease(self)
            else:
                return visitor.visitChildren(self)


    class UntilContext(LtlExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.LtlExprContext
            super().__init__(parser)
            self.left = None # LtlExprContext
            self.right = None # LtlExprContext
            self.copyFrom(ctx)

        def ltlExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlExprContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntil" ):
                listener.enterUntil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntil" ):
                listener.exitUntil(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntil" ):
                return visitor.visitUntil(self)
            else:
                return visitor.visitChildren(self)



    def ltlExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LTLParser.LtlExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_ltlExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LTLParser.T__0, LTLParser.T__1]:
                localctx = LTLParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                _la = self._input.LA(1)
                if not(_la==LTLParser.T__0 or _la==LTLParser.T__1):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 6
                localctx.child = self.ltlExpr(19)
                pass
            elif token in [LTLParser.T__2, LTLParser.T__3]:
                localctx = LTLParser.NextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==LTLParser.T__2 or _la==LTLParser.T__3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                localctx.child = self.ltlExpr(18)
                pass
            elif token in [LTLParser.T__4, LTLParser.T__5]:
                localctx = LTLParser.EventuallyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                _la = self._input.LA(1)
                if not(_la==LTLParser.T__4 or _la==LTLParser.T__5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 10
                localctx.child = self.ltlExpr(17)
                pass
            elif token in [LTLParser.T__6, LTLParser.T__7]:
                localctx = LTLParser.AlwaysContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                _la = self._input.LA(1)
                if not(_la==LTLParser.T__6 or _la==LTLParser.T__7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 12
                localctx.child = self.ltlExpr(16)
                pass
            elif token in [LTLParser.T__28]:
                localctx = LTLParser.GroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(LTLParser.T__28)
                self.state = 14
                self.ltlExpr(0)
                self.state = 15
                self.match(LTLParser.T__29)
                pass
            elif token in [LTLParser.ATOM]:
                localctx = LTLParser.EvaluationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                localctx.child = self.atomExpr()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LTLParser.UntilContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 20
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 21
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__8 or _la==LTLParser.T__9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        localctx.right = self.ltlExpr(16)
                        pass

                    elif la_ == 2:
                        localctx = LTLParser.ReleaseContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 23
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 24
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__10 or _la==LTLParser.T__11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        localctx.right = self.ltlExpr(15)
                        pass

                    elif la_ == 3:
                        localctx = LTLParser.MultDivEqContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 26
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 27
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__12 or _la==LTLParser.T__13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        localctx.right = self.ltlExpr(14)
                        pass

                    elif la_ == 4:
                        localctx = LTLParser.SumSubEqContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 29
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 30
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__14 or _la==LTLParser.T__15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        localctx.right = self.ltlExpr(13)
                        pass

                    elif la_ == 5:
                        localctx = LTLParser.EqContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 32
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")

                        self.state = 33
                        self.match(LTLParser.T__16)
                        self.state = 34
                        localctx.right = self.ltlExpr(12)
                        pass

                    elif la_ == 6:
                        localctx = LTLParser.NEqContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 35
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")

                        self.state = 36
                        self.match(LTLParser.T__17)
                        self.state = 37
                        localctx.right = self.ltlExpr(11)
                        pass

                    elif la_ == 7:
                        localctx = LTLParser.LessContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 38
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")

                        self.state = 39
                        self.match(LTLParser.T__18)
                        self.state = 40
                        localctx.right = self.ltlExpr(10)
                        pass

                    elif la_ == 8:
                        localctx = LTLParser.GreaterContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 41
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")

                        self.state = 42
                        self.match(LTLParser.T__19)
                        self.state = 43
                        localctx.right = self.ltlExpr(9)
                        pass

                    elif la_ == 9:
                        localctx = LTLParser.LessEqContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 44
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")

                        self.state = 45
                        self.match(LTLParser.T__20)
                        self.state = 46
                        localctx.right = self.ltlExpr(8)
                        pass

                    elif la_ == 10:
                        localctx = LTLParser.GreaterEqContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 47
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")

                        self.state = 48
                        self.match(LTLParser.T__21)
                        self.state = 49
                        localctx.right = self.ltlExpr(7)
                        pass

                    elif la_ == 11:
                        localctx = LTLParser.ConjunctionContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 50
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 51
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__22 or _la==LTLParser.T__23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        localctx.right = self.ltlExpr(6)
                        pass

                    elif la_ == 12:
                        localctx = LTLParser.DisjunctionContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 53
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 54
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__24 or _la==LTLParser.T__25):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        localctx.right = self.ltlExpr(5)
                        pass

                    elif la_ == 13:
                        localctx = LTLParser.ImpliesContext(self, LTLParser.LtlExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltlExpr)
                        self.state = 56
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 57
                        _la = self._input.LA(1)
                        if not(_la==LTLParser.T__26 or _la==LTLParser.T__27):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        localctx.right = self.ltlExpr(4)
                        pass

             
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATOM(self):
            return self.getToken(LTLParser.ATOM, 0)

        def getRuleIndex(self):
            return LTLParser.RULE_atomExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)




    def atomExpr(self):

        localctx = LTLParser.AtomExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atomExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(LTLParser.ATOM)
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
        self._predicates[0] = self.ltlExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def ltlExpr_sempred(self, localctx:LtlExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         




