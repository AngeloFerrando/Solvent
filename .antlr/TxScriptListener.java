// Generated from /home/angelo/Desktop/SMT/txscript-z3/TxScript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TxScriptParser}.
 */
public interface TxScriptListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#contractExpr}.
	 * @param ctx the parse tree
	 */
	void enterContractExpr(TxScriptParser.ContractExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#contractExpr}.
	 * @param ctx the parse tree
	 */
	void exitContractExpr(TxScriptParser.ContractExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#declsExpr}.
	 * @param ctx the parse tree
	 */
	void enterDeclsExpr(TxScriptParser.DeclsExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#declsExpr}.
	 * @param ctx the parse tree
	 */
	void exitDeclsExpr(TxScriptParser.DeclsExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void enterIntDecl(TxScriptParser.IntDeclContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void exitIntDecl(TxScriptParser.IntDeclContext ctx);
	/**
	 * Enter a parse tree produced by the {@code strDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void enterStrDecl(TxScriptParser.StrDeclContext ctx);
	/**
	 * Exit a parse tree produced by the {@code strDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void exitStrDecl(TxScriptParser.StrDeclContext ctx);
	/**
	 * Enter a parse tree produced by the {@code constrDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void enterConstrDecl(TxScriptParser.ConstrDeclContext ctx);
	/**
	 * Exit a parse tree produced by the {@code constrDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void exitConstrDecl(TxScriptParser.ConstrDeclContext ctx);
	/**
	 * Enter a parse tree produced by the {@code payableFunDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void enterPayableFunDecl(TxScriptParser.PayableFunDeclContext ctx);
	/**
	 * Exit a parse tree produced by the {@code payableFunDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void exitPayableFunDecl(TxScriptParser.PayableFunDeclContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nonPayableFunDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void enterNonPayableFunDecl(TxScriptParser.NonPayableFunDeclContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nonPayableFunDecl}
	 * labeled alternative in {@link TxScriptParser#declExpr}.
	 * @param ctx the parse tree
	 */
	void exitNonPayableFunDecl(TxScriptParser.NonPayableFunDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#argsExpr}.
	 * @param ctx the parse tree
	 */
	void enterArgsExpr(TxScriptParser.ArgsExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#argsExpr}.
	 * @param ctx the parse tree
	 */
	void exitArgsExpr(TxScriptParser.ArgsExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arg}
	 * labeled alternative in {@link TxScriptParser#argExpr}.
	 * @param ctx the parse tree
	 */
	void enterArg(TxScriptParser.ArgContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arg}
	 * labeled alternative in {@link TxScriptParser#argExpr}.
	 * @param ctx the parse tree
	 */
	void exitArg(TxScriptParser.ArgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sendCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void enterSendCmd(TxScriptParser.SendCmdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sendCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void exitSendCmd(TxScriptParser.SendCmdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code requireCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void enterRequireCmd(TxScriptParser.RequireCmdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code requireCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void exitRequireCmd(TxScriptParser.RequireCmdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code skipCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void enterSkipCmd(TxScriptParser.SkipCmdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code skipCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void exitSkipCmd(TxScriptParser.SkipCmdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code groupCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void enterGroupCmd(TxScriptParser.GroupCmdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code groupCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void exitGroupCmd(TxScriptParser.GroupCmdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void enterAssignCmd(TxScriptParser.AssignCmdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void exitAssignCmd(TxScriptParser.AssignCmdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifelseCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void enterIfelseCmd(TxScriptParser.IfelseCmdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifelseCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void exitIfelseCmd(TxScriptParser.IfelseCmdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code seqCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void enterSeqCmd(TxScriptParser.SeqCmdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code seqCmd}
	 * labeled alternative in {@link TxScriptParser#cmdExpr}.
	 * @param ctx the parse tree
	 */
	void exitSeqCmd(TxScriptParser.SeqCmdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code groupExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterGroupExpr(TxScriptParser.GroupExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code groupExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitGroupExpr(TxScriptParser.GroupExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code greaterExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterGreaterExpr(TxScriptParser.GreaterExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code greaterExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitGreaterExpr(TxScriptParser.GreaterExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code eqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterEqExpr(TxScriptParser.EqExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code eqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitEqExpr(TxScriptParser.EqExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code notExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNotExpr(TxScriptParser.NotExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code notExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNotExpr(TxScriptParser.NotExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code greaterEqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterGreaterEqExpr(TxScriptParser.GreaterEqExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code greaterEqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitGreaterEqExpr(TxScriptParser.GreaterEqExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code lessExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLessExpr(TxScriptParser.LessExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lessExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLessExpr(TxScriptParser.LessExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sumSubEqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterSumSubEqExpr(TxScriptParser.SumSubEqExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sumSubEqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitSumSubEqExpr(TxScriptParser.SumSubEqExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code lessEqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLessEqExpr(TxScriptParser.LessEqExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lessEqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLessEqExpr(TxScriptParser.LessEqExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code constExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterConstExpr(TxScriptParser.ConstExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code constExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitConstExpr(TxScriptParser.ConstExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code multDivEqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMultDivEqExpr(TxScriptParser.MultDivEqExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code multDivEqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMultDivEqExpr(TxScriptParser.MultDivEqExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code neqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNeqExpr(TxScriptParser.NeqExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code neqExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNeqExpr(TxScriptParser.NeqExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code andExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAndExpr(TxScriptParser.AndExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code andExpr}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAndExpr(TxScriptParser.AndExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code numberConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void enterNumberConstant(TxScriptParser.NumberConstantContext ctx);
	/**
	 * Exit a parse tree produced by the {@code numberConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void exitNumberConstant(TxScriptParser.NumberConstantContext ctx);
	/**
	 * Enter a parse tree produced by the {@code strConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void enterStrConstant(TxScriptParser.StrConstantContext ctx);
	/**
	 * Exit a parse tree produced by the {@code strConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void exitStrConstant(TxScriptParser.StrConstantContext ctx);
	/**
	 * Enter a parse tree produced by the {@code trueConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void enterTrueConstant(TxScriptParser.TrueConstantContext ctx);
	/**
	 * Exit a parse tree produced by the {@code trueConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void exitTrueConstant(TxScriptParser.TrueConstantContext ctx);
	/**
	 * Enter a parse tree produced by the {@code falseConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void enterFalseConstant(TxScriptParser.FalseConstantContext ctx);
	/**
	 * Exit a parse tree produced by the {@code falseConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void exitFalseConstant(TxScriptParser.FalseConstantContext ctx);
}