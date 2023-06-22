# Generated from TxScript.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TxScriptParser import TxScriptParser
else:
    from TxScriptParser import TxScriptParser

# This class defines a complete listener for a parse tree produced by TxScriptParser.
class TxScriptListener(ParseTreeListener):

    # Enter a parse tree produced by TxScriptParser#contractExpr.
    def enterContractExpr(self, ctx:TxScriptParser.ContractExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#contractExpr.
    def exitContractExpr(self, ctx:TxScriptParser.ContractExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#globalVarsExpr.
    def enterGlobalVarsExpr(self, ctx:TxScriptParser.GlobalVarsExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#globalVarsExpr.
    def exitGlobalVarsExpr(self, ctx:TxScriptParser.GlobalVarsExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#globalVarExpr.
    def enterGlobalVarExpr(self, ctx:TxScriptParser.GlobalVarExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#globalVarExpr.
    def exitGlobalVarExpr(self, ctx:TxScriptParser.GlobalVarExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#firstOrderFormulasExpr.
    def enterFirstOrderFormulasExpr(self, ctx:TxScriptParser.FirstOrderFormulasExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#firstOrderFormulasExpr.
    def exitFirstOrderFormulasExpr(self, ctx:TxScriptParser.FirstOrderFormulasExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#functionFormula.
    def enterFunctionFormula(self, ctx:TxScriptParser.FunctionFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#functionFormula.
    def exitFunctionFormula(self, ctx:TxScriptParser.FunctionFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#tokenijn.
    def enterTokenijn(self, ctx:TxScriptParser.TokenijnContext):
        pass

    # Exit a parse tree produced by TxScriptParser#tokenijn.
    def exitTokenijn(self, ctx:TxScriptParser.TokenijnContext):
        pass


    # Enter a parse tree produced by TxScriptParser#NEqFormula.
    def enterNEqFormula(self, ctx:TxScriptParser.NEqFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#NEqFormula.
    def exitNEqFormula(self, ctx:TxScriptParser.NEqFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#MultDivEqFormula.
    def enterMultDivEqFormula(self, ctx:TxScriptParser.MultDivEqFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#MultDivEqFormula.
    def exitMultDivEqFormula(self, ctx:TxScriptParser.MultDivEqFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#LessEqFormula.
    def enterLessEqFormula(self, ctx:TxScriptParser.LessEqFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#LessEqFormula.
    def exitLessEqFormula(self, ctx:TxScriptParser.LessEqFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#atomFormula.
    def enterAtomFormula(self, ctx:TxScriptParser.AtomFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#atomFormula.
    def exitAtomFormula(self, ctx:TxScriptParser.AtomFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#sumFormula.
    def enterSumFormula(self, ctx:TxScriptParser.SumFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#sumFormula.
    def exitSumFormula(self, ctx:TxScriptParser.SumFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#andFormula.
    def enterAndFormula(self, ctx:TxScriptParser.AndFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#andFormula.
    def exitAndFormula(self, ctx:TxScriptParser.AndFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#atomFormulaN.
    def enterAtomFormulaN(self, ctx:TxScriptParser.AtomFormulaNContext):
        pass

    # Exit a parse tree produced by TxScriptParser#atomFormulaN.
    def exitAtomFormulaN(self, ctx:TxScriptParser.AtomFormulaNContext):
        pass


    # Enter a parse tree produced by TxScriptParser#notFormula.
    def enterNotFormula(self, ctx:TxScriptParser.NotFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#notFormula.
    def exitNotFormula(self, ctx:TxScriptParser.NotFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#existsFormula.
    def enterExistsFormula(self, ctx:TxScriptParser.ExistsFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#existsFormula.
    def exitExistsFormula(self, ctx:TxScriptParser.ExistsFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#orFormula.
    def enterOrFormula(self, ctx:TxScriptParser.OrFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#orFormula.
    def exitOrFormula(self, ctx:TxScriptParser.OrFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#groupFormula.
    def enterGroupFormula(self, ctx:TxScriptParser.GroupFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#groupFormula.
    def exitGroupFormula(self, ctx:TxScriptParser.GroupFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#GreaterEqFormula.
    def enterGreaterEqFormula(self, ctx:TxScriptParser.GreaterEqFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#GreaterEqFormula.
    def exitGreaterEqFormula(self, ctx:TxScriptParser.GreaterEqFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#token0jn.
    def enterToken0jn(self, ctx:TxScriptParser.Token0jnContext):
        pass

    # Exit a parse tree produced by TxScriptParser#token0jn.
    def exitToken0jn(self, ctx:TxScriptParser.Token0jnContext):
        pass


    # Enter a parse tree produced by TxScriptParser#SumSubEqFormula.
    def enterSumSubEqFormula(self, ctx:TxScriptParser.SumSubEqFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#SumSubEqFormula.
    def exitSumSubEqFormula(self, ctx:TxScriptParser.SumSubEqFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#forallFormula.
    def enterForallFormula(self, ctx:TxScriptParser.ForallFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#forallFormula.
    def exitForallFormula(self, ctx:TxScriptParser.ForallFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#GreaterFormula.
    def enterGreaterFormula(self, ctx:TxScriptParser.GreaterFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#GreaterFormula.
    def exitGreaterFormula(self, ctx:TxScriptParser.GreaterFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#EqFormula.
    def enterEqFormula(self, ctx:TxScriptParser.EqFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#EqFormula.
    def exitEqFormula(self, ctx:TxScriptParser.EqFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#LessFormula.
    def enterLessFormula(self, ctx:TxScriptParser.LessFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#LessFormula.
    def exitLessFormula(self, ctx:TxScriptParser.LessFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#gVarn.
    def enterGVarn(self, ctx:TxScriptParser.GVarnContext):
        pass

    # Exit a parse tree produced by TxScriptParser#gVarn.
    def exitGVarn(self, ctx:TxScriptParser.GVarnContext):
        pass


    # Enter a parse tree produced by TxScriptParser#impliesFormula.
    def enterImpliesFormula(self, ctx:TxScriptParser.ImpliesFormulaContext):
        pass

    # Exit a parse tree produced by TxScriptParser#impliesFormula.
    def exitImpliesFormula(self, ctx:TxScriptParser.ImpliesFormulaContext):
        pass


    # Enter a parse tree produced by TxScriptParser#proceduresExpr.
    def enterProceduresExpr(self, ctx:TxScriptParser.ProceduresExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#proceduresExpr.
    def exitProceduresExpr(self, ctx:TxScriptParser.ProceduresExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#procedureExpr.
    def enterProcedureExpr(self, ctx:TxScriptParser.ProcedureExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#procedureExpr.
    def exitProcedureExpr(self, ctx:TxScriptParser.ProcedureExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#preconditionsExpr.
    def enterPreconditionsExpr(self, ctx:TxScriptParser.PreconditionsExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#preconditionsExpr.
    def exitPreconditionsExpr(self, ctx:TxScriptParser.PreconditionsExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#LessEq.
    def enterLessEq(self, ctx:TxScriptParser.LessEqContext):
        pass

    # Exit a parse tree produced by TxScriptParser#LessEq.
    def exitLessEq(self, ctx:TxScriptParser.LessEqContext):
        pass


    # Enter a parse tree produced by TxScriptParser#SumSubEq.
    def enterSumSubEq(self, ctx:TxScriptParser.SumSubEqContext):
        pass

    # Exit a parse tree produced by TxScriptParser#SumSubEq.
    def exitSumSubEq(self, ctx:TxScriptParser.SumSubEqContext):
        pass


    # Enter a parse tree produced by TxScriptParser#constant.
    def enterConstant(self, ctx:TxScriptParser.ConstantContext):
        pass

    # Exit a parse tree produced by TxScriptParser#constant.
    def exitConstant(self, ctx:TxScriptParser.ConstantContext):
        pass


    # Enter a parse tree produced by TxScriptParser#null.
    def enterNull(self, ctx:TxScriptParser.NullContext):
        pass

    # Exit a parse tree produced by TxScriptParser#null.
    def exitNull(self, ctx:TxScriptParser.NullContext):
        pass


    # Enter a parse tree produced by TxScriptParser#Wallet.
    def enterWallet(self, ctx:TxScriptParser.WalletContext):
        pass

    # Exit a parse tree produced by TxScriptParser#Wallet.
    def exitWallet(self, ctx:TxScriptParser.WalletContext):
        pass


    # Enter a parse tree produced by TxScriptParser#variable.
    def enterVariable(self, ctx:TxScriptParser.VariableContext):
        pass

    # Exit a parse tree produced by TxScriptParser#variable.
    def exitVariable(self, ctx:TxScriptParser.VariableContext):
        pass


    # Enter a parse tree produced by TxScriptParser#GreaterEq.
    def enterGreaterEq(self, ctx:TxScriptParser.GreaterEqContext):
        pass

    # Exit a parse tree produced by TxScriptParser#GreaterEq.
    def exitGreaterEq(self, ctx:TxScriptParser.GreaterEqContext):
        pass


    # Enter a parse tree produced by TxScriptParser#Greater.
    def enterGreater(self, ctx:TxScriptParser.GreaterContext):
        pass

    # Exit a parse tree produced by TxScriptParser#Greater.
    def exitGreater(self, ctx:TxScriptParser.GreaterContext):
        pass


    # Enter a parse tree produced by TxScriptParser#NEq.
    def enterNEq(self, ctx:TxScriptParser.NEqContext):
        pass

    # Exit a parse tree produced by TxScriptParser#NEq.
    def exitNEq(self, ctx:TxScriptParser.NEqContext):
        pass


    # Enter a parse tree produced by TxScriptParser#MultDivEq.
    def enterMultDivEq(self, ctx:TxScriptParser.MultDivEqContext):
        pass

    # Exit a parse tree produced by TxScriptParser#MultDivEq.
    def exitMultDivEq(self, ctx:TxScriptParser.MultDivEqContext):
        pass


    # Enter a parse tree produced by TxScriptParser#Eq.
    def enterEq(self, ctx:TxScriptParser.EqContext):
        pass

    # Exit a parse tree produced by TxScriptParser#Eq.
    def exitEq(self, ctx:TxScriptParser.EqContext):
        pass


    # Enter a parse tree produced by TxScriptParser#Less.
    def enterLess(self, ctx:TxScriptParser.LessContext):
        pass

    # Exit a parse tree produced by TxScriptParser#Less.
    def exitLess(self, ctx:TxScriptParser.LessContext):
        pass


    # Enter a parse tree produced by TxScriptParser#pArgsExprs.
    def enterPArgsExprs(self, ctx:TxScriptParser.PArgsExprsContext):
        pass

    # Exit a parse tree produced by TxScriptParser#pArgsExprs.
    def exitPArgsExprs(self, ctx:TxScriptParser.PArgsExprsContext):
        pass


    # Enter a parse tree produced by TxScriptParser#variableArg.
    def enterVariableArg(self, ctx:TxScriptParser.VariableArgContext):
        pass

    # Exit a parse tree produced by TxScriptParser#variableArg.
    def exitVariableArg(self, ctx:TxScriptParser.VariableArgContext):
        pass


    # Enter a parse tree produced by TxScriptParser#inputToken.
    def enterInputToken(self, ctx:TxScriptParser.InputTokenContext):
        pass

    # Exit a parse tree produced by TxScriptParser#inputToken.
    def exitInputToken(self, ctx:TxScriptParser.InputTokenContext):
        pass


    # Enter a parse tree produced by TxScriptParser#sequence.
    def enterSequence(self, ctx:TxScriptParser.SequenceContext):
        pass

    # Exit a parse tree produced by TxScriptParser#sequence.
    def exitSequence(self, ctx:TxScriptParser.SequenceContext):
        pass


    # Enter a parse tree produced by TxScriptParser#ifstatement.
    def enterIfstatement(self, ctx:TxScriptParser.IfstatementContext):
        pass

    # Exit a parse tree produced by TxScriptParser#ifstatement.
    def exitIfstatement(self, ctx:TxScriptParser.IfstatementContext):
        pass


    # Enter a parse tree produced by TxScriptParser#outputToken.
    def enterOutputToken(self, ctx:TxScriptParser.OutputTokenContext):
        pass

    # Exit a parse tree produced by TxScriptParser#outputToken.
    def exitOutputToken(self, ctx:TxScriptParser.OutputTokenContext):
        pass


    # Enter a parse tree produced by TxScriptParser#skipBody.
    def enterSkipBody(self, ctx:TxScriptParser.SkipBodyContext):
        pass

    # Exit a parse tree produced by TxScriptParser#skipBody.
    def exitSkipBody(self, ctx:TxScriptParser.SkipBodyContext):
        pass


    # Enter a parse tree produced by TxScriptParser#assignmentBody.
    def enterAssignmentBody(self, ctx:TxScriptParser.AssignmentBodyContext):
        pass

    # Exit a parse tree produced by TxScriptParser#assignmentBody.
    def exitAssignmentBody(self, ctx:TxScriptParser.AssignmentBodyContext):
        pass


    # Enter a parse tree produced by TxScriptParser#numberConstant.
    def enterNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        pass

    # Exit a parse tree produced by TxScriptParser#numberConstant.
    def exitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        pass


    # Enter a parse tree produced by TxScriptParser#agentOrTokenConstant.
    def enterAgentOrTokenConstant(self, ctx:TxScriptParser.AgentOrTokenConstantContext):
        pass

    # Exit a parse tree produced by TxScriptParser#agentOrTokenConstant.
    def exitAgentOrTokenConstant(self, ctx:TxScriptParser.AgentOrTokenConstantContext):
        pass


