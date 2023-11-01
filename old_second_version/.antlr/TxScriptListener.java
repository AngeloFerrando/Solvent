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
	 * Enter a parse tree produced by {@link TxScriptParser#globalVarsExpr}.
	 * @param ctx the parse tree
	 */
	void enterGlobalVarsExpr(TxScriptParser.GlobalVarsExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#globalVarsExpr}.
	 * @param ctx the parse tree
	 */
	void exitGlobalVarsExpr(TxScriptParser.GlobalVarsExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code globalVar}
	 * labeled alternative in {@link TxScriptParser#globalVarExpr}.
	 * @param ctx the parse tree
	 */
	void enterGlobalVar(TxScriptParser.GlobalVarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code globalVar}
	 * labeled alternative in {@link TxScriptParser#globalVarExpr}.
	 * @param ctx the parse tree
	 */
	void exitGlobalVar(TxScriptParser.GlobalVarContext ctx);
	/**
	 * Enter a parse tree produced by the {@code globalMap}
	 * labeled alternative in {@link TxScriptParser#globalVarExpr}.
	 * @param ctx the parse tree
	 */
	void enterGlobalMap(TxScriptParser.GlobalMapContext ctx);
	/**
	 * Exit a parse tree produced by the {@code globalMap}
	 * labeled alternative in {@link TxScriptParser#globalVarExpr}.
	 * @param ctx the parse tree
	 */
	void exitGlobalMap(TxScriptParser.GlobalMapContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#mapExpr}.
	 * @param ctx the parse tree
	 */
	void enterMapExpr(TxScriptParser.MapExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#mapExpr}.
	 * @param ctx the parse tree
	 */
	void exitMapExpr(TxScriptParser.MapExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#firstOrderFormulasExpr}.
	 * @param ctx the parse tree
	 */
	void enterFirstOrderFormulasExpr(TxScriptParser.FirstOrderFormulasExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#firstOrderFormulasExpr}.
	 * @param ctx the parse tree
	 */
	void exitFirstOrderFormulasExpr(TxScriptParser.FirstOrderFormulasExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code functionFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterFunctionFormula(TxScriptParser.FunctionFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code functionFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitFunctionFormula(TxScriptParser.FunctionFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tokenijn}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterTokenijn(TxScriptParser.TokenijnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tokenijn}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitTokenijn(TxScriptParser.TokenijnContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterNEqFormula(TxScriptParser.NEqFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitNEqFormula(TxScriptParser.NEqFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MultDivEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterMultDivEqFormula(TxScriptParser.MultDivEqFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MultDivEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitMultDivEqFormula(TxScriptParser.MultDivEqFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LessEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterLessEqFormula(TxScriptParser.LessEqFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LessEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitLessEqFormula(TxScriptParser.LessEqFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code atomFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterAtomFormula(TxScriptParser.AtomFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code atomFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitAtomFormula(TxScriptParser.AtomFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sumFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterSumFormula(TxScriptParser.SumFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sumFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitSumFormula(TxScriptParser.SumFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code andFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterAndFormula(TxScriptParser.AndFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code andFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitAndFormula(TxScriptParser.AndFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code atomFormulaN}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterAtomFormulaN(TxScriptParser.AtomFormulaNContext ctx);
	/**
	 * Exit a parse tree produced by the {@code atomFormulaN}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitAtomFormulaN(TxScriptParser.AtomFormulaNContext ctx);
	/**
	 * Enter a parse tree produced by the {@code notFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterNotFormula(TxScriptParser.NotFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code notFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitNotFormula(TxScriptParser.NotFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code existsFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterExistsFormula(TxScriptParser.ExistsFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code existsFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitExistsFormula(TxScriptParser.ExistsFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code orFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterOrFormula(TxScriptParser.OrFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code orFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitOrFormula(TxScriptParser.OrFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code groupFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterGroupFormula(TxScriptParser.GroupFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code groupFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitGroupFormula(TxScriptParser.GroupFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GreaterEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterGreaterEqFormula(TxScriptParser.GreaterEqFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GreaterEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitGreaterEqFormula(TxScriptParser.GreaterEqFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code token0jn}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterToken0jn(TxScriptParser.Token0jnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code token0jn}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitToken0jn(TxScriptParser.Token0jnContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SumSubEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterSumSubEqFormula(TxScriptParser.SumSubEqFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SumSubEqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitSumSubEqFormula(TxScriptParser.SumSubEqFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code forallFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterForallFormula(TxScriptParser.ForallFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code forallFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitForallFormula(TxScriptParser.ForallFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GreaterFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterGreaterFormula(TxScriptParser.GreaterFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GreaterFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitGreaterFormula(TxScriptParser.GreaterFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterEqFormula(TxScriptParser.EqFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EqFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitEqFormula(TxScriptParser.EqFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LessFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterLessFormula(TxScriptParser.LessFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LessFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitLessFormula(TxScriptParser.LessFormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code gVarn}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterGVarn(TxScriptParser.GVarnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code gVarn}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitGVarn(TxScriptParser.GVarnContext ctx);
	/**
	 * Enter a parse tree produced by the {@code impliesFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void enterImpliesFormula(TxScriptParser.ImpliesFormulaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code impliesFormula}
	 * labeled alternative in {@link TxScriptParser#firstOrderFormulaExpr}.
	 * @param ctx the parse tree
	 */
	void exitImpliesFormula(TxScriptParser.ImpliesFormulaContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#proceduresExpr}.
	 * @param ctx the parse tree
	 */
	void enterProceduresExpr(TxScriptParser.ProceduresExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#proceduresExpr}.
	 * @param ctx the parse tree
	 */
	void exitProceduresExpr(TxScriptParser.ProceduresExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#procedureExpr}.
	 * @param ctx the parse tree
	 */
	void enterProcedureExpr(TxScriptParser.ProcedureExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#procedureExpr}.
	 * @param ctx the parse tree
	 */
	void exitProcedureExpr(TxScriptParser.ProcedureExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#requiresExpr}.
	 * @param ctx the parse tree
	 */
	void enterRequiresExpr(TxScriptParser.RequiresExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#requiresExpr}.
	 * @param ctx the parse tree
	 */
	void exitRequiresExpr(TxScriptParser.RequiresExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#requireExpr}.
	 * @param ctx the parse tree
	 */
	void enterRequireExpr(TxScriptParser.RequireExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#requireExpr}.
	 * @param ctx the parse tree
	 */
	void exitRequireExpr(TxScriptParser.RequireExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SumSubEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterSumSubEq(TxScriptParser.SumSubEqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SumSubEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitSumSubEq(TxScriptParser.SumSubEqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code constant}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterConstant(TxScriptParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by the {@code constant}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitConstant(TxScriptParser.ConstantContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Wallet}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterWallet(TxScriptParser.WalletContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Wallet}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitWallet(TxScriptParser.WalletContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GreaterEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterGreaterEq(TxScriptParser.GreaterEqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GreaterEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitGreaterEq(TxScriptParser.GreaterEqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MultDivEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMultDivEq(TxScriptParser.MultDivEqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MultDivEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMultDivEq(TxScriptParser.MultDivEqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Eq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterEq(TxScriptParser.EqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Eq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitEq(TxScriptParser.EqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LessEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLessEq(TxScriptParser.LessEqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LessEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLessEq(TxScriptParser.LessEqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code null}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNull(TxScriptParser.NullContext ctx);
	/**
	 * Exit a parse tree produced by the {@code null}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNull(TxScriptParser.NullContext ctx);
	/**
	 * Enter a parse tree produced by the {@code variable}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterVariable(TxScriptParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code variable}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitVariable(TxScriptParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Greater}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterGreater(TxScriptParser.GreaterContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Greater}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitGreater(TxScriptParser.GreaterContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNEq(TxScriptParser.NEqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NEq}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNEq(TxScriptParser.NEqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code map}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMap(TxScriptParser.MapContext ctx);
	/**
	 * Exit a parse tree produced by the {@code map}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMap(TxScriptParser.MapContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Less}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLess(TxScriptParser.LessContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Less}
	 * labeled alternative in {@link TxScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLess(TxScriptParser.LessContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#pArgsExprs}.
	 * @param ctx the parse tree
	 */
	void enterPArgsExprs(TxScriptParser.PArgsExprsContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#pArgsExprs}.
	 * @param ctx the parse tree
	 */
	void exitPArgsExprs(TxScriptParser.PArgsExprsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code variableArg}
	 * labeled alternative in {@link TxScriptParser#pArgsExpr}.
	 * @param ctx the parse tree
	 */
	void enterVariableArg(TxScriptParser.VariableArgContext ctx);
	/**
	 * Exit a parse tree produced by the {@code variableArg}
	 * labeled alternative in {@link TxScriptParser#pArgsExpr}.
	 * @param ctx the parse tree
	 */
	void exitVariableArg(TxScriptParser.VariableArgContext ctx);
	/**
	 * Enter a parse tree produced by {@link TxScriptParser#bodyExprs}.
	 * @param ctx the parse tree
	 */
	void enterBodyExprs(TxScriptParser.BodyExprsContext ctx);
	/**
	 * Exit a parse tree produced by {@link TxScriptParser#bodyExprs}.
	 * @param ctx the parse tree
	 */
	void exitBodyExprs(TxScriptParser.BodyExprsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code skipBody}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void enterSkipBody(TxScriptParser.SkipBodyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code skipBody}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void exitSkipBody(TxScriptParser.SkipBodyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code withdraw}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void enterWithdraw(TxScriptParser.WithdrawContext ctx);
	/**
	 * Exit a parse tree produced by the {@code withdraw}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void exitWithdraw(TxScriptParser.WithdrawContext ctx);
	/**
	 * Enter a parse tree produced by the {@code deposit}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void enterDeposit(TxScriptParser.DepositContext ctx);
	/**
	 * Exit a parse tree produced by the {@code deposit}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void exitDeposit(TxScriptParser.DepositContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignmentBody}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentBody(TxScriptParser.AssignmentBodyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignmentBody}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentBody(TxScriptParser.AssignmentBodyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignmentBodyMap}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentBodyMap(TxScriptParser.AssignmentBodyMapContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignmentBodyMap}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentBodyMap(TxScriptParser.AssignmentBodyMapContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifstatement}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void enterIfstatement(TxScriptParser.IfstatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifstatement}
	 * labeled alternative in {@link TxScriptParser#bodyExpr}.
	 * @param ctx the parse tree
	 */
	void exitIfstatement(TxScriptParser.IfstatementContext ctx);
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
	 * Enter a parse tree produced by the {@code agentOrTokenConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void enterAgentOrTokenConstant(TxScriptParser.AgentOrTokenConstantContext ctx);
	/**
	 * Exit a parse tree produced by the {@code agentOrTokenConstant}
	 * labeled alternative in {@link TxScriptParser#constantExpr}.
	 * @param ctx the parse tree
	 */
	void exitAgentOrTokenConstant(TxScriptParser.AgentOrTokenConstantContext ctx);
}