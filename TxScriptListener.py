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


    # Enter a parse tree produced by TxScriptParser#propertiesExpr.
    def enterPropertiesExpr(self, ctx:TxScriptParser.PropertiesExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#propertiesExpr.
    def exitPropertiesExpr(self, ctx:TxScriptParser.PropertiesExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#propertyExpr.
    def enterPropertyExpr(self, ctx:TxScriptParser.PropertyExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#propertyExpr.
    def exitPropertyExpr(self, ctx:TxScriptParser.PropertyExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#declsExpr.
    def enterDeclsExpr(self, ctx:TxScriptParser.DeclsExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#declsExpr.
    def exitDeclsExpr(self, ctx:TxScriptParser.DeclsExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#fieldDecl.
    def enterFieldDecl(self, ctx:TxScriptParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#fieldDecl.
    def exitFieldDecl(self, ctx:TxScriptParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#constFieldDecl.
    def enterConstFieldDecl(self, ctx:TxScriptParser.ConstFieldDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#constFieldDecl.
    def exitConstFieldDecl(self, ctx:TxScriptParser.ConstFieldDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#constrDecl.
    def enterConstrDecl(self, ctx:TxScriptParser.ConstrDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#constrDecl.
    def exitConstrDecl(self, ctx:TxScriptParser.ConstrDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#payableFunDecl.
    def enterPayableFunDecl(self, ctx:TxScriptParser.PayableFunDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#payableFunDecl.
    def exitPayableFunDecl(self, ctx:TxScriptParser.PayableFunDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#nonPayableFunDecl.
    def enterNonPayableFunDecl(self, ctx:TxScriptParser.NonPayableFunDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#nonPayableFunDecl.
    def exitNonPayableFunDecl(self, ctx:TxScriptParser.NonPayableFunDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#payableConstructorDecl.
    def enterPayableConstructorDecl(self, ctx:TxScriptParser.PayableConstructorDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#payableConstructorDecl.
    def exitPayableConstructorDecl(self, ctx:TxScriptParser.PayableConstructorDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#nonPayableConstructorDecl.
    def enterNonPayableConstructorDecl(self, ctx:TxScriptParser.NonPayableConstructorDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#nonPayableConstructorDecl.
    def exitNonPayableConstructorDecl(self, ctx:TxScriptParser.NonPayableConstructorDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#intDecl.
    def enterIntDecl(self, ctx:TxScriptParser.IntDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#intDecl.
    def exitIntDecl(self, ctx:TxScriptParser.IntDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#boolDecl.
    def enterBoolDecl(self, ctx:TxScriptParser.BoolDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#boolDecl.
    def exitBoolDecl(self, ctx:TxScriptParser.BoolDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#strDecl.
    def enterStrDecl(self, ctx:TxScriptParser.StrDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#strDecl.
    def exitStrDecl(self, ctx:TxScriptParser.StrDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#addrDecl.
    def enterAddrDecl(self, ctx:TxScriptParser.AddrDeclContext):
        pass

    # Exit a parse tree produced by TxScriptParser#addrDecl.
    def exitAddrDecl(self, ctx:TxScriptParser.AddrDeclContext):
        pass


    # Enter a parse tree produced by TxScriptParser#mapAddrDeclInt.
    def enterMapAddrDeclInt(self, ctx:TxScriptParser.MapAddrDeclIntContext):
        pass

    # Exit a parse tree produced by TxScriptParser#mapAddrDeclInt.
    def exitMapAddrDeclInt(self, ctx:TxScriptParser.MapAddrDeclIntContext):
        pass


    # Enter a parse tree produced by TxScriptParser#argsExpr.
    def enterArgsExpr(self, ctx:TxScriptParser.ArgsExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#argsExpr.
    def exitArgsExpr(self, ctx:TxScriptParser.ArgsExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#arg.
    def enterArg(self, ctx:TxScriptParser.ArgContext):
        pass

    # Exit a parse tree produced by TxScriptParser#arg.
    def exitArg(self, ctx:TxScriptParser.ArgContext):
        pass


    # Enter a parse tree produced by TxScriptParser#sendCmd.
    def enterSendCmd(self, ctx:TxScriptParser.SendCmdContext):
        pass

    # Exit a parse tree produced by TxScriptParser#sendCmd.
    def exitSendCmd(self, ctx:TxScriptParser.SendCmdContext):
        pass


    # Enter a parse tree produced by TxScriptParser#requireCmd.
    def enterRequireCmd(self, ctx:TxScriptParser.RequireCmdContext):
        pass

    # Exit a parse tree produced by TxScriptParser#requireCmd.
    def exitRequireCmd(self, ctx:TxScriptParser.RequireCmdContext):
        pass


    # Enter a parse tree produced by TxScriptParser#skipCmd.
    def enterSkipCmd(self, ctx:TxScriptParser.SkipCmdContext):
        pass

    # Exit a parse tree produced by TxScriptParser#skipCmd.
    def exitSkipCmd(self, ctx:TxScriptParser.SkipCmdContext):
        pass


    # Enter a parse tree produced by TxScriptParser#groupCmd.
    def enterGroupCmd(self, ctx:TxScriptParser.GroupCmdContext):
        pass

    # Exit a parse tree produced by TxScriptParser#groupCmd.
    def exitGroupCmd(self, ctx:TxScriptParser.GroupCmdContext):
        pass


    # Enter a parse tree produced by TxScriptParser#assignCmd.
    def enterAssignCmd(self, ctx:TxScriptParser.AssignCmdContext):
        pass

    # Exit a parse tree produced by TxScriptParser#assignCmd.
    def exitAssignCmd(self, ctx:TxScriptParser.AssignCmdContext):
        pass


    # Enter a parse tree produced by TxScriptParser#ifelseCmd.
    def enterIfelseCmd(self, ctx:TxScriptParser.IfelseCmdContext):
        pass

    # Exit a parse tree produced by TxScriptParser#ifelseCmd.
    def exitIfelseCmd(self, ctx:TxScriptParser.IfelseCmdContext):
        pass


    # Enter a parse tree produced by TxScriptParser#ifCmd.
    def enterIfCmd(self, ctx:TxScriptParser.IfCmdContext):
        pass

    # Exit a parse tree produced by TxScriptParser#ifCmd.
    def exitIfCmd(self, ctx:TxScriptParser.IfCmdContext):
        pass


    # Enter a parse tree produced by TxScriptParser#seqCmd.
    def enterSeqCmd(self, ctx:TxScriptParser.SeqCmdContext):
        pass

    # Exit a parse tree produced by TxScriptParser#seqCmd.
    def exitSeqCmd(self, ctx:TxScriptParser.SeqCmdContext):
        pass


    # Enter a parse tree produced by TxScriptParser#assignMapCmd.
    def enterAssignMapCmd(self, ctx:TxScriptParser.AssignMapCmdContext):
        pass

    # Exit a parse tree produced by TxScriptParser#assignMapCmd.
    def exitAssignMapCmd(self, ctx:TxScriptParser.AssignMapCmdContext):
        pass


    # Enter a parse tree produced by TxScriptParser#groupExpr.
    def enterGroupExpr(self, ctx:TxScriptParser.GroupExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#groupExpr.
    def exitGroupExpr(self, ctx:TxScriptParser.GroupExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#greaterEqExpr.
    def enterGreaterEqExpr(self, ctx:TxScriptParser.GreaterEqExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#greaterEqExpr.
    def exitGreaterEqExpr(self, ctx:TxScriptParser.GreaterEqExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#mapExpr.
    def enterMapExpr(self, ctx:TxScriptParser.MapExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#mapExpr.
    def exitMapExpr(self, ctx:TxScriptParser.MapExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#lessExpr.
    def enterLessExpr(self, ctx:TxScriptParser.LessExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#lessExpr.
    def exitLessExpr(self, ctx:TxScriptParser.LessExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#orExpr.
    def enterOrExpr(self, ctx:TxScriptParser.OrExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#orExpr.
    def exitOrExpr(self, ctx:TxScriptParser.OrExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#neqExpr.
    def enterNeqExpr(self, ctx:TxScriptParser.NeqExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#neqExpr.
    def exitNeqExpr(self, ctx:TxScriptParser.NeqExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#greaterExpr.
    def enterGreaterExpr(self, ctx:TxScriptParser.GreaterExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#greaterExpr.
    def exitGreaterExpr(self, ctx:TxScriptParser.GreaterExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#eqExpr.
    def enterEqExpr(self, ctx:TxScriptParser.EqExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#eqExpr.
    def exitEqExpr(self, ctx:TxScriptParser.EqExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#notExpr.
    def enterNotExpr(self, ctx:TxScriptParser.NotExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#notExpr.
    def exitNotExpr(self, ctx:TxScriptParser.NotExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#sumSubEqExpr.
    def enterSumSubEqExpr(self, ctx:TxScriptParser.SumSubEqExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#sumSubEqExpr.
    def exitSumSubEqExpr(self, ctx:TxScriptParser.SumSubEqExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#lessEqExpr.
    def enterLessEqExpr(self, ctx:TxScriptParser.LessEqExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#lessEqExpr.
    def exitLessEqExpr(self, ctx:TxScriptParser.LessEqExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#constExpr.
    def enterConstExpr(self, ctx:TxScriptParser.ConstExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#constExpr.
    def exitConstExpr(self, ctx:TxScriptParser.ConstExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#multDivEqExpr.
    def enterMultDivEqExpr(self, ctx:TxScriptParser.MultDivEqExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#multDivEqExpr.
    def exitMultDivEqExpr(self, ctx:TxScriptParser.MultDivEqExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#andExpr.
    def enterAndExpr(self, ctx:TxScriptParser.AndExprContext):
        pass

    # Exit a parse tree produced by TxScriptParser#andExpr.
    def exitAndExpr(self, ctx:TxScriptParser.AndExprContext):
        pass


    # Enter a parse tree produced by TxScriptParser#qslf.
    def enterQslf(self, ctx:TxScriptParser.QslfContext):
        pass

    # Exit a parse tree produced by TxScriptParser#qslf.
    def exitQslf(self, ctx:TxScriptParser.QslfContext):
        pass


    # Enter a parse tree produced by TxScriptParser#numberConstant.
    def enterNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        pass

    # Exit a parse tree produced by TxScriptParser#numberConstant.
    def exitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        pass


    # Enter a parse tree produced by TxScriptParser#strConstant.
    def enterStrConstant(self, ctx:TxScriptParser.StrConstantContext):
        pass

    # Exit a parse tree produced by TxScriptParser#strConstant.
    def exitStrConstant(self, ctx:TxScriptParser.StrConstantContext):
        pass


    # Enter a parse tree produced by TxScriptParser#trueConstant.
    def enterTrueConstant(self, ctx:TxScriptParser.TrueConstantContext):
        pass

    # Exit a parse tree produced by TxScriptParser#trueConstant.
    def exitTrueConstant(self, ctx:TxScriptParser.TrueConstantContext):
        pass


    # Enter a parse tree produced by TxScriptParser#falseConstant.
    def enterFalseConstant(self, ctx:TxScriptParser.FalseConstantContext):
        pass

    # Exit a parse tree produced by TxScriptParser#falseConstant.
    def exitFalseConstant(self, ctx:TxScriptParser.FalseConstantContext):
        pass


