// Generated from /home/angelo/Desktop/SMT/txscript-z3/old/TxScript.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TxScriptParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, T__50=51, T__51=52, 
		T__52=53, T__53=54, T__54=55, LABEL=56, LABELUPPER=57, NUMBER=58, REAL=59, 
		TYPE=60, WS=61, COMMENT=62, LINE_COMMENT=63;
	public static final int
		RULE_contractExpr = 0, RULE_globalVarsExpr = 1, RULE_globalVarExpr = 2, 
		RULE_firstOrderFormulasExpr = 3, RULE_firstOrderFormulaExpr = 4, RULE_proceduresExpr = 5, 
		RULE_procedureExpr = 6, RULE_preconditionsExpr = 7, RULE_expression = 8, 
		RULE_pArgsExprs = 9, RULE_pArgsExpr = 10, RULE_bodyExpr = 11, RULE_constantExpr = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"contractExpr", "globalVarsExpr", "globalVarExpr", "firstOrderFormulasExpr", 
			"firstOrderFormulaExpr", "proceduresExpr", "procedureExpr", "preconditionsExpr", 
			"expression", "pArgsExprs", "pArgsExpr", "bodyExpr", "constantExpr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'contract'", "'{'", "'resources_bound'", "':'", "'agents_bound'", 
			"'tokens_bound'", "'global'", "'}'", "'int'", "'float'", "'bool'", "'='", 
			"'true'", "'false'", "'query'", "'#'", "'('", "'?'", "')'", "'not'", 
			"'!'", "'*'", "'/'", "'+'", "'-'", "'=='", "'!='", "'<'", "'>'", "'<='", 
			"'>='", "'and'", "'&'", "'or'", "'|'", "'implies'", "'->'", "'Exists'", 
			"'.'", "'Forall'", "'sum'", "','", "'in'", "'['", "']'", "'@time'", "'_'", 
			"'@pre'", "'null'", "'skip'", "':='", "';'", "'if'", "'then'", "'else'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "LABEL", "LABELUPPER", 
			"NUMBER", "REAL", "TYPE", "WS", "COMMENT", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "TxScript.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TxScriptParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ContractExprContext extends ParserRuleContext {
		public Token name;
		public Token resBound;
		public Token agentBound;
		public Token tokenBound;
		public GlobalVarsExprContext gVars;
		public ProceduresExprContext child;
		public FirstOrderFormulasExprContext phis;
		public TerminalNode LABELUPPER() { return getToken(TxScriptParser.LABELUPPER, 0); }
		public List<TerminalNode> NUMBER() { return getTokens(TxScriptParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(TxScriptParser.NUMBER, i);
		}
		public ProceduresExprContext proceduresExpr() {
			return getRuleContext(ProceduresExprContext.class,0);
		}
		public FirstOrderFormulasExprContext firstOrderFormulasExpr() {
			return getRuleContext(FirstOrderFormulasExprContext.class,0);
		}
		public GlobalVarsExprContext globalVarsExpr() {
			return getRuleContext(GlobalVarsExprContext.class,0);
		}
		public ContractExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contractExpr; }
	}

	public final ContractExprContext contractExpr() throws RecognitionException {
		ContractExprContext _localctx = new ContractExprContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_contractExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			match(T__0);
			setState(27);
			((ContractExprContext)_localctx).name = match(LABELUPPER);
			setState(28);
			match(T__1);
			setState(29);
			match(T__2);
			setState(30);
			match(T__3);
			setState(31);
			((ContractExprContext)_localctx).resBound = match(NUMBER);
			setState(32);
			match(T__4);
			setState(33);
			match(T__3);
			setState(34);
			((ContractExprContext)_localctx).agentBound = match(NUMBER);
			setState(35);
			match(T__5);
			setState(36);
			match(T__3);
			setState(37);
			((ContractExprContext)_localctx).tokenBound = match(NUMBER);
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(38);
				match(T__6);
				setState(39);
				match(T__3);
				setState(40);
				((ContractExprContext)_localctx).gVars = globalVarsExpr();
				}
			}

			setState(43);
			((ContractExprContext)_localctx).child = proceduresExpr();
			setState(44);
			match(T__7);
			setState(45);
			((ContractExprContext)_localctx).phis = firstOrderFormulasExpr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GlobalVarsExprContext extends ParserRuleContext {
		public List<GlobalVarExprContext> globalVarExpr() {
			return getRuleContexts(GlobalVarExprContext.class);
		}
		public GlobalVarExprContext globalVarExpr(int i) {
			return getRuleContext(GlobalVarExprContext.class,i);
		}
		public GlobalVarsExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_globalVarsExpr; }
	}

	public final GlobalVarsExprContext globalVarsExpr() throws RecognitionException {
		GlobalVarsExprContext _localctx = new GlobalVarsExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_globalVarsExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(47);
				globalVarExpr();
				}
				}
				setState(50); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GlobalVarExprContext extends ParserRuleContext {
		public Token ty;
		public Token name;
		public Token val;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public TerminalNode NUMBER() { return getToken(TxScriptParser.NUMBER, 0); }
		public TerminalNode REAL() { return getToken(TxScriptParser.REAL, 0); }
		public GlobalVarExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_globalVarExpr; }
	}

	public final GlobalVarExprContext globalVarExpr() throws RecognitionException {
		GlobalVarExprContext _localctx = new GlobalVarExprContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_globalVarExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			((GlobalVarExprContext)_localctx).ty = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10))) != 0)) ) {
				((GlobalVarExprContext)_localctx).ty = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(53);
			((GlobalVarExprContext)_localctx).name = match(LABEL);
			setState(54);
			match(T__11);
			setState(55);
			((GlobalVarExprContext)_localctx).val = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__13) | (1L << NUMBER) | (1L << REAL))) != 0)) ) {
				((GlobalVarExprContext)_localctx).val = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FirstOrderFormulasExprContext extends ParserRuleContext {
		public FirstOrderFormulaExprContext child;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public FirstOrderFormulasExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_firstOrderFormulasExpr; }
	}

	public final FirstOrderFormulasExprContext firstOrderFormulasExpr() throws RecognitionException {
		FirstOrderFormulasExprContext _localctx = new FirstOrderFormulasExprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_firstOrderFormulasExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__14) {
				{
				{
				setState(57);
				match(T__14);
				setState(58);
				match(T__1);
				setState(59);
				((FirstOrderFormulasExprContext)_localctx).child = firstOrderFormulaExpr(0);
				setState(60);
				match(T__7);
				}
				}
				setState(66);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FirstOrderFormulaExprContext extends ParserRuleContext {
		public FirstOrderFormulaExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_firstOrderFormulaExpr; }
	 
		public FirstOrderFormulaExprContext() { }
		public void copyFrom(FirstOrderFormulaExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class FunctionFormulaContext extends FirstOrderFormulaExprContext {
		public Token child;
		public Token agent;
		public Token amount;
		public Token token;
		public List<TerminalNode> LABEL() { return getTokens(TxScriptParser.LABEL); }
		public TerminalNode LABEL(int i) {
			return getToken(TxScriptParser.LABEL, i);
		}
		public FunctionFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class TokenijnContext extends FirstOrderFormulaExprContext {
		public Token i;
		public Token j;
		public Token n;
		public List<TerminalNode> LABEL() { return getTokens(TxScriptParser.LABEL); }
		public TerminalNode LABEL(int i) {
			return getToken(TxScriptParser.LABEL, i);
		}
		public List<TerminalNode> NUMBER() { return getTokens(TxScriptParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(TxScriptParser.NUMBER, i);
		}
		public TokenijnContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class NEqFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public NEqFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class MultDivEqFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public Token op;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public MultDivEqFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class LessEqFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public LessEqFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class AtomFormulaContext extends FirstOrderFormulaExprContext {
		public Token child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public TerminalNode NUMBER() { return getToken(TxScriptParser.NUMBER, 0); }
		public AtomFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class SumFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext child;
		public Token var;
		public Token varMin;
		public Token varMax;
		public FirstOrderFormulaExprContext firstOrderFormulaExpr() {
			return getRuleContext(FirstOrderFormulaExprContext.class,0);
		}
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public List<TerminalNode> NUMBER() { return getTokens(TxScriptParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(TxScriptParser.NUMBER, i);
		}
		public SumFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class AndFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public AndFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class AtomFormulaNContext extends FirstOrderFormulaExprContext {
		public Token child;
		public Token n;
		public List<TerminalNode> LABEL() { return getTokens(TxScriptParser.LABEL); }
		public TerminalNode LABEL(int i) {
			return getToken(TxScriptParser.LABEL, i);
		}
		public TerminalNode NUMBER() { return getToken(TxScriptParser.NUMBER, 0); }
		public AtomFormulaNContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class NotFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext child;
		public FirstOrderFormulaExprContext firstOrderFormulaExpr() {
			return getRuleContext(FirstOrderFormulaExprContext.class,0);
		}
		public NotFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class ExistsFormulaContext extends FirstOrderFormulaExprContext {
		public Token var;
		public FirstOrderFormulaExprContext child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public FirstOrderFormulaExprContext firstOrderFormulaExpr() {
			return getRuleContext(FirstOrderFormulaExprContext.class,0);
		}
		public ExistsFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class OrFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public OrFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class GroupFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext child;
		public FirstOrderFormulaExprContext firstOrderFormulaExpr() {
			return getRuleContext(FirstOrderFormulaExprContext.class,0);
		}
		public GroupFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class GreaterEqFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public GreaterEqFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class Token0jnContext extends FirstOrderFormulaExprContext {
		public Token j;
		public Token n;
		public List<TerminalNode> LABEL() { return getTokens(TxScriptParser.LABEL); }
		public TerminalNode LABEL(int i) {
			return getToken(TxScriptParser.LABEL, i);
		}
		public List<TerminalNode> NUMBER() { return getTokens(TxScriptParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(TxScriptParser.NUMBER, i);
		}
		public Token0jnContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class SumSubEqFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public Token op;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public SumSubEqFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class ForallFormulaContext extends FirstOrderFormulaExprContext {
		public Token var;
		public FirstOrderFormulaExprContext child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public FirstOrderFormulaExprContext firstOrderFormulaExpr() {
			return getRuleContext(FirstOrderFormulaExprContext.class,0);
		}
		public ForallFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class GreaterFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public GreaterFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class EqFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public EqFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class LessFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public LessFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class GVarnContext extends FirstOrderFormulaExprContext {
		public Token x;
		public Token n;
		public List<TerminalNode> LABEL() { return getTokens(TxScriptParser.LABEL); }
		public TerminalNode LABEL(int i) {
			return getToken(TxScriptParser.LABEL, i);
		}
		public TerminalNode NUMBER() { return getToken(TxScriptParser.NUMBER, 0); }
		public GVarnContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	public static class ImpliesFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext left;
		public FirstOrderFormulaExprContext right;
		public List<FirstOrderFormulaExprContext> firstOrderFormulaExpr() {
			return getRuleContexts(FirstOrderFormulaExprContext.class);
		}
		public FirstOrderFormulaExprContext firstOrderFormulaExpr(int i) {
			return getRuleContext(FirstOrderFormulaExprContext.class,i);
		}
		public ImpliesFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}

	public final FirstOrderFormulaExprContext firstOrderFormulaExpr() throws RecognitionException {
		return firstOrderFormulaExpr(0);
	}

	private FirstOrderFormulaExprContext firstOrderFormulaExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		FirstOrderFormulaExprContext _localctx = new FirstOrderFormulaExprContext(_ctx, _parentState);
		FirstOrderFormulaExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_firstOrderFormulaExpr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				_localctx = new AtomFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(68);
				((AtomFormulaContext)_localctx).child = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LABEL || _la==NUMBER) ) {
					((AtomFormulaContext)_localctx).child = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 2:
				{
				_localctx = new AtomFormulaNContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(69);
				((AtomFormulaNContext)_localctx).child = match(LABEL);
				setState(70);
				match(T__3);
				setState(71);
				((AtomFormulaNContext)_localctx).n = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LABEL || _la==NUMBER) ) {
					((AtomFormulaNContext)_localctx).n = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 3:
				{
				_localctx = new Token0jnContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(72);
				match(T__1);
				setState(73);
				match(T__15);
				setState(74);
				((Token0jnContext)_localctx).j = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LABEL || _la==NUMBER) ) {
					((Token0jnContext)_localctx).j = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(75);
				match(T__7);
				setState(76);
				((Token0jnContext)_localctx).n = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LABEL || _la==NUMBER) ) {
					((Token0jnContext)_localctx).n = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 4:
				{
				_localctx = new TokenijnContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(77);
				match(T__1);
				setState(78);
				match(T__15);
				setState(79);
				((TokenijnContext)_localctx).i = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LABEL || _la==NUMBER) ) {
					((TokenijnContext)_localctx).i = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(80);
				match(T__3);
				setState(81);
				((TokenijnContext)_localctx).j = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LABEL || _la==NUMBER) ) {
					((TokenijnContext)_localctx).j = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(82);
				match(T__7);
				setState(83);
				((TokenijnContext)_localctx).n = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LABEL || _la==NUMBER) ) {
					((TokenijnContext)_localctx).n = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 5:
				{
				_localctx = new GVarnContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(84);
				match(T__1);
				setState(85);
				((GVarnContext)_localctx).x = match(LABEL);
				setState(86);
				match(T__7);
				setState(87);
				((GVarnContext)_localctx).n = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LABEL || _la==NUMBER) ) {
					((GVarnContext)_localctx).n = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 6:
				{
				_localctx = new FunctionFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(88);
				((FunctionFormulaContext)_localctx).child = match(LABEL);
				setState(89);
				match(T__16);
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LABEL) {
					{
					setState(90);
					((FunctionFormulaContext)_localctx).agent = match(LABEL);
					setState(91);
					match(T__3);
					setState(92);
					((FunctionFormulaContext)_localctx).amount = match(LABEL);
					setState(93);
					match(T__17);
					setState(94);
					((FunctionFormulaContext)_localctx).token = match(LABEL);
					}
				}

				setState(97);
				match(T__18);
				}
				break;
			case 7:
				{
				_localctx = new NotFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(98);
				_la = _input.LA(1);
				if ( !(_la==T__19 || _la==T__20) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(99);
				((NotFormulaContext)_localctx).child = firstOrderFormulaExpr(16);
				}
				break;
			case 8:
				{
				_localctx = new ExistsFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(100);
				match(T__37);
				setState(101);
				((ExistsFormulaContext)_localctx).var = match(LABEL);
				setState(102);
				match(T__38);
				setState(103);
				((ExistsFormulaContext)_localctx).child = firstOrderFormulaExpr(4);
				}
				break;
			case 9:
				{
				_localctx = new ForallFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(104);
				match(T__39);
				setState(105);
				((ForallFormulaContext)_localctx).var = match(LABEL);
				setState(106);
				match(T__38);
				setState(107);
				((ForallFormulaContext)_localctx).child = firstOrderFormulaExpr(3);
				}
				break;
			case 10:
				{
				_localctx = new SumFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(108);
				match(T__40);
				setState(109);
				match(T__16);
				setState(110);
				((SumFormulaContext)_localctx).child = firstOrderFormulaExpr(0);
				setState(111);
				match(T__41);
				setState(112);
				((SumFormulaContext)_localctx).var = match(LABEL);
				setState(113);
				match(T__42);
				setState(114);
				match(T__43);
				setState(115);
				((SumFormulaContext)_localctx).varMin = match(NUMBER);
				setState(116);
				match(T__41);
				setState(117);
				((SumFormulaContext)_localctx).varMax = match(NUMBER);
				setState(118);
				match(T__44);
				setState(119);
				match(T__18);
				}
				break;
			case 11:
				{
				_localctx = new GroupFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(121);
				match(T__16);
				setState(122);
				((GroupFormulaContext)_localctx).child = firstOrderFormulaExpr(0);
				setState(123);
				match(T__18);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(162);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(160);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						_localctx = new MultDivEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((MultDivEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(127);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(128);
						((MultDivEqFormulaContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__21 || _la==T__22) ) {
							((MultDivEqFormulaContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(129);
						((MultDivEqFormulaContext)_localctx).right = firstOrderFormulaExpr(16);
						}
						break;
					case 2:
						{
						_localctx = new SumSubEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((SumSubEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(130);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(131);
						((SumSubEqFormulaContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__23 || _la==T__24) ) {
							((SumSubEqFormulaContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(132);
						((SumSubEqFormulaContext)_localctx).right = firstOrderFormulaExpr(15);
						}
						break;
					case 3:
						{
						_localctx = new EqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((EqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(133);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						{
						setState(134);
						match(T__25);
						}
						setState(135);
						((EqFormulaContext)_localctx).right = firstOrderFormulaExpr(14);
						}
						break;
					case 4:
						{
						_localctx = new NEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((NEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(136);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						{
						setState(137);
						match(T__26);
						}
						setState(138);
						((NEqFormulaContext)_localctx).right = firstOrderFormulaExpr(13);
						}
						break;
					case 5:
						{
						_localctx = new LessFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((LessFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(139);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						{
						setState(140);
						match(T__27);
						}
						setState(141);
						((LessFormulaContext)_localctx).right = firstOrderFormulaExpr(12);
						}
						break;
					case 6:
						{
						_localctx = new GreaterFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((GreaterFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(142);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						{
						setState(143);
						match(T__28);
						}
						setState(144);
						((GreaterFormulaContext)_localctx).right = firstOrderFormulaExpr(11);
						}
						break;
					case 7:
						{
						_localctx = new LessEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((LessEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(145);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						{
						setState(146);
						match(T__29);
						}
						setState(147);
						((LessEqFormulaContext)_localctx).right = firstOrderFormulaExpr(10);
						}
						break;
					case 8:
						{
						_localctx = new GreaterEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((GreaterEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(148);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						{
						setState(149);
						match(T__30);
						}
						setState(150);
						((GreaterEqFormulaContext)_localctx).right = firstOrderFormulaExpr(9);
						}
						break;
					case 9:
						{
						_localctx = new AndFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((AndFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(151);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(152);
						_la = _input.LA(1);
						if ( !(_la==T__31 || _la==T__32) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(153);
						((AndFormulaContext)_localctx).right = firstOrderFormulaExpr(8);
						}
						break;
					case 10:
						{
						_localctx = new OrFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((OrFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(154);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(155);
						_la = _input.LA(1);
						if ( !(_la==T__33 || _la==T__34) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(156);
						((OrFormulaContext)_localctx).right = firstOrderFormulaExpr(7);
						}
						break;
					case 11:
						{
						_localctx = new ImpliesFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((ImpliesFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(157);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(158);
						_la = _input.LA(1);
						if ( !(_la==T__35 || _la==T__36) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(159);
						((ImpliesFormulaContext)_localctx).right = firstOrderFormulaExpr(6);
						}
						break;
					}
					} 
				}
				setState(164);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ProceduresExprContext extends ParserRuleContext {
		public ProcedureExprContext child;
		public List<ProcedureExprContext> procedureExpr() {
			return getRuleContexts(ProcedureExprContext.class);
		}
		public ProcedureExprContext procedureExpr(int i) {
			return getRuleContext(ProcedureExprContext.class,i);
		}
		public ProceduresExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_proceduresExpr; }
	}

	public final ProceduresExprContext proceduresExpr() throws RecognitionException {
		ProceduresExprContext _localctx = new ProceduresExprContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_proceduresExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(165);
				((ProceduresExprContext)_localctx).child = procedureExpr();
				}
				}
				setState(168); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__45 );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProcedureExprContext extends ParserRuleContext {
		public Token start;
		public Token end;
		public PreconditionsExprContext preconditions;
		public Token action;
		public PArgsExprsContext pArgs;
		public BodyExprContext body;
		public PreconditionsExprContext preconditionsExpr() {
			return getRuleContext(PreconditionsExprContext.class,0);
		}
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public PArgsExprsContext pArgsExprs() {
			return getRuleContext(PArgsExprsContext.class,0);
		}
		public BodyExprContext bodyExpr() {
			return getRuleContext(BodyExprContext.class,0);
		}
		public List<TerminalNode> NUMBER() { return getTokens(TxScriptParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(TxScriptParser.NUMBER, i);
		}
		public ProcedureExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procedureExpr; }
	}

	public final ProcedureExprContext procedureExpr() throws RecognitionException {
		ProcedureExprContext _localctx = new ProcedureExprContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_procedureExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			match(T__45);
			setState(171);
			match(T__43);
			setState(172);
			((ProcedureExprContext)_localctx).start = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==T__46 || _la==NUMBER) ) {
				((ProcedureExprContext)_localctx).start = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(173);
			match(T__41);
			setState(174);
			((ProcedureExprContext)_localctx).end = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==T__46 || _la==NUMBER) ) {
				((ProcedureExprContext)_localctx).end = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(175);
			match(T__44);
			setState(176);
			match(T__47);
			setState(177);
			((ProcedureExprContext)_localctx).preconditions = preconditionsExpr();
			setState(178);
			((ProcedureExprContext)_localctx).action = match(LABEL);
			setState(179);
			match(T__16);
			setState(180);
			((ProcedureExprContext)_localctx).pArgs = pArgsExprs();
			setState(181);
			match(T__18);
			setState(182);
			match(T__1);
			setState(183);
			((ProcedureExprContext)_localctx).body = bodyExpr(0);
			setState(184);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PreconditionsExprContext extends ParserRuleContext {
		public ExpressionContext child;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public PreconditionsExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preconditionsExpr; }
	}

	public final PreconditionsExprContext preconditionsExpr() throws RecognitionException {
		PreconditionsExprContext _localctx = new PreconditionsExprContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_preconditionsExpr);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(187); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(186);
					((PreconditionsExprContext)_localctx).child = expression(0);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(189); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class LessEqContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public LessEqContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class SumSubEqContext extends ExpressionContext {
		public ExpressionContext left;
		public Token op;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public SumSubEqContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ConstantContext extends ExpressionContext {
		public ConstantExprContext child;
		public ConstantExprContext constantExpr() {
			return getRuleContext(ConstantExprContext.class,0);
		}
		public ConstantContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class NullContext extends ExpressionContext {
		public Token child;
		public NullContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class WalletContext extends ExpressionContext {
		public ExpressionContext child;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public WalletContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class VariableContext extends ExpressionContext {
		public Token child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public VariableContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class GreaterEqContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public GreaterEqContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class GreaterContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public GreaterContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class NEqContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public NEqContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class MultDivEqContext extends ExpressionContext {
		public ExpressionContext left;
		public Token op;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MultDivEqContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class EqContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public EqContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class LessContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public LessContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__48:
				{
				_localctx = new NullContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(192);
				((NullContext)_localctx).child = match(T__48);
				}
				break;
			case LABELUPPER:
			case NUMBER:
				{
				_localctx = new ConstantContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(193);
				((ConstantContext)_localctx).child = constantExpr();
				}
				break;
			case LABEL:
				{
				_localctx = new VariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(194);
				((VariableContext)_localctx).child = match(LABEL);
				}
				break;
			case T__15:
				{
				_localctx = new WalletContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(195);
				match(T__15);
				setState(196);
				((WalletContext)_localctx).child = expression(9);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(225);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(223);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new MultDivEqContext(new ExpressionContext(_parentctx, _parentState));
						((MultDivEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(199);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(200);
						((MultDivEqContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__21 || _la==T__22) ) {
							((MultDivEqContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(201);
						((MultDivEqContext)_localctx).right = expression(9);
						}
						break;
					case 2:
						{
						_localctx = new SumSubEqContext(new ExpressionContext(_parentctx, _parentState));
						((SumSubEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(202);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(203);
						((SumSubEqContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__23 || _la==T__24) ) {
							((SumSubEqContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(204);
						((SumSubEqContext)_localctx).right = expression(8);
						}
						break;
					case 3:
						{
						_localctx = new EqContext(new ExpressionContext(_parentctx, _parentState));
						((EqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(205);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						{
						setState(206);
						match(T__25);
						}
						setState(207);
						((EqContext)_localctx).right = expression(7);
						}
						break;
					case 4:
						{
						_localctx = new NEqContext(new ExpressionContext(_parentctx, _parentState));
						((NEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(208);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						{
						setState(209);
						match(T__26);
						}
						setState(210);
						((NEqContext)_localctx).right = expression(6);
						}
						break;
					case 5:
						{
						_localctx = new LessContext(new ExpressionContext(_parentctx, _parentState));
						((LessContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(211);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						{
						setState(212);
						match(T__27);
						}
						setState(213);
						((LessContext)_localctx).right = expression(5);
						}
						break;
					case 6:
						{
						_localctx = new GreaterContext(new ExpressionContext(_parentctx, _parentState));
						((GreaterContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(214);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						{
						setState(215);
						match(T__28);
						}
						setState(216);
						((GreaterContext)_localctx).right = expression(4);
						}
						break;
					case 7:
						{
						_localctx = new LessEqContext(new ExpressionContext(_parentctx, _parentState));
						((LessEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(217);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						{
						setState(218);
						match(T__29);
						}
						setState(219);
						((LessEqContext)_localctx).right = expression(3);
						}
						break;
					case 8:
						{
						_localctx = new GreaterEqContext(new ExpressionContext(_parentctx, _parentState));
						((GreaterEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(220);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						{
						setState(221);
						match(T__30);
						}
						setState(222);
						((GreaterEqContext)_localctx).right = expression(2);
						}
						break;
					}
					} 
				}
				setState(227);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class PArgsExprsContext extends ParserRuleContext {
		public List<PArgsExprContext> pArgsExpr() {
			return getRuleContexts(PArgsExprContext.class);
		}
		public PArgsExprContext pArgsExpr(int i) {
			return getRuleContext(PArgsExprContext.class,i);
		}
		public PArgsExprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pArgsExprs; }
	}

	public final PArgsExprsContext pArgsExprs() throws RecognitionException {
		PArgsExprsContext _localctx = new PArgsExprsContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_pArgsExprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(228);
				pArgsExpr();
				}
				}
				setState(231); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LABEL );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PArgsExprContext extends ParserRuleContext {
		public PArgsExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pArgsExpr; }
	 
		public PArgsExprContext() { }
		public void copyFrom(PArgsExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class VariableArgContext extends PArgsExprContext {
		public Token variable;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public VariableArgContext(PArgsExprContext ctx) { copyFrom(ctx); }
	}
	public static class InputTokenContext extends PArgsExprContext {
		public Token agent;
		public Token data;
		public Token token;
		public List<TerminalNode> LABEL() { return getTokens(TxScriptParser.LABEL); }
		public TerminalNode LABEL(int i) {
			return getToken(TxScriptParser.LABEL, i);
		}
		public InputTokenContext(PArgsExprContext ctx) { copyFrom(ctx); }
	}

	public final PArgsExprContext pArgsExpr() throws RecognitionException {
		PArgsExprContext _localctx = new PArgsExprContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_pArgsExpr);
		try {
			setState(239);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				_localctx = new VariableArgContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(233);
				((VariableArgContext)_localctx).variable = match(LABEL);
				}
				break;
			case 2:
				_localctx = new InputTokenContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(234);
				((InputTokenContext)_localctx).agent = match(LABEL);
				setState(235);
				match(T__17);
				setState(236);
				((InputTokenContext)_localctx).data = match(LABEL);
				setState(237);
				match(T__3);
				setState(238);
				((InputTokenContext)_localctx).token = match(LABEL);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BodyExprContext extends ParserRuleContext {
		public BodyExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bodyExpr; }
	 
		public BodyExprContext() { }
		public void copyFrom(BodyExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SequenceContext extends BodyExprContext {
		public BodyExprContext left;
		public BodyExprContext right;
		public List<BodyExprContext> bodyExpr() {
			return getRuleContexts(BodyExprContext.class);
		}
		public BodyExprContext bodyExpr(int i) {
			return getRuleContext(BodyExprContext.class,i);
		}
		public SequenceContext(BodyExprContext ctx) { copyFrom(ctx); }
	}
	public static class IfstatementContext extends BodyExprContext {
		public ExpressionContext condition;
		public BodyExprContext first;
		public BodyExprContext second;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<BodyExprContext> bodyExpr() {
			return getRuleContexts(BodyExprContext.class);
		}
		public BodyExprContext bodyExpr(int i) {
			return getRuleContext(BodyExprContext.class,i);
		}
		public IfstatementContext(BodyExprContext ctx) { copyFrom(ctx); }
	}
	public static class OutputTokenContext extends BodyExprContext {
		public ExpressionContext agent;
		public ExpressionContext data;
		public ExpressionContext token;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public OutputTokenContext(BodyExprContext ctx) { copyFrom(ctx); }
	}
	public static class SkipBodyContext extends BodyExprContext {
		public Token child;
		public SkipBodyContext(BodyExprContext ctx) { copyFrom(ctx); }
	}
	public static class AssignmentBodyContext extends BodyExprContext {
		public Token variable;
		public ExpressionContext child;
		public TerminalNode LABELUPPER() { return getToken(TxScriptParser.LABELUPPER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentBodyContext(BodyExprContext ctx) { copyFrom(ctx); }
	}

	public final BodyExprContext bodyExpr() throws RecognitionException {
		return bodyExpr(0);
	}

	private BodyExprContext bodyExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		BodyExprContext _localctx = new BodyExprContext(_ctx, _parentState);
		BodyExprContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_bodyExpr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				_localctx = new SkipBodyContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(242);
				((SkipBodyContext)_localctx).child = match(T__49);
				}
				break;
			case 2:
				{
				_localctx = new AssignmentBodyContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(243);
				((AssignmentBodyContext)_localctx).variable = match(LABELUPPER);
				setState(244);
				match(T__50);
				setState(245);
				((AssignmentBodyContext)_localctx).child = expression(0);
				}
				break;
			case 3:
				{
				_localctx = new OutputTokenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(246);
				((OutputTokenContext)_localctx).agent = expression(0);
				setState(247);
				match(T__20);
				setState(248);
				((OutputTokenContext)_localctx).data = expression(0);
				setState(249);
				match(T__3);
				setState(250);
				((OutputTokenContext)_localctx).token = expression(0);
				}
				break;
			case 4:
				{
				_localctx = new IfstatementContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(252);
				match(T__52);
				setState(253);
				((IfstatementContext)_localctx).condition = expression(0);
				setState(254);
				match(T__53);
				setState(255);
				((IfstatementContext)_localctx).first = bodyExpr(0);
				setState(256);
				match(T__54);
				setState(257);
				((IfstatementContext)_localctx).second = bodyExpr(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(266);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new SequenceContext(new BodyExprContext(_parentctx, _parentState));
					((SequenceContext)_localctx).left = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_bodyExpr);
					setState(261);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(262);
					match(T__51);
					setState(263);
					((SequenceContext)_localctx).right = bodyExpr(3);
					}
					} 
				}
				setState(268);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ConstantExprContext extends ParserRuleContext {
		public ConstantExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constantExpr; }
	 
		public ConstantExprContext() { }
		public void copyFrom(ConstantExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AgentOrTokenConstantContext extends ConstantExprContext {
		public Token v;
		public TerminalNode LABELUPPER() { return getToken(TxScriptParser.LABELUPPER, 0); }
		public AgentOrTokenConstantContext(ConstantExprContext ctx) { copyFrom(ctx); }
	}
	public static class NumberConstantContext extends ConstantExprContext {
		public Token v;
		public TerminalNode NUMBER() { return getToken(TxScriptParser.NUMBER, 0); }
		public NumberConstantContext(ConstantExprContext ctx) { copyFrom(ctx); }
	}

	public final ConstantExprContext constantExpr() throws RecognitionException {
		ConstantExprContext _localctx = new ConstantExprContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_constantExpr);
		try {
			setState(271);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				_localctx = new NumberConstantContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				((NumberConstantContext)_localctx).v = match(NUMBER);
				}
				break;
			case LABELUPPER:
				_localctx = new AgentOrTokenConstantContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(270);
				((AgentOrTokenConstantContext)_localctx).v = match(LABELUPPER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return firstOrderFormulaExpr_sempred((FirstOrderFormulaExprContext)_localctx, predIndex);
		case 8:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 11:
			return bodyExpr_sempred((BodyExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean firstOrderFormulaExpr_sempred(FirstOrderFormulaExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 11);
		case 5:
			return precpred(_ctx, 10);
		case 6:
			return precpred(_ctx, 9);
		case 7:
			return precpred(_ctx, 8);
		case 8:
			return precpred(_ctx, 7);
		case 9:
			return precpred(_ctx, 6);
		case 10:
			return precpred(_ctx, 5);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 11:
			return precpred(_ctx, 8);
		case 12:
			return precpred(_ctx, 7);
		case 13:
			return precpred(_ctx, 6);
		case 14:
			return precpred(_ctx, 5);
		case 15:
			return precpred(_ctx, 4);
		case 16:
			return precpred(_ctx, 3);
		case 17:
			return precpred(_ctx, 2);
		case 18:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean bodyExpr_sempred(BodyExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 19:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A\u0114\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\5\2,\n\2\3\2\3\2\3\2\3\2\3\3\6\3\63\n\3\r\3\16\3"+
		"\64\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\7\5A\n\5\f\5\16\5D\13\5\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6b\n\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\5\6\u0080\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00a3\n\6\f\6\16\6\u00a6\13\6\3\7\6\7"+
		"\u00a9\n\7\r\7\16\7\u00aa\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\t\6\t\u00be\n\t\r\t\16\t\u00bf\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\5\n\u00c8\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00e2\n\n\f\n\16"+
		"\n\u00e5\13\n\3\13\6\13\u00e8\n\13\r\13\16\13\u00e9\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\5\f\u00f2\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\5\r\u0106\n\r\3\r\3\r\3\r\7\r\u010b\n\r\f\r\16"+
		"\r\u010e\13\r\3\16\3\16\5\16\u0112\n\16\3\16\2\5\n\22\30\17\2\4\6\b\n"+
		"\f\16\20\22\24\26\30\32\2\f\3\2\13\r\4\2\17\20<=\4\2::<<\3\2\26\27\3\2"+
		"\30\31\3\2\32\33\3\2\"#\3\2$%\3\2&\'\4\2\61\61<<\2\u0133\2\34\3\2\2\2"+
		"\4\62\3\2\2\2\6\66\3\2\2\2\bB\3\2\2\2\n\177\3\2\2\2\f\u00a8\3\2\2\2\16"+
		"\u00ac\3\2\2\2\20\u00bd\3\2\2\2\22\u00c7\3\2\2\2\24\u00e7\3\2\2\2\26\u00f1"+
		"\3\2\2\2\30\u0105\3\2\2\2\32\u0111\3\2\2\2\34\35\7\3\2\2\35\36\7;\2\2"+
		"\36\37\7\4\2\2\37 \7\5\2\2 !\7\6\2\2!\"\7<\2\2\"#\7\7\2\2#$\7\6\2\2$%"+
		"\7<\2\2%&\7\b\2\2&\'\7\6\2\2\'+\7<\2\2()\7\t\2\2)*\7\6\2\2*,\5\4\3\2+"+
		"(\3\2\2\2+,\3\2\2\2,-\3\2\2\2-.\5\f\7\2./\7\n\2\2/\60\5\b\5\2\60\3\3\2"+
		"\2\2\61\63\5\6\4\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2"+
		"\2\2\65\5\3\2\2\2\66\67\t\2\2\2\678\7:\2\289\7\16\2\29:\t\3\2\2:\7\3\2"+
		"\2\2;<\7\21\2\2<=\7\4\2\2=>\5\n\6\2>?\7\n\2\2?A\3\2\2\2@;\3\2\2\2AD\3"+
		"\2\2\2B@\3\2\2\2BC\3\2\2\2C\t\3\2\2\2DB\3\2\2\2EF\b\6\1\2F\u0080\t\4\2"+
		"\2GH\7:\2\2HI\7\6\2\2I\u0080\t\4\2\2JK\7\4\2\2KL\7\22\2\2LM\t\4\2\2MN"+
		"\7\n\2\2N\u0080\t\4\2\2OP\7\4\2\2PQ\7\22\2\2QR\t\4\2\2RS\7\6\2\2ST\t\4"+
		"\2\2TU\7\n\2\2U\u0080\t\4\2\2VW\7\4\2\2WX\7:\2\2XY\7\n\2\2Y\u0080\t\4"+
		"\2\2Z[\7:\2\2[a\7\23\2\2\\]\7:\2\2]^\7\6\2\2^_\7:\2\2_`\7\24\2\2`b\7:"+
		"\2\2a\\\3\2\2\2ab\3\2\2\2bc\3\2\2\2c\u0080\7\25\2\2de\t\5\2\2e\u0080\5"+
		"\n\6\22fg\7(\2\2gh\7:\2\2hi\7)\2\2i\u0080\5\n\6\6jk\7*\2\2kl\7:\2\2lm"+
		"\7)\2\2m\u0080\5\n\6\5no\7+\2\2op\7\23\2\2pq\5\n\6\2qr\7,\2\2rs\7:\2\2"+
		"st\7-\2\2tu\7.\2\2uv\7<\2\2vw\7,\2\2wx\7<\2\2xy\7/\2\2yz\7\25\2\2z\u0080"+
		"\3\2\2\2{|\7\23\2\2|}\5\n\6\2}~\7\25\2\2~\u0080\3\2\2\2\177E\3\2\2\2\177"+
		"G\3\2\2\2\177J\3\2\2\2\177O\3\2\2\2\177V\3\2\2\2\177Z\3\2\2\2\177d\3\2"+
		"\2\2\177f\3\2\2\2\177j\3\2\2\2\177n\3\2\2\2\177{\3\2\2\2\u0080\u00a4\3"+
		"\2\2\2\u0081\u0082\f\21\2\2\u0082\u0083\t\6\2\2\u0083\u00a3\5\n\6\22\u0084"+
		"\u0085\f\20\2\2\u0085\u0086\t\7\2\2\u0086\u00a3\5\n\6\21\u0087\u0088\f"+
		"\17\2\2\u0088\u0089\7\34\2\2\u0089\u00a3\5\n\6\20\u008a\u008b\f\16\2\2"+
		"\u008b\u008c\7\35\2\2\u008c\u00a3\5\n\6\17\u008d\u008e\f\r\2\2\u008e\u008f"+
		"\7\36\2\2\u008f\u00a3\5\n\6\16\u0090\u0091\f\f\2\2\u0091\u0092\7\37\2"+
		"\2\u0092\u00a3\5\n\6\r\u0093\u0094\f\13\2\2\u0094\u0095\7 \2\2\u0095\u00a3"+
		"\5\n\6\f\u0096\u0097\f\n\2\2\u0097\u0098\7!\2\2\u0098\u00a3\5\n\6\13\u0099"+
		"\u009a\f\t\2\2\u009a\u009b\t\b\2\2\u009b\u00a3\5\n\6\n\u009c\u009d\f\b"+
		"\2\2\u009d\u009e\t\t\2\2\u009e\u00a3\5\n\6\t\u009f\u00a0\f\7\2\2\u00a0"+
		"\u00a1\t\n\2\2\u00a1\u00a3\5\n\6\b\u00a2\u0081\3\2\2\2\u00a2\u0084\3\2"+
		"\2\2\u00a2\u0087\3\2\2\2\u00a2\u008a\3\2\2\2\u00a2\u008d\3\2\2\2\u00a2"+
		"\u0090\3\2\2\2\u00a2\u0093\3\2\2\2\u00a2\u0096\3\2\2\2\u00a2\u0099\3\2"+
		"\2\2\u00a2\u009c\3\2\2\2\u00a2\u009f\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4"+
		"\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\13\3\2\2\2\u00a6\u00a4\3\2\2"+
		"\2\u00a7\u00a9\5\16\b\2\u00a8\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa"+
		"\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\r\3\2\2\2\u00ac\u00ad\7\60\2"+
		"\2\u00ad\u00ae\7.\2\2\u00ae\u00af\t\13\2\2\u00af\u00b0\7,\2\2\u00b0\u00b1"+
		"\t\13\2\2\u00b1\u00b2\7/\2\2\u00b2\u00b3\7\62\2\2\u00b3\u00b4\5\20\t\2"+
		"\u00b4\u00b5\7:\2\2\u00b5\u00b6\7\23\2\2\u00b6\u00b7\5\24\13\2\u00b7\u00b8"+
		"\7\25\2\2\u00b8\u00b9\7\4\2\2\u00b9\u00ba\5\30\r\2\u00ba\u00bb\7\n\2\2"+
		"\u00bb\17\3\2\2\2\u00bc\u00be\5\22\n\2\u00bd\u00bc\3\2\2\2\u00be\u00bf"+
		"\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\21\3\2\2\2\u00c1"+
		"\u00c2\b\n\1\2\u00c2\u00c8\7\63\2\2\u00c3\u00c8\5\32\16\2\u00c4\u00c8"+
		"\7:\2\2\u00c5\u00c6\7\22\2\2\u00c6\u00c8\5\22\n\13\u00c7\u00c1\3\2\2\2"+
		"\u00c7\u00c3\3\2\2\2\u00c7\u00c4\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00e3"+
		"\3\2\2\2\u00c9\u00ca\f\n\2\2\u00ca\u00cb\t\6\2\2\u00cb\u00e2\5\22\n\13"+
		"\u00cc\u00cd\f\t\2\2\u00cd\u00ce\t\7\2\2\u00ce\u00e2\5\22\n\n\u00cf\u00d0"+
		"\f\b\2\2\u00d0\u00d1\7\34\2\2\u00d1\u00e2\5\22\n\t\u00d2\u00d3\f\7\2\2"+
		"\u00d3\u00d4\7\35\2\2\u00d4\u00e2\5\22\n\b\u00d5\u00d6\f\6\2\2\u00d6\u00d7"+
		"\7\36\2\2\u00d7\u00e2\5\22\n\7\u00d8\u00d9\f\5\2\2\u00d9\u00da\7\37\2"+
		"\2\u00da\u00e2\5\22\n\6\u00db\u00dc\f\4\2\2\u00dc\u00dd\7 \2\2\u00dd\u00e2"+
		"\5\22\n\5\u00de\u00df\f\3\2\2\u00df\u00e0\7!\2\2\u00e0\u00e2\5\22\n\4"+
		"\u00e1\u00c9\3\2\2\2\u00e1\u00cc\3\2\2\2\u00e1\u00cf\3\2\2\2\u00e1\u00d2"+
		"\3\2\2\2\u00e1\u00d5\3\2\2\2\u00e1\u00d8\3\2\2\2\u00e1\u00db\3\2\2\2\u00e1"+
		"\u00de\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2"+
		"\2\2\u00e4\23\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e8\5\26\f\2\u00e7\u00e6"+
		"\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea"+
		"\25\3\2\2\2\u00eb\u00f2\7:\2\2\u00ec\u00ed\7:\2\2\u00ed\u00ee\7\24\2\2"+
		"\u00ee\u00ef\7:\2\2\u00ef\u00f0\7\6\2\2\u00f0\u00f2\7:\2\2\u00f1\u00eb"+
		"\3\2\2\2\u00f1\u00ec\3\2\2\2\u00f2\27\3\2\2\2\u00f3\u00f4\b\r\1\2\u00f4"+
		"\u0106\7\64\2\2\u00f5\u00f6\7;\2\2\u00f6\u00f7\7\65\2\2\u00f7\u0106\5"+
		"\22\n\2\u00f8\u00f9\5\22\n\2\u00f9\u00fa\7\27\2\2\u00fa\u00fb\5\22\n\2"+
		"\u00fb\u00fc\7\6\2\2\u00fc\u00fd\5\22\n\2\u00fd\u0106\3\2\2\2\u00fe\u00ff"+
		"\7\67\2\2\u00ff\u0100\5\22\n\2\u0100\u0101\78\2\2\u0101\u0102\5\30\r\2"+
		"\u0102\u0103\79\2\2\u0103\u0104\5\30\r\3\u0104\u0106\3\2\2\2\u0105\u00f3"+
		"\3\2\2\2\u0105\u00f5\3\2\2\2\u0105\u00f8\3\2\2\2\u0105\u00fe\3\2\2\2\u0106"+
		"\u010c\3\2\2\2\u0107\u0108\f\4\2\2\u0108\u0109\7\66\2\2\u0109\u010b\5"+
		"\30\r\5\u010a\u0107\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c"+
		"\u010d\3\2\2\2\u010d\31\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0112\7<\2\2"+
		"\u0110\u0112\7;\2\2\u0111\u010f\3\2\2\2\u0111\u0110\3\2\2\2\u0112\33\3"+
		"\2\2\2\23+\64Ba\177\u00a2\u00a4\u00aa\u00bf\u00c7\u00e1\u00e3\u00e9\u00f1"+
		"\u0105\u010c\u0111";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}