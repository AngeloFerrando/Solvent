# Generated from TxScript.g4 by ANTLR 4.8
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



del TxScriptParser