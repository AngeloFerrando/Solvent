from antlr4 import *
from LTLLexer import *
from LTLParser import *
from LTLVisitor import *

class Z3Visitor(LTLVisitor):

    def __init__(self):
        pass

    # Visit a parse tree produced by LTLParser#Evaluation.
    def visitEvaluation(self, ctx:LTLParser.EvaluationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Disjunction.
    def visitDisjunction(self, ctx:LTLParser.DisjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return 'Or(' + left + ', ' + right + ')'


    # Visit a parse tree produced by LTLParser#Implies.
    def visitImplies(self, ctx:LTLParser.ImpliesContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return 'If(' + left + ', ' + right + ')'


    # Visit a parse tree produced by LTLParser#Negation.
    def visitNegation(self, ctx:LTLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Next.
    def visitNext(self, ctx:LTLParser.NextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Eventually.
    def visitEventually(self, ctx:LTLParser.EventuallyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Conjunction.
    def visitConjunction(self, ctx:LTLParser.ConjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return 'And(' + left + ', ' + right + ')'


    # Visit a parse tree produced by LTLParser#Grouping.
    def visitGrouping(self, ctx:LTLParser.GroupingContext):
        return self.visit(ctx.child)


    # Visit a parse tree produced by LTLParser#Always.
    def visitAlways(self, ctx:LTLParser.AlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Release.
    def visitRelease(self, ctx:LTLParser.ReleaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Until.
    def visitUntil(self, ctx:LTLParser.UntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#atomExpr.
    def visitAtomExpr(self, ctx:LTLParser.AtomExprContext):
        ctx.text
