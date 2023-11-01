// Generated from /home/angelo/Desktop/SMT/txscript-z3/old_second_version/TxScript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class TxScriptParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

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
		T__52=53, LABEL=54, LABELUPPER=55, NUMBER=56, REAL=57, TYPE=58, WS=59, 
		COMMENT=60, LINE_COMMENT=61;
	public static final int
		RULE_contractExpr = 0, RULE_globalVarsExpr = 1, RULE_globalVarExpr = 2, 
		RULE_mapExpr = 3, RULE_firstOrderFormulasExpr = 4, RULE_firstOrderFormulaExpr = 5, 
		RULE_proceduresExpr = 6, RULE_procedureExpr = 7, RULE_requiresExpr = 8, 
		RULE_requireExpr = 9, RULE_expression = 10, RULE_pArgsExprs = 11, RULE_pArgsExpr = 12, 
		RULE_bodyExprs = 13, RULE_bodyExpr = 14, RULE_constantExpr = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"contractExpr", "globalVarsExpr", "globalVarExpr", "mapExpr", "firstOrderFormulasExpr", 
			"firstOrderFormulaExpr", "proceduresExpr", "procedureExpr", "requiresExpr", 
			"requireExpr", "expression", "pArgsExprs", "pArgsExpr", "bodyExprs", 
			"bodyExpr", "constantExpr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'contract'", "'{'", "'resources_bound'", "':'", "';'", "'agents_bound'", 
			"'tokens_bound'", "'}'", "'int'", "'float'", "'bool'", "'='", "'true'", 
			"'false'", "'map'", "'('", "'participant'", "'->'", "')'", "'query'", 
			"'#'", "'?'", "'not'", "'!'", "'*'", "'/'", "'+'", "'-'", "'=='", "'!='", 
			"'<'", "'>'", "'<='", "'>='", "'and'", "'&'", "'or'", "'|'", "'implies'", 
			"'Exists'", "'.'", "'Forall'", "'sum'", "','", "'in'", "'['", "']'", 
			"'require'", "'null'", "'skip'", "'if'", "'then'", "'else'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "LABEL", "LABELUPPER", "NUMBER", 
			"REAL", "TYPE", "WS", "COMMENT", "LINE_COMMENT"
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

	@SuppressWarnings("CheckReturnValue")
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
			setState(32);
			match(T__0);
			setState(33);
			((ContractExprContext)_localctx).name = match(LABELUPPER);
			setState(34);
			match(T__1);
			setState(35);
			match(T__2);
			setState(36);
			match(T__3);
			setState(37);
			((ContractExprContext)_localctx).resBound = match(NUMBER);
			setState(38);
			match(T__4);
			setState(39);
			match(T__5);
			setState(40);
			match(T__3);
			setState(41);
			((ContractExprContext)_localctx).agentBound = match(NUMBER);
			setState(42);
			match(T__4);
			setState(43);
			match(T__6);
			setState(44);
			match(T__3);
			setState(45);
			((ContractExprContext)_localctx).tokenBound = match(NUMBER);
			setState(46);
			match(T__4);
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 36352L) != 0)) {
				{
				setState(47);
				((ContractExprContext)_localctx).gVars = globalVarsExpr();
				}
			}

			setState(50);
			((ContractExprContext)_localctx).child = proceduresExpr();
			setState(51);
			match(T__7);
			setState(52);
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

	@SuppressWarnings("CheckReturnValue")
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
			setState(55); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(54);
				globalVarExpr();
				}
				}
				setState(57); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 36352L) != 0) );
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

	@SuppressWarnings("CheckReturnValue")
	public static class GlobalVarExprContext extends ParserRuleContext {
		public GlobalVarExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_globalVarExpr; }
	 
		public GlobalVarExprContext() { }
		public void copyFrom(GlobalVarExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GlobalMapContext extends GlobalVarExprContext {
		public MapExprContext mapDef;
		public Token name;
		public MapExprContext mapExpr() {
			return getRuleContext(MapExprContext.class,0);
		}
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public GlobalMapContext(GlobalVarExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GlobalVarContext extends GlobalVarExprContext {
		public Token ty;
		public Token name;
		public Token val;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public TerminalNode NUMBER() { return getToken(TxScriptParser.NUMBER, 0); }
		public TerminalNode REAL() { return getToken(TxScriptParser.REAL, 0); }
		public GlobalVarContext(GlobalVarExprContext ctx) { copyFrom(ctx); }
	}

	public final GlobalVarExprContext globalVarExpr() throws RecognitionException {
		GlobalVarExprContext _localctx = new GlobalVarExprContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_globalVarExpr);
		int _la;
		try {
			setState(68);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
			case T__9:
			case T__10:
				_localctx = new GlobalVarContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(59);
				((GlobalVarContext)_localctx).ty = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3584L) != 0)) ) {
					((GlobalVarContext)_localctx).ty = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(60);
				((GlobalVarContext)_localctx).name = match(LABEL);
				setState(61);
				match(T__11);
				setState(62);
				((GlobalVarContext)_localctx).val = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 216172782113808384L) != 0)) ) {
					((GlobalVarContext)_localctx).val = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(63);
				match(T__4);
				}
				break;
			case T__14:
				_localctx = new GlobalMapContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(64);
				((GlobalMapContext)_localctx).mapDef = mapExpr();
				setState(65);
				((GlobalMapContext)_localctx).name = match(LABEL);
				setState(66);
				match(T__4);
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

	@SuppressWarnings("CheckReturnValue")
	public static class MapExprContext extends ParserRuleContext {
		public Token domain;
		public Token codomain;
		public MapExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapExpr; }
	}

	public final MapExprContext mapExpr() throws RecognitionException {
		MapExprContext _localctx = new MapExprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_mapExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(T__14);
			setState(71);
			match(T__15);
			setState(72);
			((MapExprContext)_localctx).domain = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 134656L) != 0)) ) {
				((MapExprContext)_localctx).domain = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(73);
			match(T__17);
			setState(74);
			((MapExprContext)_localctx).codomain = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 134656L) != 0)) ) {
				((MapExprContext)_localctx).codomain = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(75);
			match(T__18);
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

	@SuppressWarnings("CheckReturnValue")
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
		enterRule(_localctx, 8, RULE_firstOrderFormulasExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__19) {
				{
				{
				setState(77);
				match(T__19);
				setState(78);
				match(T__1);
				setState(79);
				((FirstOrderFormulasExprContext)_localctx).child = firstOrderFormulaExpr(0);
				setState(80);
				match(T__7);
				}
				}
				setState(86);
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

	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class AtomFormulaContext extends FirstOrderFormulaExprContext {
		public Token child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public TerminalNode NUMBER() { return getToken(TxScriptParser.NUMBER, 0); }
		public AtomFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class NotFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext child;
		public FirstOrderFormulaExprContext firstOrderFormulaExpr() {
			return getRuleContext(FirstOrderFormulaExprContext.class,0);
		}
		public NotFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExistsFormulaContext extends FirstOrderFormulaExprContext {
		public Token var;
		public FirstOrderFormulaExprContext child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public FirstOrderFormulaExprContext firstOrderFormulaExpr() {
			return getRuleContext(FirstOrderFormulaExprContext.class,0);
		}
		public ExistsFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class GroupFormulaContext extends FirstOrderFormulaExprContext {
		public FirstOrderFormulaExprContext child;
		public FirstOrderFormulaExprContext firstOrderFormulaExpr() {
			return getRuleContext(FirstOrderFormulaExprContext.class,0);
		}
		public GroupFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class ForallFormulaContext extends FirstOrderFormulaExprContext {
		public Token var;
		public FirstOrderFormulaExprContext child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public FirstOrderFormulaExprContext firstOrderFormulaExpr() {
			return getRuleContext(FirstOrderFormulaExprContext.class,0);
		}
		public ForallFormulaContext(FirstOrderFormulaExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_firstOrderFormulaExpr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				_localctx = new AtomFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(88);
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
				setState(89);
				((AtomFormulaNContext)_localctx).child = match(LABEL);
				setState(90);
				match(T__3);
				setState(91);
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
				setState(92);
				match(T__1);
				setState(93);
				match(T__20);
				setState(94);
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
				setState(95);
				match(T__7);
				setState(96);
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
				setState(97);
				match(T__1);
				setState(98);
				match(T__20);
				setState(99);
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
				setState(100);
				match(T__3);
				setState(101);
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
				setState(102);
				match(T__7);
				setState(103);
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
				setState(104);
				match(T__1);
				setState(105);
				((GVarnContext)_localctx).x = match(LABEL);
				setState(106);
				match(T__7);
				setState(107);
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
				setState(108);
				((FunctionFormulaContext)_localctx).child = match(LABEL);
				setState(109);
				match(T__15);
				setState(115);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LABEL) {
					{
					setState(110);
					((FunctionFormulaContext)_localctx).agent = match(LABEL);
					setState(111);
					match(T__3);
					setState(112);
					((FunctionFormulaContext)_localctx).amount = match(LABEL);
					setState(113);
					match(T__21);
					setState(114);
					((FunctionFormulaContext)_localctx).token = match(LABEL);
					}
				}

				setState(117);
				match(T__18);
				}
				break;
			case 7:
				{
				_localctx = new NotFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(118);
				_la = _input.LA(1);
				if ( !(_la==T__22 || _la==T__23) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(119);
				((NotFormulaContext)_localctx).child = firstOrderFormulaExpr(16);
				}
				break;
			case 8:
				{
				_localctx = new ExistsFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(120);
				match(T__39);
				setState(121);
				((ExistsFormulaContext)_localctx).var = match(LABEL);
				setState(122);
				match(T__40);
				setState(123);
				((ExistsFormulaContext)_localctx).child = firstOrderFormulaExpr(4);
				}
				break;
			case 9:
				{
				_localctx = new ForallFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(124);
				match(T__41);
				setState(125);
				((ForallFormulaContext)_localctx).var = match(LABEL);
				setState(126);
				match(T__40);
				setState(127);
				((ForallFormulaContext)_localctx).child = firstOrderFormulaExpr(3);
				}
				break;
			case 10:
				{
				_localctx = new SumFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(128);
				match(T__42);
				setState(129);
				match(T__15);
				setState(130);
				((SumFormulaContext)_localctx).child = firstOrderFormulaExpr(0);
				setState(131);
				match(T__43);
				setState(132);
				((SumFormulaContext)_localctx).var = match(LABEL);
				setState(133);
				match(T__44);
				setState(134);
				match(T__45);
				setState(135);
				((SumFormulaContext)_localctx).varMin = match(NUMBER);
				setState(136);
				match(T__43);
				setState(137);
				((SumFormulaContext)_localctx).varMax = match(NUMBER);
				setState(138);
				match(T__46);
				setState(139);
				match(T__18);
				}
				break;
			case 11:
				{
				_localctx = new GroupFormulaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(141);
				match(T__15);
				setState(142);
				((GroupFormulaContext)_localctx).child = firstOrderFormulaExpr(0);
				setState(143);
				match(T__18);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(182);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(180);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new MultDivEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((MultDivEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(147);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(148);
						((MultDivEqFormulaContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__24 || _la==T__25) ) {
							((MultDivEqFormulaContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(149);
						((MultDivEqFormulaContext)_localctx).right = firstOrderFormulaExpr(16);
						}
						break;
					case 2:
						{
						_localctx = new SumSubEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((SumSubEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(150);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(151);
						((SumSubEqFormulaContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__26 || _la==T__27) ) {
							((SumSubEqFormulaContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(152);
						((SumSubEqFormulaContext)_localctx).right = firstOrderFormulaExpr(15);
						}
						break;
					case 3:
						{
						_localctx = new EqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((EqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(153);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						{
						setState(154);
						match(T__28);
						}
						setState(155);
						((EqFormulaContext)_localctx).right = firstOrderFormulaExpr(14);
						}
						break;
					case 4:
						{
						_localctx = new NEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((NEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(156);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						{
						setState(157);
						match(T__29);
						}
						setState(158);
						((NEqFormulaContext)_localctx).right = firstOrderFormulaExpr(13);
						}
						break;
					case 5:
						{
						_localctx = new LessFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((LessFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(159);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						{
						setState(160);
						match(T__30);
						}
						setState(161);
						((LessFormulaContext)_localctx).right = firstOrderFormulaExpr(12);
						}
						break;
					case 6:
						{
						_localctx = new GreaterFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((GreaterFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(162);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						{
						setState(163);
						match(T__31);
						}
						setState(164);
						((GreaterFormulaContext)_localctx).right = firstOrderFormulaExpr(11);
						}
						break;
					case 7:
						{
						_localctx = new LessEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((LessEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(165);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						{
						setState(166);
						match(T__32);
						}
						setState(167);
						((LessEqFormulaContext)_localctx).right = firstOrderFormulaExpr(10);
						}
						break;
					case 8:
						{
						_localctx = new GreaterEqFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((GreaterEqFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(168);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						{
						setState(169);
						match(T__33);
						}
						setState(170);
						((GreaterEqFormulaContext)_localctx).right = firstOrderFormulaExpr(9);
						}
						break;
					case 9:
						{
						_localctx = new AndFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((AndFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(171);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(172);
						_la = _input.LA(1);
						if ( !(_la==T__34 || _la==T__35) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(173);
						((AndFormulaContext)_localctx).right = firstOrderFormulaExpr(8);
						}
						break;
					case 10:
						{
						_localctx = new OrFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((OrFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(174);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(175);
						_la = _input.LA(1);
						if ( !(_la==T__36 || _la==T__37) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(176);
						((OrFormulaContext)_localctx).right = firstOrderFormulaExpr(7);
						}
						break;
					case 11:
						{
						_localctx = new ImpliesFormulaContext(new FirstOrderFormulaExprContext(_parentctx, _parentState));
						((ImpliesFormulaContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_firstOrderFormulaExpr);
						setState(177);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(178);
						_la = _input.LA(1);
						if ( !(_la==T__17 || _la==T__38) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(179);
						((ImpliesFormulaContext)_localctx).right = firstOrderFormulaExpr(6);
						}
						break;
					}
					} 
				}
				setState(184);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
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

	@SuppressWarnings("CheckReturnValue")
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
		enterRule(_localctx, 12, RULE_proceduresExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(185);
				((ProceduresExprContext)_localctx).child = procedureExpr();
				}
				}
				setState(188); 
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

	@SuppressWarnings("CheckReturnValue")
	public static class ProcedureExprContext extends ParserRuleContext {
		public Token action;
		public PArgsExprsContext pArgs;
		public RequiresExprContext requires;
		public BodyExprsContext body;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public RequiresExprContext requiresExpr() {
			return getRuleContext(RequiresExprContext.class,0);
		}
		public BodyExprsContext bodyExprs() {
			return getRuleContext(BodyExprsContext.class,0);
		}
		public PArgsExprsContext pArgsExprs() {
			return getRuleContext(PArgsExprsContext.class,0);
		}
		public ProcedureExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procedureExpr; }
	}

	public final ProcedureExprContext procedureExpr() throws RecognitionException {
		ProcedureExprContext _localctx = new ProcedureExprContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_procedureExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			((ProcedureExprContext)_localctx).action = match(LABEL);
			setState(191);
			match(T__15);
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LABEL) {
				{
				setState(192);
				((ProcedureExprContext)_localctx).pArgs = pArgsExprs();
				}
			}

			setState(195);
			match(T__18);
			setState(196);
			match(T__1);
			setState(197);
			((ProcedureExprContext)_localctx).requires = requiresExpr();
			setState(198);
			((ProcedureExprContext)_localctx).body = bodyExprs();
			setState(199);
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

	@SuppressWarnings("CheckReturnValue")
	public static class RequiresExprContext extends ParserRuleContext {
		public RequireExprContext child;
		public List<RequireExprContext> requireExpr() {
			return getRuleContexts(RequireExprContext.class);
		}
		public RequireExprContext requireExpr(int i) {
			return getRuleContext(RequireExprContext.class,i);
		}
		public RequiresExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_requiresExpr; }
	}

	public final RequiresExprContext requiresExpr() throws RecognitionException {
		RequiresExprContext _localctx = new RequiresExprContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_requiresExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__47) {
				{
				{
				setState(201);
				((RequiresExprContext)_localctx).child = requireExpr();
				}
				}
				setState(206);
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

	@SuppressWarnings("CheckReturnValue")
	public static class RequireExprContext extends ParserRuleContext {
		public ExpressionContext child;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public RequireExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_requireExpr; }
	}

	public final RequireExprContext requireExpr() throws RecognitionException {
		RequireExprContext _localctx = new RequireExprContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_requireExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			match(T__47);
			setState(208);
			match(T__15);
			setState(209);
			((RequireExprContext)_localctx).child = expression(0);
			setState(210);
			match(T__18);
			setState(211);
			match(T__4);
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

	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class ConstantContext extends ExpressionContext {
		public ConstantExprContext child;
		public ConstantExprContext constantExpr() {
			return getRuleContext(ConstantExprContext.class,0);
		}
		public ConstantContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WalletContext extends ExpressionContext {
		public ExpressionContext child;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public WalletContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class NullContext extends ExpressionContext {
		public Token child;
		public NullContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VariableContext extends ExpressionContext {
		public Token child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public VariableContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class MapContext extends ExpressionContext {
		public Token child;
		public ExpressionContext arg;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public MapContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
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
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				_localctx = new NullContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(214);
				((NullContext)_localctx).child = match(T__48);
				}
				break;
			case 2:
				{
				_localctx = new ConstantContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(215);
				((ConstantContext)_localctx).child = constantExpr();
				}
				break;
			case 3:
				{
				_localctx = new VariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(216);
				((VariableContext)_localctx).child = match(LABEL);
				}
				break;
			case 4:
				{
				_localctx = new MapContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(217);
				((MapContext)_localctx).child = match(LABEL);
				setState(218);
				match(T__45);
				setState(219);
				((MapContext)_localctx).arg = expression(0);
				setState(220);
				match(T__46);
				}
				break;
			case 5:
				{
				_localctx = new WalletContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(222);
				match(T__20);
				setState(223);
				((WalletContext)_localctx).child = expression(9);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(252);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(250);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
					case 1:
						{
						_localctx = new MultDivEqContext(new ExpressionContext(_parentctx, _parentState));
						((MultDivEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(226);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(227);
						((MultDivEqContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__24 || _la==T__25) ) {
							((MultDivEqContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(228);
						((MultDivEqContext)_localctx).right = expression(9);
						}
						break;
					case 2:
						{
						_localctx = new SumSubEqContext(new ExpressionContext(_parentctx, _parentState));
						((SumSubEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(229);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(230);
						((SumSubEqContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__26 || _la==T__27) ) {
							((SumSubEqContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(231);
						((SumSubEqContext)_localctx).right = expression(8);
						}
						break;
					case 3:
						{
						_localctx = new EqContext(new ExpressionContext(_parentctx, _parentState));
						((EqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(232);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						{
						setState(233);
						match(T__28);
						}
						setState(234);
						((EqContext)_localctx).right = expression(7);
						}
						break;
					case 4:
						{
						_localctx = new NEqContext(new ExpressionContext(_parentctx, _parentState));
						((NEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(235);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						{
						setState(236);
						match(T__29);
						}
						setState(237);
						((NEqContext)_localctx).right = expression(6);
						}
						break;
					case 5:
						{
						_localctx = new LessContext(new ExpressionContext(_parentctx, _parentState));
						((LessContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(238);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						{
						setState(239);
						match(T__30);
						}
						setState(240);
						((LessContext)_localctx).right = expression(5);
						}
						break;
					case 6:
						{
						_localctx = new GreaterContext(new ExpressionContext(_parentctx, _parentState));
						((GreaterContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(241);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						{
						setState(242);
						match(T__31);
						}
						setState(243);
						((GreaterContext)_localctx).right = expression(4);
						}
						break;
					case 7:
						{
						_localctx = new LessEqContext(new ExpressionContext(_parentctx, _parentState));
						((LessEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(244);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						{
						setState(245);
						match(T__32);
						}
						setState(246);
						((LessEqContext)_localctx).right = expression(3);
						}
						break;
					case 8:
						{
						_localctx = new GreaterEqContext(new ExpressionContext(_parentctx, _parentState));
						((GreaterEqContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(247);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						{
						setState(248);
						match(T__33);
						}
						setState(249);
						((GreaterEqContext)_localctx).right = expression(2);
						}
						break;
					}
					} 
				}
				setState(254);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
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

	@SuppressWarnings("CheckReturnValue")
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
		enterRule(_localctx, 22, RULE_pArgsExprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(256); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(255);
				pArgsExpr();
				}
				}
				setState(258); 
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

	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class VariableArgContext extends PArgsExprContext {
		public Token variable;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public VariableArgContext(PArgsExprContext ctx) { copyFrom(ctx); }
	}

	public final PArgsExprContext pArgsExpr() throws RecognitionException {
		PArgsExprContext _localctx = new PArgsExprContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_pArgsExpr);
		try {
			_localctx = new VariableArgContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			((VariableArgContext)_localctx).variable = match(LABEL);
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

	@SuppressWarnings("CheckReturnValue")
	public static class BodyExprsContext extends ParserRuleContext {
		public List<BodyExprContext> bodyExpr() {
			return getRuleContexts(BodyExprContext.class);
		}
		public BodyExprContext bodyExpr(int i) {
			return getRuleContext(BodyExprContext.class,i);
		}
		public BodyExprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bodyExprs; }
	}

	public final BodyExprsContext bodyExprs() throws RecognitionException {
		BodyExprsContext _localctx = new BodyExprsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_bodyExprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 130041439242420224L) != 0)) {
				{
				{
				setState(262);
				bodyExpr();
				setState(263);
				match(T__4);
				}
				}
				setState(269);
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

	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class SkipBodyContext extends BodyExprContext {
		public Token child;
		public SkipBodyContext(BodyExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DepositContext extends BodyExprContext {
		public ExpressionContext agent;
		public ExpressionContext variable;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public DepositContext(BodyExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentBodyMapContext extends BodyExprContext {
		public ExpressionContext variable;
		public ExpressionContext arg;
		public ExpressionContext child;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AssignmentBodyMapContext(BodyExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentBodyContext extends BodyExprContext {
		public ExpressionContext variable;
		public ExpressionContext child;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AssignmentBodyContext(BodyExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WithdrawContext extends BodyExprContext {
		public ExpressionContext agent;
		public ExpressionContext variable;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public WithdrawContext(BodyExprContext ctx) { copyFrom(ctx); }
	}

	public final BodyExprContext bodyExpr() throws RecognitionException {
		BodyExprContext _localctx = new BodyExprContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_bodyExpr);
		try {
			setState(297);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				_localctx = new SkipBodyContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(270);
				((SkipBodyContext)_localctx).child = match(T__49);
				}
				break;
			case 2:
				_localctx = new WithdrawContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(271);
				((WithdrawContext)_localctx).agent = expression(0);
				setState(272);
				match(T__23);
				setState(273);
				((WithdrawContext)_localctx).variable = expression(0);
				}
				break;
			case 3:
				_localctx = new DepositContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(275);
				((DepositContext)_localctx).agent = expression(0);
				setState(276);
				match(T__21);
				setState(277);
				((DepositContext)_localctx).variable = expression(0);
				}
				break;
			case 4:
				_localctx = new AssignmentBodyContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(279);
				((AssignmentBodyContext)_localctx).variable = expression(0);
				setState(280);
				match(T__11);
				setState(281);
				((AssignmentBodyContext)_localctx).child = expression(0);
				}
				break;
			case 5:
				_localctx = new AssignmentBodyMapContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(283);
				((AssignmentBodyMapContext)_localctx).variable = expression(0);
				setState(284);
				match(T__45);
				setState(285);
				((AssignmentBodyMapContext)_localctx).arg = expression(0);
				setState(286);
				match(T__46);
				setState(287);
				match(T__11);
				setState(288);
				((AssignmentBodyMapContext)_localctx).child = expression(0);
				}
				break;
			case 6:
				_localctx = new IfstatementContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(290);
				match(T__50);
				setState(291);
				((IfstatementContext)_localctx).condition = expression(0);
				setState(292);
				match(T__51);
				setState(293);
				((IfstatementContext)_localctx).first = bodyExpr();
				setState(294);
				match(T__52);
				setState(295);
				((IfstatementContext)_localctx).second = bodyExpr();
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

	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class AgentOrTokenConstantContext extends ConstantExprContext {
		public Token v;
		public TerminalNode LABELUPPER() { return getToken(TxScriptParser.LABELUPPER, 0); }
		public AgentOrTokenConstantContext(ConstantExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumberConstantContext extends ConstantExprContext {
		public Token v;
		public TerminalNode NUMBER() { return getToken(TxScriptParser.NUMBER, 0); }
		public NumberConstantContext(ConstantExprContext ctx) { copyFrom(ctx); }
	}

	public final ConstantExprContext constantExpr() throws RecognitionException {
		ConstantExprContext _localctx = new ConstantExprContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_constantExpr);
		try {
			setState(301);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				_localctx = new NumberConstantContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(299);
				((NumberConstantContext)_localctx).v = match(NUMBER);
				}
				break;
			case LABELUPPER:
				_localctx = new AgentOrTokenConstantContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(300);
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
		case 5:
			return firstOrderFormulaExpr_sempred((FirstOrderFormulaExprContext)_localctx, predIndex);
		case 10:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
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

	public static final String _serializedATN =
		"\u0004\u0001=\u0130\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u00001\b\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0004\u0001"+
		"8\b\u0001\u000b\u0001\f\u00019\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003"+
		"\u0002E\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0005\u0004S\b\u0004\n\u0004\f\u0004V\t\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005t\b\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005\u0092\b\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0005\u0005\u00b5\b\u0005\n\u0005\f\u0005"+
		"\u00b8\t\u0005\u0001\u0006\u0004\u0006\u00bb\b\u0006\u000b\u0006\f\u0006"+
		"\u00bc\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u00c2\b\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0005\b\u00cb\b\b\n\b\f\b\u00ce\t\b\u0001\t\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00e1\b\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0005\n\u00fb\b\n\n\n\f\n\u00fe\t\n\u0001\u000b"+
		"\u0004\u000b\u0101\b\u000b\u000b\u000b\f\u000b\u0102\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0005\r\u010a\b\r\n\r\f\r\u010d\t\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0003\u000e\u012a\b\u000e\u0001\u000f\u0001\u000f\u0003"+
		"\u000f\u012e\b\u000f\u0001\u000f\u0000\u0002\n\u0014\u0010\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		"\u0000\n\u0001\u0000\t\u000b\u0002\u0000\r\u000e89\u0002\u0000\t\u000b"+
		"\u0011\u0011\u0002\u00006688\u0001\u0000\u0017\u0018\u0001\u0000\u0019"+
		"\u001a\u0001\u0000\u001b\u001c\u0001\u0000#$\u0001\u0000%&\u0002\u0000"+
		"\u0012\u0012\'\'\u0150\u0000 \u0001\u0000\u0000\u0000\u00027\u0001\u0000"+
		"\u0000\u0000\u0004D\u0001\u0000\u0000\u0000\u0006F\u0001\u0000\u0000\u0000"+
		"\bT\u0001\u0000\u0000\u0000\n\u0091\u0001\u0000\u0000\u0000\f\u00ba\u0001"+
		"\u0000\u0000\u0000\u000e\u00be\u0001\u0000\u0000\u0000\u0010\u00cc\u0001"+
		"\u0000\u0000\u0000\u0012\u00cf\u0001\u0000\u0000\u0000\u0014\u00e0\u0001"+
		"\u0000\u0000\u0000\u0016\u0100\u0001\u0000\u0000\u0000\u0018\u0104\u0001"+
		"\u0000\u0000\u0000\u001a\u010b\u0001\u0000\u0000\u0000\u001c\u0129\u0001"+
		"\u0000\u0000\u0000\u001e\u012d\u0001\u0000\u0000\u0000 !\u0005\u0001\u0000"+
		"\u0000!\"\u00057\u0000\u0000\"#\u0005\u0002\u0000\u0000#$\u0005\u0003"+
		"\u0000\u0000$%\u0005\u0004\u0000\u0000%&\u00058\u0000\u0000&\'\u0005\u0005"+
		"\u0000\u0000\'(\u0005\u0006\u0000\u0000()\u0005\u0004\u0000\u0000)*\u0005"+
		"8\u0000\u0000*+\u0005\u0005\u0000\u0000+,\u0005\u0007\u0000\u0000,-\u0005"+
		"\u0004\u0000\u0000-.\u00058\u0000\u0000.0\u0005\u0005\u0000\u0000/1\u0003"+
		"\u0002\u0001\u00000/\u0001\u0000\u0000\u000001\u0001\u0000\u0000\u0000"+
		"12\u0001\u0000\u0000\u000023\u0003\f\u0006\u000034\u0005\b\u0000\u0000"+
		"45\u0003\b\u0004\u00005\u0001\u0001\u0000\u0000\u000068\u0003\u0004\u0002"+
		"\u000076\u0001\u0000\u0000\u000089\u0001\u0000\u0000\u000097\u0001\u0000"+
		"\u0000\u00009:\u0001\u0000\u0000\u0000:\u0003\u0001\u0000\u0000\u0000"+
		";<\u0007\u0000\u0000\u0000<=\u00056\u0000\u0000=>\u0005\f\u0000\u0000"+
		">?\u0007\u0001\u0000\u0000?E\u0005\u0005\u0000\u0000@A\u0003\u0006\u0003"+
		"\u0000AB\u00056\u0000\u0000BC\u0005\u0005\u0000\u0000CE\u0001\u0000\u0000"+
		"\u0000D;\u0001\u0000\u0000\u0000D@\u0001\u0000\u0000\u0000E\u0005\u0001"+
		"\u0000\u0000\u0000FG\u0005\u000f\u0000\u0000GH\u0005\u0010\u0000\u0000"+
		"HI\u0007\u0002\u0000\u0000IJ\u0005\u0012\u0000\u0000JK\u0007\u0002\u0000"+
		"\u0000KL\u0005\u0013\u0000\u0000L\u0007\u0001\u0000\u0000\u0000MN\u0005"+
		"\u0014\u0000\u0000NO\u0005\u0002\u0000\u0000OP\u0003\n\u0005\u0000PQ\u0005"+
		"\b\u0000\u0000QS\u0001\u0000\u0000\u0000RM\u0001\u0000\u0000\u0000SV\u0001"+
		"\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000"+
		"U\t\u0001\u0000\u0000\u0000VT\u0001\u0000\u0000\u0000WX\u0006\u0005\uffff"+
		"\uffff\u0000X\u0092\u0007\u0003\u0000\u0000YZ\u00056\u0000\u0000Z[\u0005"+
		"\u0004\u0000\u0000[\u0092\u0007\u0003\u0000\u0000\\]\u0005\u0002\u0000"+
		"\u0000]^\u0005\u0015\u0000\u0000^_\u0007\u0003\u0000\u0000_`\u0005\b\u0000"+
		"\u0000`\u0092\u0007\u0003\u0000\u0000ab\u0005\u0002\u0000\u0000bc\u0005"+
		"\u0015\u0000\u0000cd\u0007\u0003\u0000\u0000de\u0005\u0004\u0000\u0000"+
		"ef\u0007\u0003\u0000\u0000fg\u0005\b\u0000\u0000g\u0092\u0007\u0003\u0000"+
		"\u0000hi\u0005\u0002\u0000\u0000ij\u00056\u0000\u0000jk\u0005\b\u0000"+
		"\u0000k\u0092\u0007\u0003\u0000\u0000lm\u00056\u0000\u0000ms\u0005\u0010"+
		"\u0000\u0000no\u00056\u0000\u0000op\u0005\u0004\u0000\u0000pq\u00056\u0000"+
		"\u0000qr\u0005\u0016\u0000\u0000rt\u00056\u0000\u0000sn\u0001\u0000\u0000"+
		"\u0000st\u0001\u0000\u0000\u0000tu\u0001\u0000\u0000\u0000u\u0092\u0005"+
		"\u0013\u0000\u0000vw\u0007\u0004\u0000\u0000w\u0092\u0003\n\u0005\u0010"+
		"xy\u0005(\u0000\u0000yz\u00056\u0000\u0000z{\u0005)\u0000\u0000{\u0092"+
		"\u0003\n\u0005\u0004|}\u0005*\u0000\u0000}~\u00056\u0000\u0000~\u007f"+
		"\u0005)\u0000\u0000\u007f\u0092\u0003\n\u0005\u0003\u0080\u0081\u0005"+
		"+\u0000\u0000\u0081\u0082\u0005\u0010\u0000\u0000\u0082\u0083\u0003\n"+
		"\u0005\u0000\u0083\u0084\u0005,\u0000\u0000\u0084\u0085\u00056\u0000\u0000"+
		"\u0085\u0086\u0005-\u0000\u0000\u0086\u0087\u0005.\u0000\u0000\u0087\u0088"+
		"\u00058\u0000\u0000\u0088\u0089\u0005,\u0000\u0000\u0089\u008a\u00058"+
		"\u0000\u0000\u008a\u008b\u0005/\u0000\u0000\u008b\u008c\u0005\u0013\u0000"+
		"\u0000\u008c\u0092\u0001\u0000\u0000\u0000\u008d\u008e\u0005\u0010\u0000"+
		"\u0000\u008e\u008f\u0003\n\u0005\u0000\u008f\u0090\u0005\u0013\u0000\u0000"+
		"\u0090\u0092\u0001\u0000\u0000\u0000\u0091W\u0001\u0000\u0000\u0000\u0091"+
		"Y\u0001\u0000\u0000\u0000\u0091\\\u0001\u0000\u0000\u0000\u0091a\u0001"+
		"\u0000\u0000\u0000\u0091h\u0001\u0000\u0000\u0000\u0091l\u0001\u0000\u0000"+
		"\u0000\u0091v\u0001\u0000\u0000\u0000\u0091x\u0001\u0000\u0000\u0000\u0091"+
		"|\u0001\u0000\u0000\u0000\u0091\u0080\u0001\u0000\u0000\u0000\u0091\u008d"+
		"\u0001\u0000\u0000\u0000\u0092\u00b6\u0001\u0000\u0000\u0000\u0093\u0094"+
		"\n\u000f\u0000\u0000\u0094\u0095\u0007\u0005\u0000\u0000\u0095\u00b5\u0003"+
		"\n\u0005\u0010\u0096\u0097\n\u000e\u0000\u0000\u0097\u0098\u0007\u0006"+
		"\u0000\u0000\u0098\u00b5\u0003\n\u0005\u000f\u0099\u009a\n\r\u0000\u0000"+
		"\u009a\u009b\u0005\u001d\u0000\u0000\u009b\u00b5\u0003\n\u0005\u000e\u009c"+
		"\u009d\n\f\u0000\u0000\u009d\u009e\u0005\u001e\u0000\u0000\u009e\u00b5"+
		"\u0003\n\u0005\r\u009f\u00a0\n\u000b\u0000\u0000\u00a0\u00a1\u0005\u001f"+
		"\u0000\u0000\u00a1\u00b5\u0003\n\u0005\f\u00a2\u00a3\n\n\u0000\u0000\u00a3"+
		"\u00a4\u0005 \u0000\u0000\u00a4\u00b5\u0003\n\u0005\u000b\u00a5\u00a6"+
		"\n\t\u0000\u0000\u00a6\u00a7\u0005!\u0000\u0000\u00a7\u00b5\u0003\n\u0005"+
		"\n\u00a8\u00a9\n\b\u0000\u0000\u00a9\u00aa\u0005\"\u0000\u0000\u00aa\u00b5"+
		"\u0003\n\u0005\t\u00ab\u00ac\n\u0007\u0000\u0000\u00ac\u00ad\u0007\u0007"+
		"\u0000\u0000\u00ad\u00b5\u0003\n\u0005\b\u00ae\u00af\n\u0006\u0000\u0000"+
		"\u00af\u00b0\u0007\b\u0000\u0000\u00b0\u00b5\u0003\n\u0005\u0007\u00b1"+
		"\u00b2\n\u0005\u0000\u0000\u00b2\u00b3\u0007\t\u0000\u0000\u00b3\u00b5"+
		"\u0003\n\u0005\u0006\u00b4\u0093\u0001\u0000\u0000\u0000\u00b4\u0096\u0001"+
		"\u0000\u0000\u0000\u00b4\u0099\u0001\u0000\u0000\u0000\u00b4\u009c\u0001"+
		"\u0000\u0000\u0000\u00b4\u009f\u0001\u0000\u0000\u0000\u00b4\u00a2\u0001"+
		"\u0000\u0000\u0000\u00b4\u00a5\u0001\u0000\u0000\u0000\u00b4\u00a8\u0001"+
		"\u0000\u0000\u0000\u00b4\u00ab\u0001\u0000\u0000\u0000\u00b4\u00ae\u0001"+
		"\u0000\u0000\u0000\u00b4\u00b1\u0001\u0000\u0000\u0000\u00b5\u00b8\u0001"+
		"\u0000\u0000\u0000\u00b6\u00b4\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001"+
		"\u0000\u0000\u0000\u00b7\u000b\u0001\u0000\u0000\u0000\u00b8\u00b6\u0001"+
		"\u0000\u0000\u0000\u00b9\u00bb\u0003\u000e\u0007\u0000\u00ba\u00b9\u0001"+
		"\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00ba\u0001"+
		"\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000\u0000\u0000\u00bd\r\u0001\u0000"+
		"\u0000\u0000\u00be\u00bf\u00056\u0000\u0000\u00bf\u00c1\u0005\u0010\u0000"+
		"\u0000\u00c0\u00c2\u0003\u0016\u000b\u0000\u00c1\u00c0\u0001\u0000\u0000"+
		"\u0000\u00c1\u00c2\u0001\u0000\u0000\u0000\u00c2\u00c3\u0001\u0000\u0000"+
		"\u0000\u00c3\u00c4\u0005\u0013\u0000\u0000\u00c4\u00c5\u0005\u0002\u0000"+
		"\u0000\u00c5\u00c6\u0003\u0010\b\u0000\u00c6\u00c7\u0003\u001a\r\u0000"+
		"\u00c7\u00c8\u0005\b\u0000\u0000\u00c8\u000f\u0001\u0000\u0000\u0000\u00c9"+
		"\u00cb\u0003\u0012\t\u0000\u00ca\u00c9\u0001\u0000\u0000\u0000\u00cb\u00ce"+
		"\u0001\u0000\u0000\u0000\u00cc\u00ca\u0001\u0000\u0000\u0000\u00cc\u00cd"+
		"\u0001\u0000\u0000\u0000\u00cd\u0011\u0001\u0000\u0000\u0000\u00ce\u00cc"+
		"\u0001\u0000\u0000\u0000\u00cf\u00d0\u00050\u0000\u0000\u00d0\u00d1\u0005"+
		"\u0010\u0000\u0000\u00d1\u00d2\u0003\u0014\n\u0000\u00d2\u00d3\u0005\u0013"+
		"\u0000\u0000\u00d3\u00d4\u0005\u0005\u0000\u0000\u00d4\u0013\u0001\u0000"+
		"\u0000\u0000\u00d5\u00d6\u0006\n\uffff\uffff\u0000\u00d6\u00e1\u00051"+
		"\u0000\u0000\u00d7\u00e1\u0003\u001e\u000f\u0000\u00d8\u00e1\u00056\u0000"+
		"\u0000\u00d9\u00da\u00056\u0000\u0000\u00da\u00db\u0005.\u0000\u0000\u00db"+
		"\u00dc\u0003\u0014\n\u0000\u00dc\u00dd\u0005/\u0000\u0000\u00dd\u00e1"+
		"\u0001\u0000\u0000\u0000\u00de\u00df\u0005\u0015\u0000\u0000\u00df\u00e1"+
		"\u0003\u0014\n\t\u00e0\u00d5\u0001\u0000\u0000\u0000\u00e0\u00d7\u0001"+
		"\u0000\u0000\u0000\u00e0\u00d8\u0001\u0000\u0000\u0000\u00e0\u00d9\u0001"+
		"\u0000\u0000\u0000\u00e0\u00de\u0001\u0000\u0000\u0000\u00e1\u00fc\u0001"+
		"\u0000\u0000\u0000\u00e2\u00e3\n\b\u0000\u0000\u00e3\u00e4\u0007\u0005"+
		"\u0000\u0000\u00e4\u00fb\u0003\u0014\n\t\u00e5\u00e6\n\u0007\u0000\u0000"+
		"\u00e6\u00e7\u0007\u0006\u0000\u0000\u00e7\u00fb\u0003\u0014\n\b\u00e8"+
		"\u00e9\n\u0006\u0000\u0000\u00e9\u00ea\u0005\u001d\u0000\u0000\u00ea\u00fb"+
		"\u0003\u0014\n\u0007\u00eb\u00ec\n\u0005\u0000\u0000\u00ec\u00ed\u0005"+
		"\u001e\u0000\u0000\u00ed\u00fb\u0003\u0014\n\u0006\u00ee\u00ef\n\u0004"+
		"\u0000\u0000\u00ef\u00f0\u0005\u001f\u0000\u0000\u00f0\u00fb\u0003\u0014"+
		"\n\u0005\u00f1\u00f2\n\u0003\u0000\u0000\u00f2\u00f3\u0005 \u0000\u0000"+
		"\u00f3\u00fb\u0003\u0014\n\u0004\u00f4\u00f5\n\u0002\u0000\u0000\u00f5"+
		"\u00f6\u0005!\u0000\u0000\u00f6\u00fb\u0003\u0014\n\u0003\u00f7\u00f8"+
		"\n\u0001\u0000\u0000\u00f8\u00f9\u0005\"\u0000\u0000\u00f9\u00fb\u0003"+
		"\u0014\n\u0002\u00fa\u00e2\u0001\u0000\u0000\u0000\u00fa\u00e5\u0001\u0000"+
		"\u0000\u0000\u00fa\u00e8\u0001\u0000\u0000\u0000\u00fa\u00eb\u0001\u0000"+
		"\u0000\u0000\u00fa\u00ee\u0001\u0000\u0000\u0000\u00fa\u00f1\u0001\u0000"+
		"\u0000\u0000\u00fa\u00f4\u0001\u0000\u0000\u0000\u00fa\u00f7\u0001\u0000"+
		"\u0000\u0000\u00fb\u00fe\u0001\u0000\u0000\u0000\u00fc\u00fa\u0001\u0000"+
		"\u0000\u0000\u00fc\u00fd\u0001\u0000\u0000\u0000\u00fd\u0015\u0001\u0000"+
		"\u0000\u0000\u00fe\u00fc\u0001\u0000\u0000\u0000\u00ff\u0101\u0003\u0018"+
		"\f\u0000\u0100\u00ff\u0001\u0000\u0000\u0000\u0101\u0102\u0001\u0000\u0000"+
		"\u0000\u0102\u0100\u0001\u0000\u0000\u0000\u0102\u0103\u0001\u0000\u0000"+
		"\u0000\u0103\u0017\u0001\u0000\u0000\u0000\u0104\u0105\u00056\u0000\u0000"+
		"\u0105\u0019\u0001\u0000\u0000\u0000\u0106\u0107\u0003\u001c\u000e\u0000"+
		"\u0107\u0108\u0005\u0005\u0000\u0000\u0108\u010a\u0001\u0000\u0000\u0000"+
		"\u0109\u0106\u0001\u0000\u0000\u0000\u010a\u010d\u0001\u0000\u0000\u0000"+
		"\u010b\u0109\u0001\u0000\u0000\u0000\u010b\u010c\u0001\u0000\u0000\u0000"+
		"\u010c\u001b\u0001\u0000\u0000\u0000\u010d\u010b\u0001\u0000\u0000\u0000"+
		"\u010e\u012a\u00052\u0000\u0000\u010f\u0110\u0003\u0014\n\u0000\u0110"+
		"\u0111\u0005\u0018\u0000\u0000\u0111\u0112\u0003\u0014\n\u0000\u0112\u012a"+
		"\u0001\u0000\u0000\u0000\u0113\u0114\u0003\u0014\n\u0000\u0114\u0115\u0005"+
		"\u0016\u0000\u0000\u0115\u0116\u0003\u0014\n\u0000\u0116\u012a\u0001\u0000"+
		"\u0000\u0000\u0117\u0118\u0003\u0014\n\u0000\u0118\u0119\u0005\f\u0000"+
		"\u0000\u0119\u011a\u0003\u0014\n\u0000\u011a\u012a\u0001\u0000\u0000\u0000"+
		"\u011b\u011c\u0003\u0014\n\u0000\u011c\u011d\u0005.\u0000\u0000\u011d"+
		"\u011e\u0003\u0014\n\u0000\u011e\u011f\u0005/\u0000\u0000\u011f\u0120"+
		"\u0005\f\u0000\u0000\u0120\u0121\u0003\u0014\n\u0000\u0121\u012a\u0001"+
		"\u0000\u0000\u0000\u0122\u0123\u00053\u0000\u0000\u0123\u0124\u0003\u0014"+
		"\n\u0000\u0124\u0125\u00054\u0000\u0000\u0125\u0126\u0003\u001c\u000e"+
		"\u0000\u0126\u0127\u00055\u0000\u0000\u0127\u0128\u0003\u001c\u000e\u0000"+
		"\u0128\u012a\u0001\u0000\u0000\u0000\u0129\u010e\u0001\u0000\u0000\u0000"+
		"\u0129\u010f\u0001\u0000\u0000\u0000\u0129\u0113\u0001\u0000\u0000\u0000"+
		"\u0129\u0117\u0001\u0000\u0000\u0000\u0129\u011b\u0001\u0000\u0000\u0000"+
		"\u0129\u0122\u0001\u0000\u0000\u0000\u012a\u001d\u0001\u0000\u0000\u0000"+
		"\u012b\u012e\u00058\u0000\u0000\u012c\u012e\u00057\u0000\u0000\u012d\u012b"+
		"\u0001\u0000\u0000\u0000\u012d\u012c\u0001\u0000\u0000\u0000\u012e\u001f"+
		"\u0001\u0000\u0000\u0000\u001209DTs\u0091\u00b4\u00b6\u00bc\u00c1\u00cc"+
		"\u00e0\u00fa\u00fc\u0102\u010b\u0129\u012d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}