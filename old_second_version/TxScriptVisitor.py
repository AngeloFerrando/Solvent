# Generated from TxScript.g4 by ANTLR 4.7.2
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


    # Visit a parse tree produced by TxScriptParser#globalVarsExpr.
    def visitGlobalVarsExpr(self, ctx:TxScriptParser.GlobalVarsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#globalVar.
    def visitGlobalVar(self, ctx:TxScriptParser.GlobalVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#globalMap.
    def visitGlobalMap(self, ctx:TxScriptParser.GlobalMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#mapExpr.
    def visitMapExpr(self, ctx:TxScriptParser.MapExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#firstOrderFormulasExpr.
    def visitFirstOrderFormulasExpr(self, ctx:TxScriptParser.FirstOrderFormulasExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#functionFormula.
    def visitFunctionFormula(self, ctx:TxScriptParser.FunctionFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#tokenijn.
    def visitTokenijn(self, ctx:TxScriptParser.TokenijnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#NEqFormula.
    def visitNEqFormula(self, ctx:TxScriptParser.NEqFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#MultDivEqFormula.
    def visitMultDivEqFormula(self, ctx:TxScriptParser.MultDivEqFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#LessEqFormula.
    def visitLessEqFormula(self, ctx:TxScriptParser.LessEqFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#atomFormula.
    def visitAtomFormula(self, ctx:TxScriptParser.AtomFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#sumFormula.
    def visitSumFormula(self, ctx:TxScriptParser.SumFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#andFormula.
    def visitAndFormula(self, ctx:TxScriptParser.AndFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#atomFormulaN.
    def visitAtomFormulaN(self, ctx:TxScriptParser.AtomFormulaNContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#notFormula.
    def visitNotFormula(self, ctx:TxScriptParser.NotFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#existsFormula.
    def visitExistsFormula(self, ctx:TxScriptParser.ExistsFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#orFormula.
    def visitOrFormula(self, ctx:TxScriptParser.OrFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#groupFormula.
    def visitGroupFormula(self, ctx:TxScriptParser.GroupFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#GreaterEqFormula.
    def visitGreaterEqFormula(self, ctx:TxScriptParser.GreaterEqFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#token0jn.
    def visitToken0jn(self, ctx:TxScriptParser.Token0jnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#SumSubEqFormula.
    def visitSumSubEqFormula(self, ctx:TxScriptParser.SumSubEqFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#forallFormula.
    def visitForallFormula(self, ctx:TxScriptParser.ForallFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#GreaterFormula.
    def visitGreaterFormula(self, ctx:TxScriptParser.GreaterFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#EqFormula.
    def visitEqFormula(self, ctx:TxScriptParser.EqFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#LessFormula.
    def visitLessFormula(self, ctx:TxScriptParser.LessFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#gVarn.
    def visitGVarn(self, ctx:TxScriptParser.GVarnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#impliesFormula.
    def visitImpliesFormula(self, ctx:TxScriptParser.ImpliesFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#proceduresExpr.
    def visitProceduresExpr(self, ctx:TxScriptParser.ProceduresExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#procedureExpr.
    def visitProcedureExpr(self, ctx:TxScriptParser.ProcedureExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#requiresExpr.
    def visitRequiresExpr(self, ctx:TxScriptParser.RequiresExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#requireExpr.
    def visitRequireExpr(self, ctx:TxScriptParser.RequireExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#SumSubEq.
    def visitSumSubEq(self, ctx:TxScriptParser.SumSubEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#constant.
    def visitConstant(self, ctx:TxScriptParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#Wallet.
    def visitWallet(self, ctx:TxScriptParser.WalletContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#GreaterEq.
    def visitGreaterEq(self, ctx:TxScriptParser.GreaterEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#MultDivEq.
    def visitMultDivEq(self, ctx:TxScriptParser.MultDivEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#Eq.
    def visitEq(self, ctx:TxScriptParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#LessEq.
    def visitLessEq(self, ctx:TxScriptParser.LessEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#null.
    def visitNull(self, ctx:TxScriptParser.NullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#variable.
    def visitVariable(self, ctx:TxScriptParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#Greater.
    def visitGreater(self, ctx:TxScriptParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#NEq.
    def visitNEq(self, ctx:TxScriptParser.NEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#map.
    def visitMap(self, ctx:TxScriptParser.MapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#Less.
    def visitLess(self, ctx:TxScriptParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#pArgsExprs.
    def visitPArgsExprs(self, ctx:TxScriptParser.PArgsExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#variableArg.
    def visitVariableArg(self, ctx:TxScriptParser.VariableArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#bodyExprs.
    def visitBodyExprs(self, ctx:TxScriptParser.BodyExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#skipBody.
    def visitSkipBody(self, ctx:TxScriptParser.SkipBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#withdraw.
    def visitWithdraw(self, ctx:TxScriptParser.WithdrawContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#deposit.
    def visitDeposit(self, ctx:TxScriptParser.DepositContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#assignmentBody.
    def visitAssignmentBody(self, ctx:TxScriptParser.AssignmentBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#assignmentBodyMap.
    def visitAssignmentBodyMap(self, ctx:TxScriptParser.AssignmentBodyMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#ifstatement.
    def visitIfstatement(self, ctx:TxScriptParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#numberConstant.
    def visitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#agentOrTokenConstant.
    def visitAgentOrTokenConstant(self, ctx:TxScriptParser.AgentOrTokenConstantContext):
        return self.visitChildren(ctx)



del TxScriptParser