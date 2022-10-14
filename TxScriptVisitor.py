# Generated from TxScript.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TxScriptParser import TxScriptParser
else:
    from TxScriptParser import TxScriptParser

# This class defines a complete generic visitor for a parse tree produced by TxScriptParser.

class TxScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TxScriptParser#contractExpr.
    def visitContractExpr(self, ctx:TxScriptParser.ContractExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#proceduresExpr.
    def visitProceduresExpr(self, ctx:TxScriptParser.ProceduresExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#procedureExpr.
    def visitProcedureExpr(self, ctx:TxScriptParser.ProcedureExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#preconditionsExpr.
    def visitPreconditionsExpr(self, ctx:TxScriptParser.PreconditionsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#LessEq.
    def visitLessEq(self, ctx:TxScriptParser.LessEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#SumSubEq.
    def visitSumSubEq(self, ctx:TxScriptParser.SumSubEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#constant.
    def visitConstant(self, ctx:TxScriptParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#null.
    def visitNull(self, ctx:TxScriptParser.NullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#Wallet.
    def visitWallet(self, ctx:TxScriptParser.WalletContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#variable.
    def visitVariable(self, ctx:TxScriptParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#GreaterEq.
    def visitGreaterEq(self, ctx:TxScriptParser.GreaterEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#Greater.
    def visitGreater(self, ctx:TxScriptParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#NEq.
    def visitNEq(self, ctx:TxScriptParser.NEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#MultDivEq.
    def visitMultDivEq(self, ctx:TxScriptParser.MultDivEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#Eq.
    def visitEq(self, ctx:TxScriptParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#Less.
    def visitLess(self, ctx:TxScriptParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#variableArg.
    def visitVariableArg(self, ctx:TxScriptParser.VariableArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#inputToken.
    def visitInputToken(self, ctx:TxScriptParser.InputTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#sequence.
    def visitSequence(self, ctx:TxScriptParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#ifstatement.
    def visitIfstatement(self, ctx:TxScriptParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#outputToken.
    def visitOutputToken(self, ctx:TxScriptParser.OutputTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#skipBody.
    def visitSkipBody(self, ctx:TxScriptParser.SkipBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#assignmentBody.
    def visitAssignmentBody(self, ctx:TxScriptParser.AssignmentBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#numberConstant.
    def visitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#agentOrTokenConstant.
    def visitAgentOrTokenConstant(self, ctx:TxScriptParser.AgentOrTokenConstantContext):
        return self.visitChildren(ctx)



del TxScriptParser