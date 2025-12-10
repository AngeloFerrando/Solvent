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


    # Visit a parse tree produced by TxScriptParser#propertiesExpr.
    def visitPropertiesExpr(self, ctx:TxScriptParser.PropertiesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#propertyExpr.
    def visitPropertyExpr(self, ctx:TxScriptParser.PropertyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#declsExpr.
    def visitDeclsExpr(self, ctx:TxScriptParser.DeclsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#fieldDecl.
    def visitFieldDecl(self, ctx:TxScriptParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#constrDecl.
    def visitConstrDecl(self, ctx:TxScriptParser.ConstrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#payableFunDecl.
    def visitPayableFunDecl(self, ctx:TxScriptParser.PayableFunDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#nonPayableFunDecl.
    def visitNonPayableFunDecl(self, ctx:TxScriptParser.NonPayableFunDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#payableConstructorDecl.
    def visitPayableConstructorDecl(self, ctx:TxScriptParser.PayableConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#nonPayableConstructorDecl.
    def visitNonPayableConstructorDecl(self, ctx:TxScriptParser.NonPayableConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#intDecl.
    def visitIntDecl(self, ctx:TxScriptParser.IntDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#uintDecl.
    def visitUintDecl(self, ctx:TxScriptParser.UintDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#boolDecl.
    def visitBoolDecl(self, ctx:TxScriptParser.BoolDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#strDecl.
    def visitStrDecl(self, ctx:TxScriptParser.StrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#addrDecl.
    def visitAddrDecl(self, ctx:TxScriptParser.AddrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#hashDecl.
    def visitHashDecl(self, ctx:TxScriptParser.HashDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#secretDecl.
    def visitSecretDecl(self, ctx:TxScriptParser.SecretDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#mapAddrDeclInt.
    def visitMapAddrDeclInt(self, ctx:TxScriptParser.MapAddrDeclIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#argsExpr.
    def visitArgsExpr(self, ctx:TxScriptParser.ArgsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#arg.
    def visitArg(self, ctx:TxScriptParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#argMap.
    def visitArgMap(self, ctx:TxScriptParser.ArgMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#sendCmd.
    def visitSendCmd(self, ctx:TxScriptParser.SendCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#requireCmd.
    def visitRequireCmd(self, ctx:TxScriptParser.RequireCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#skipCmd.
    def visitSkipCmd(self, ctx:TxScriptParser.SkipCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#groupCmd.
    def visitGroupCmd(self, ctx:TxScriptParser.GroupCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#assignCmd.
    def visitAssignCmd(self, ctx:TxScriptParser.AssignCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#ifelseCmd.
    def visitIfelseCmd(self, ctx:TxScriptParser.IfelseCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#ifCmd.
    def visitIfCmd(self, ctx:TxScriptParser.IfCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#seqCmd.
    def visitSeqCmd(self, ctx:TxScriptParser.SeqCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#assignMapCmd.
    def visitAssignMapCmd(self, ctx:TxScriptParser.AssignMapCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#groupExpr.
    def visitGroupExpr(self, ctx:TxScriptParser.GroupExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#sha256Expr.
    def visitSha256Expr(self, ctx:TxScriptParser.Sha256ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#greaterEqExpr.
    def visitGreaterEqExpr(self, ctx:TxScriptParser.GreaterEqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#mapExpr.
    def visitMapExpr(self, ctx:TxScriptParser.MapExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#lessExpr.
    def visitLessExpr(self, ctx:TxScriptParser.LessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#orExpr.
    def visitOrExpr(self, ctx:TxScriptParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#neqExpr.
    def visitNeqExpr(self, ctx:TxScriptParser.NeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#lengthExpr.
    def visitLengthExpr(self, ctx:TxScriptParser.LengthExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#greaterExpr.
    def visitGreaterExpr(self, ctx:TxScriptParser.GreaterExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#eqExpr.
    def visitEqExpr(self, ctx:TxScriptParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#notExpr.
    def visitNotExpr(self, ctx:TxScriptParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#multDivModExpr.
    def visitMultDivModExpr(self, ctx:TxScriptParser.MultDivModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#payableExpr.
    def visitPayableExpr(self, ctx:TxScriptParser.PayableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#oldExpr.
    def visitOldExpr(self, ctx:TxScriptParser.OldExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#sumSubExpr.
    def visitSumSubExpr(self, ctx:TxScriptParser.SumSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#lessEqExpr.
    def visitLessEqExpr(self, ctx:TxScriptParser.LessEqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#constExpr.
    def visitConstExpr(self, ctx:TxScriptParser.ConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#andExpr.
    def visitAndExpr(self, ctx:TxScriptParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#qslf.
    def visitQslf(self, ctx:TxScriptParser.QslfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#rules.
    def visitRules(self, ctx:TxScriptParser.RulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#ruleExpr.
    def visitRuleExpr(self, ctx:TxScriptParser.RuleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#andFormulaExpr.
    def visitAndFormulaExpr(self, ctx:TxScriptParser.AndFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#forallFormulaExpr.
    def visitForallFormulaExpr(self, ctx:TxScriptParser.ForallFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#existsFormulaExpr.
    def visitExistsFormulaExpr(self, ctx:TxScriptParser.ExistsFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#exprFormulaExpr.
    def visitExprFormulaExpr(self, ctx:TxScriptParser.ExprFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#notFormulaExpr.
    def visitNotFormulaExpr(self, ctx:TxScriptParser.NotFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#complexExprFormulaExpr.
    def visitComplexExprFormulaExpr(self, ctx:TxScriptParser.ComplexExprFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#orFormulaExpr.
    def visitOrFormulaExpr(self, ctx:TxScriptParser.OrFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#impliesFormulaExpr.
    def visitImpliesFormulaExpr(self, ctx:TxScriptParser.ImpliesFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#groupFormulaExpr.
    def visitGroupFormulaExpr(self, ctx:TxScriptParser.GroupFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#typeAddress.
    def visitTypeAddress(self, ctx:TxScriptParser.TypeAddressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#typeInt.
    def visitTypeInt(self, ctx:TxScriptParser.TypeIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#typeUInt.
    def visitTypeUInt(self, ctx:TxScriptParser.TypeUIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#typeBool.
    def visitTypeBool(self, ctx:TxScriptParser.TypeBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#typeMethod.
    def visitTypeMethod(self, ctx:TxScriptParser.TypeMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#typeCallDataArgs.
    def visitTypeCallDataArgs(self, ctx:TxScriptParser.TypeCallDataArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#varsFormulaExpr.
    def visitVarsFormulaExpr(self, ctx:TxScriptParser.VarsFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#varFormulaExpr.
    def visitVarFormulaExpr(self, ctx:TxScriptParser.VarFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#argsFormulaExpr.
    def visitArgsFormulaExpr(self, ctx:TxScriptParser.ArgsFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#argFormulaExpr.
    def visitArgFormulaExpr(self, ctx:TxScriptParser.ArgFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#numberConstant.
    def visitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#strConstant.
    def visitStrConstant(self, ctx:TxScriptParser.StrConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#trueConstant.
    def visitTrueConstant(self, ctx:TxScriptParser.TrueConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#falseConstant.
    def visitFalseConstant(self, ctx:TxScriptParser.FalseConstantContext):
        return self.visitChildren(ctx)



del TxScriptParser