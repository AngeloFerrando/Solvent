// Generated from /home/angelo/Desktop/SMT/txscript-z3/TxScript.g4 by ANTLR 4.13.1
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
		T__31=32, T__32=33, T__33=34, LABEL=35, LABELUPPER=36, NUMBER=37, REAL=38, 
		TYPE=39, WS=40, COMMENT=41, LINE_COMMENT=42;
	public static final int
		RULE_contractExpr = 0, RULE_declsExpr = 1, RULE_declExpr = 2, RULE_argsExpr = 3, 
		RULE_argExpr = 4, RULE_cmdExpr = 5, RULE_expression = 6, RULE_constantExpr = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"contractExpr", "declsExpr", "declExpr", "argsExpr", "argExpr", "cmdExpr", 
			"expression", "constantExpr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'contract'", "'{'", "'}'", "'int'", "'string'", "'address'", "'constraint'", 
			"'('", "')'", "'function'", "'payable'", "'constructor'", "'skip'", "'require'", 
			"'if'", "'else'", "'='", "'!'", "';'", "'*'", "'/'", "'+'", "'-'", "'=='", 
			"'!='", "'<'", "'>'", "'<='", "'>='", "'and'", "'&&'", "'not'", "'true'", 
			"'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "LABEL", 
			"LABELUPPER", "NUMBER", "REAL", "TYPE", "WS", "COMMENT", "LINE_COMMENT"
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
		public DeclsExprContext decl;
		public TerminalNode LABELUPPER() { return getToken(TxScriptParser.LABELUPPER, 0); }
		public DeclsExprContext declsExpr() {
			return getRuleContext(DeclsExprContext.class,0);
		}
		public ContractExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contractExpr; }
	}

	public final ContractExprContext contractExpr() throws RecognitionException {
		ContractExprContext _localctx = new ContractExprContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_contractExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			match(T__0);
			setState(17);
			((ContractExprContext)_localctx).name = match(LABELUPPER);
			setState(18);
			match(T__1);
			setState(19);
			((ContractExprContext)_localctx).decl = declsExpr();
			setState(20);
			match(T__2);
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
	public static class DeclsExprContext extends ParserRuleContext {
		public List<DeclExprContext> declExpr() {
			return getRuleContexts(DeclExprContext.class);
		}
		public DeclExprContext declExpr(int i) {
			return getRuleContext(DeclExprContext.class,i);
		}
		public DeclsExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declsExpr; }
	}

	public final DeclsExprContext declsExpr() throws RecognitionException {
		DeclsExprContext _localctx = new DeclsExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declsExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(22);
				declExpr();
				}
				}
				setState(25); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 5360L) != 0) );
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
	public static class DeclExprContext extends ParserRuleContext {
		public DeclExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declExpr; }
	 
		public DeclExprContext() { }
		public void copyFrom(DeclExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ConstrDeclContext extends DeclExprContext {
		public Token name;
		public ArgsExprContext args;
		public CmdExprContext cmds;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public ArgsExprContext argsExpr() {
			return getRuleContext(ArgsExprContext.class,0);
		}
		public CmdExprContext cmdExpr() {
			return getRuleContext(CmdExprContext.class,0);
		}
		public ConstrDeclContext(DeclExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NonPayableFunDeclContext extends DeclExprContext {
		public Token name;
		public ArgsExprContext args;
		public CmdExprContext cmds;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public ArgsExprContext argsExpr() {
			return getRuleContext(ArgsExprContext.class,0);
		}
		public CmdExprContext cmdExpr() {
			return getRuleContext(CmdExprContext.class,0);
		}
		public NonPayableFunDeclContext(DeclExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ConstructorDeclContext extends DeclExprContext {
		public ArgsExprContext args;
		public CmdExprContext cmds;
		public ArgsExprContext argsExpr() {
			return getRuleContext(ArgsExprContext.class,0);
		}
		public CmdExprContext cmdExpr() {
			return getRuleContext(CmdExprContext.class,0);
		}
		public ConstructorDeclContext(DeclExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddrDeclContext extends DeclExprContext {
		public Token var;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public AddrDeclContext(DeclExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StrDeclContext extends DeclExprContext {
		public Token var;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public StrDeclContext(DeclExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PayableFunDeclContext extends DeclExprContext {
		public Token name;
		public ArgsExprContext args;
		public CmdExprContext cmds;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public ArgsExprContext argsExpr() {
			return getRuleContext(ArgsExprContext.class,0);
		}
		public CmdExprContext cmdExpr() {
			return getRuleContext(CmdExprContext.class,0);
		}
		public PayableFunDeclContext(DeclExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntDeclContext extends DeclExprContext {
		public Token var;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public IntDeclContext(DeclExprContext ctx) { copyFrom(ctx); }
	}

	public final DeclExprContext declExpr() throws RecognitionException {
		DeclExprContext _localctx = new DeclExprContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declExpr);
		try {
			setState(69);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new IntDeclContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(27);
				match(T__3);
				setState(28);
				((IntDeclContext)_localctx).var = match(LABEL);
				}
				break;
			case 2:
				_localctx = new StrDeclContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				match(T__4);
				setState(30);
				((StrDeclContext)_localctx).var = match(LABEL);
				}
				break;
			case 3:
				_localctx = new AddrDeclContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(31);
				match(T__5);
				setState(32);
				((AddrDeclContext)_localctx).var = match(LABEL);
				}
				break;
			case 4:
				_localctx = new ConstrDeclContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(33);
				match(T__6);
				setState(34);
				((ConstrDeclContext)_localctx).name = match(LABEL);
				setState(35);
				match(T__7);
				setState(36);
				((ConstrDeclContext)_localctx).args = argsExpr();
				setState(37);
				match(T__8);
				setState(38);
				match(T__1);
				setState(39);
				((ConstrDeclContext)_localctx).cmds = cmdExpr(0);
				setState(40);
				match(T__2);
				}
				break;
			case 5:
				_localctx = new PayableFunDeclContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(42);
				match(T__9);
				setState(43);
				((PayableFunDeclContext)_localctx).name = match(LABEL);
				setState(44);
				match(T__7);
				setState(45);
				((PayableFunDeclContext)_localctx).args = argsExpr();
				setState(46);
				match(T__8);
				setState(47);
				match(T__10);
				setState(48);
				match(T__1);
				setState(49);
				((PayableFunDeclContext)_localctx).cmds = cmdExpr(0);
				setState(50);
				match(T__2);
				}
				break;
			case 6:
				_localctx = new NonPayableFunDeclContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(52);
				match(T__9);
				setState(53);
				((NonPayableFunDeclContext)_localctx).name = match(LABEL);
				setState(54);
				match(T__7);
				setState(55);
				((NonPayableFunDeclContext)_localctx).args = argsExpr();
				setState(56);
				match(T__8);
				setState(57);
				match(T__1);
				setState(58);
				((NonPayableFunDeclContext)_localctx).cmds = cmdExpr(0);
				setState(59);
				match(T__2);
				}
				break;
			case 7:
				_localctx = new ConstructorDeclContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(61);
				match(T__11);
				setState(62);
				match(T__7);
				setState(63);
				((ConstructorDeclContext)_localctx).args = argsExpr();
				setState(64);
				match(T__8);
				setState(65);
				match(T__1);
				setState(66);
				((ConstructorDeclContext)_localctx).cmds = cmdExpr(0);
				setState(67);
				match(T__2);
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
	public static class ArgsExprContext extends ParserRuleContext {
		public List<ArgExprContext> argExpr() {
			return getRuleContexts(ArgExprContext.class);
		}
		public ArgExprContext argExpr(int i) {
			return getRuleContext(ArgExprContext.class,i);
		}
		public ArgsExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argsExpr; }
	}

	public final ArgsExprContext argsExpr() throws RecognitionException {
		ArgsExprContext _localctx = new ArgsExprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_argsExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LABEL) {
				{
				{
				setState(71);
				argExpr();
				}
				}
				setState(76);
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
	public static class ArgExprContext extends ParserRuleContext {
		public ArgExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argExpr; }
	 
		public ArgExprContext() { }
		public void copyFrom(ArgExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArgContext extends ArgExprContext {
		public Token var;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public ArgContext(ArgExprContext ctx) { copyFrom(ctx); }
	}

	public final ArgExprContext argExpr() throws RecognitionException {
		ArgExprContext _localctx = new ArgExprContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_argExpr);
		try {
			_localctx = new ArgContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			((ArgContext)_localctx).var = match(LABEL);
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
	public static class CmdExprContext extends ParserRuleContext {
		public CmdExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cmdExpr; }
	 
		public CmdExprContext() { }
		public void copyFrom(CmdExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SendCmdContext extends CmdExprContext {
		public Token sender;
		public ExpressionContext amount;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public SendCmdContext(CmdExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RequireCmdContext extends CmdExprContext {
		public ExpressionContext child;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public RequireCmdContext(CmdExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SkipCmdContext extends CmdExprContext {
		public SkipCmdContext(CmdExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GroupCmdContext extends CmdExprContext {
		public CmdExprContext cmdExpr() {
			return getRuleContext(CmdExprContext.class,0);
		}
		public GroupCmdContext(CmdExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignCmdContext extends CmdExprContext {
		public Token var;
		public ExpressionContext child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignCmdContext(CmdExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfelseCmdContext extends CmdExprContext {
		public ExpressionContext condition;
		public CmdExprContext ifcmd;
		public CmdExprContext elsecmd;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<CmdExprContext> cmdExpr() {
			return getRuleContexts(CmdExprContext.class);
		}
		public CmdExprContext cmdExpr(int i) {
			return getRuleContext(CmdExprContext.class,i);
		}
		public IfelseCmdContext(CmdExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SeqCmdContext extends CmdExprContext {
		public CmdExprContext seq1;
		public CmdExprContext seq2;
		public List<CmdExprContext> cmdExpr() {
			return getRuleContexts(CmdExprContext.class);
		}
		public CmdExprContext cmdExpr(int i) {
			return getRuleContext(CmdExprContext.class,i);
		}
		public SeqCmdContext(CmdExprContext ctx) { copyFrom(ctx); }
	}

	public final CmdExprContext cmdExpr() throws RecognitionException {
		return cmdExpr(0);
	}

	private CmdExprContext cmdExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CmdExprContext _localctx = new CmdExprContext(_ctx, _parentState);
		CmdExprContext _prevctx = _localctx;
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_cmdExpr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				_localctx = new SkipCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(80);
				match(T__12);
				}
				break;
			case 2:
				{
				_localctx = new RequireCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(81);
				match(T__13);
				setState(82);
				match(T__7);
				setState(83);
				((RequireCmdContext)_localctx).child = expression(0);
				setState(84);
				match(T__8);
				}
				break;
			case 3:
				{
				_localctx = new IfelseCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(86);
				match(T__14);
				setState(87);
				match(T__7);
				setState(88);
				((IfelseCmdContext)_localctx).condition = expression(0);
				setState(89);
				match(T__8);
				setState(90);
				match(T__1);
				setState(91);
				((IfelseCmdContext)_localctx).ifcmd = cmdExpr(0);
				setState(92);
				match(T__2);
				setState(93);
				match(T__15);
				setState(94);
				match(T__1);
				setState(95);
				((IfelseCmdContext)_localctx).elsecmd = cmdExpr(0);
				setState(96);
				match(T__2);
				}
				break;
			case 4:
				{
				_localctx = new AssignCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(98);
				((AssignCmdContext)_localctx).var = match(LABEL);
				setState(99);
				match(T__16);
				setState(100);
				((AssignCmdContext)_localctx).child = expression(0);
				}
				break;
			case 5:
				{
				_localctx = new SendCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(101);
				((SendCmdContext)_localctx).sender = match(LABEL);
				setState(102);
				match(T__17);
				setState(103);
				((SendCmdContext)_localctx).amount = expression(0);
				}
				break;
			case 6:
				{
				_localctx = new GroupCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(104);
				match(T__7);
				setState(105);
				cmdExpr(0);
				setState(106);
				match(T__8);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(115);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new SeqCmdContext(new CmdExprContext(_parentctx, _parentState));
					((SeqCmdContext)_localctx).seq1 = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_cmdExpr);
					setState(110);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(111);
					match(T__18);
					setState(112);
					((SeqCmdContext)_localctx).seq2 = cmdExpr(2);
					}
					} 
				}
				setState(117);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
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
	public static class GroupExprContext extends ExpressionContext {
		public ExpressionContext child;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public GroupExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GreaterExprContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public GreaterExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class EqExprContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public EqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotExprContext extends ExpressionContext {
		public ExpressionContext child;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public NotExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GreaterEqExprContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public GreaterEqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LessExprContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public LessExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SumSubEqExprContext extends ExpressionContext {
		public ExpressionContext left;
		public Token op;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public SumSubEqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LessEqExprContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public LessEqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ConstExprContext extends ExpressionContext {
		public ConstantExprContext child;
		public ConstantExprContext constantExpr() {
			return getRuleContext(ConstantExprContext.class,0);
		}
		public ConstExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MultDivEqExprContext extends ExpressionContext {
		public ExpressionContext left;
		public Token op;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MultDivEqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NeqExprContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public NeqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndExprContext extends ExpressionContext {
		public ExpressionContext left;
		public ExpressionContext right;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AndExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__32:
			case T__33:
			case LABEL:
			case NUMBER:
				{
				_localctx = new ConstExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(119);
				((ConstExprContext)_localctx).child = constantExpr();
				}
				break;
			case T__31:
				{
				_localctx = new NotExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(120);
				match(T__31);
				setState(121);
				((NotExprContext)_localctx).child = expression(2);
				}
				break;
			case T__7:
				{
				_localctx = new GroupExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(122);
				match(T__7);
				setState(123);
				((GroupExprContext)_localctx).child = expression(0);
				setState(124);
				match(T__8);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(157);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(155);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new MultDivEqExprContext(new ExpressionContext(_parentctx, _parentState));
						((MultDivEqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(128);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(129);
						((MultDivEqExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__19 || _la==T__20) ) {
							((MultDivEqExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(130);
						((MultDivEqExprContext)_localctx).right = expression(12);
						}
						break;
					case 2:
						{
						_localctx = new SumSubEqExprContext(new ExpressionContext(_parentctx, _parentState));
						((SumSubEqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(131);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(132);
						((SumSubEqExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__21 || _la==T__22) ) {
							((SumSubEqExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(133);
						((SumSubEqExprContext)_localctx).right = expression(11);
						}
						break;
					case 3:
						{
						_localctx = new EqExprContext(new ExpressionContext(_parentctx, _parentState));
						((EqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(134);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						{
						setState(135);
						match(T__23);
						}
						setState(136);
						((EqExprContext)_localctx).right = expression(10);
						}
						break;
					case 4:
						{
						_localctx = new NeqExprContext(new ExpressionContext(_parentctx, _parentState));
						((NeqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(137);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						{
						setState(138);
						match(T__24);
						}
						setState(139);
						((NeqExprContext)_localctx).right = expression(9);
						}
						break;
					case 5:
						{
						_localctx = new LessExprContext(new ExpressionContext(_parentctx, _parentState));
						((LessExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(140);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						{
						setState(141);
						match(T__25);
						}
						setState(142);
						((LessExprContext)_localctx).right = expression(8);
						}
						break;
					case 6:
						{
						_localctx = new GreaterExprContext(new ExpressionContext(_parentctx, _parentState));
						((GreaterExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(143);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						{
						setState(144);
						match(T__26);
						}
						setState(145);
						((GreaterExprContext)_localctx).right = expression(7);
						}
						break;
					case 7:
						{
						_localctx = new LessEqExprContext(new ExpressionContext(_parentctx, _parentState));
						((LessEqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(146);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						{
						setState(147);
						match(T__27);
						}
						setState(148);
						((LessEqExprContext)_localctx).right = expression(6);
						}
						break;
					case 8:
						{
						_localctx = new GreaterEqExprContext(new ExpressionContext(_parentctx, _parentState));
						((GreaterEqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(149);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						{
						setState(150);
						match(T__28);
						}
						setState(151);
						((GreaterEqExprContext)_localctx).right = expression(5);
						}
						break;
					case 9:
						{
						_localctx = new AndExprContext(new ExpressionContext(_parentctx, _parentState));
						((AndExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(152);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(153);
						_la = _input.LA(1);
						if ( !(_la==T__29 || _la==T__30) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(154);
						((AndExprContext)_localctx).right = expression(4);
						}
						break;
					}
					} 
				}
				setState(159);
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
	public static class FalseConstantContext extends ConstantExprContext {
		public Token v;
		public FalseConstantContext(ConstantExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StrConstantContext extends ConstantExprContext {
		public Token v;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public StrConstantContext(ConstantExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TrueConstantContext extends ConstantExprContext {
		public Token v;
		public TrueConstantContext(ConstantExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumberConstantContext extends ConstantExprContext {
		public Token v;
		public TerminalNode NUMBER() { return getToken(TxScriptParser.NUMBER, 0); }
		public NumberConstantContext(ConstantExprContext ctx) { copyFrom(ctx); }
	}

	public final ConstantExprContext constantExpr() throws RecognitionException {
		ConstantExprContext _localctx = new ConstantExprContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_constantExpr);
		try {
			setState(164);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				_localctx = new NumberConstantContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(160);
				((NumberConstantContext)_localctx).v = match(NUMBER);
				}
				break;
			case LABEL:
				_localctx = new StrConstantContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(161);
				((StrConstantContext)_localctx).v = match(LABEL);
				}
				break;
			case T__32:
				_localctx = new TrueConstantContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(162);
				((TrueConstantContext)_localctx).v = match(T__32);
				}
				break;
			case T__33:
				_localctx = new FalseConstantContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(163);
				((FalseConstantContext)_localctx).v = match(T__33);
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
			return cmdExpr_sempred((CmdExprContext)_localctx, predIndex);
		case 6:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean cmdExpr_sempred(CmdExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 11);
		case 2:
			return precpred(_ctx, 10);
		case 3:
			return precpred(_ctx, 9);
		case 4:
			return precpred(_ctx, 8);
		case 5:
			return precpred(_ctx, 7);
		case 6:
			return precpred(_ctx, 6);
		case 7:
			return precpred(_ctx, 5);
		case 8:
			return precpred(_ctx, 4);
		case 9:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001*\u00a7\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0004\u0001\u0018\b\u0001\u000b\u0001\f\u0001\u0019\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		"F\b\u0002\u0001\u0003\u0005\u0003I\b\u0003\n\u0003\f\u0003L\t\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0003\u0005m\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0005"+
		"\u0005r\b\u0005\n\u0005\f\u0005u\t\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003"+
		"\u0006\u007f\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006\u009c"+
		"\b\u0006\n\u0006\f\u0006\u009f\t\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0003\u0007\u00a5\b\u0007\u0001\u0007\u0000\u0002\n\f\b\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0000\u0003\u0001\u0000\u0014\u0015\u0001"+
		"\u0000\u0016\u0017\u0001\u0000\u001e\u001f\u00ba\u0000\u0010\u0001\u0000"+
		"\u0000\u0000\u0002\u0017\u0001\u0000\u0000\u0000\u0004E\u0001\u0000\u0000"+
		"\u0000\u0006J\u0001\u0000\u0000\u0000\bM\u0001\u0000\u0000\u0000\nl\u0001"+
		"\u0000\u0000\u0000\f~\u0001\u0000\u0000\u0000\u000e\u00a4\u0001\u0000"+
		"\u0000\u0000\u0010\u0011\u0005\u0001\u0000\u0000\u0011\u0012\u0005$\u0000"+
		"\u0000\u0012\u0013\u0005\u0002\u0000\u0000\u0013\u0014\u0003\u0002\u0001"+
		"\u0000\u0014\u0015\u0005\u0003\u0000\u0000\u0015\u0001\u0001\u0000\u0000"+
		"\u0000\u0016\u0018\u0003\u0004\u0002\u0000\u0017\u0016\u0001\u0000\u0000"+
		"\u0000\u0018\u0019\u0001\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000"+
		"\u0000\u0019\u001a\u0001\u0000\u0000\u0000\u001a\u0003\u0001\u0000\u0000"+
		"\u0000\u001b\u001c\u0005\u0004\u0000\u0000\u001cF\u0005#\u0000\u0000\u001d"+
		"\u001e\u0005\u0005\u0000\u0000\u001eF\u0005#\u0000\u0000\u001f \u0005"+
		"\u0006\u0000\u0000 F\u0005#\u0000\u0000!\"\u0005\u0007\u0000\u0000\"#"+
		"\u0005#\u0000\u0000#$\u0005\b\u0000\u0000$%\u0003\u0006\u0003\u0000%&"+
		"\u0005\t\u0000\u0000&\'\u0005\u0002\u0000\u0000\'(\u0003\n\u0005\u0000"+
		"()\u0005\u0003\u0000\u0000)F\u0001\u0000\u0000\u0000*+\u0005\n\u0000\u0000"+
		"+,\u0005#\u0000\u0000,-\u0005\b\u0000\u0000-.\u0003\u0006\u0003\u0000"+
		"./\u0005\t\u0000\u0000/0\u0005\u000b\u0000\u000001\u0005\u0002\u0000\u0000"+
		"12\u0003\n\u0005\u000023\u0005\u0003\u0000\u00003F\u0001\u0000\u0000\u0000"+
		"45\u0005\n\u0000\u000056\u0005#\u0000\u000067\u0005\b\u0000\u000078\u0003"+
		"\u0006\u0003\u000089\u0005\t\u0000\u00009:\u0005\u0002\u0000\u0000:;\u0003"+
		"\n\u0005\u0000;<\u0005\u0003\u0000\u0000<F\u0001\u0000\u0000\u0000=>\u0005"+
		"\f\u0000\u0000>?\u0005\b\u0000\u0000?@\u0003\u0006\u0003\u0000@A\u0005"+
		"\t\u0000\u0000AB\u0005\u0002\u0000\u0000BC\u0003\n\u0005\u0000CD\u0005"+
		"\u0003\u0000\u0000DF\u0001\u0000\u0000\u0000E\u001b\u0001\u0000\u0000"+
		"\u0000E\u001d\u0001\u0000\u0000\u0000E\u001f\u0001\u0000\u0000\u0000E"+
		"!\u0001\u0000\u0000\u0000E*\u0001\u0000\u0000\u0000E4\u0001\u0000\u0000"+
		"\u0000E=\u0001\u0000\u0000\u0000F\u0005\u0001\u0000\u0000\u0000GI\u0003"+
		"\b\u0004\u0000HG\u0001\u0000\u0000\u0000IL\u0001\u0000\u0000\u0000JH\u0001"+
		"\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000K\u0007\u0001\u0000\u0000"+
		"\u0000LJ\u0001\u0000\u0000\u0000MN\u0005#\u0000\u0000N\t\u0001\u0000\u0000"+
		"\u0000OP\u0006\u0005\uffff\uffff\u0000Pm\u0005\r\u0000\u0000QR\u0005\u000e"+
		"\u0000\u0000RS\u0005\b\u0000\u0000ST\u0003\f\u0006\u0000TU\u0005\t\u0000"+
		"\u0000Um\u0001\u0000\u0000\u0000VW\u0005\u000f\u0000\u0000WX\u0005\b\u0000"+
		"\u0000XY\u0003\f\u0006\u0000YZ\u0005\t\u0000\u0000Z[\u0005\u0002\u0000"+
		"\u0000[\\\u0003\n\u0005\u0000\\]\u0005\u0003\u0000\u0000]^\u0005\u0010"+
		"\u0000\u0000^_\u0005\u0002\u0000\u0000_`\u0003\n\u0005\u0000`a\u0005\u0003"+
		"\u0000\u0000am\u0001\u0000\u0000\u0000bc\u0005#\u0000\u0000cd\u0005\u0011"+
		"\u0000\u0000dm\u0003\f\u0006\u0000ef\u0005#\u0000\u0000fg\u0005\u0012"+
		"\u0000\u0000gm\u0003\f\u0006\u0000hi\u0005\b\u0000\u0000ij\u0003\n\u0005"+
		"\u0000jk\u0005\t\u0000\u0000km\u0001\u0000\u0000\u0000lO\u0001\u0000\u0000"+
		"\u0000lQ\u0001\u0000\u0000\u0000lV\u0001\u0000\u0000\u0000lb\u0001\u0000"+
		"\u0000\u0000le\u0001\u0000\u0000\u0000lh\u0001\u0000\u0000\u0000ms\u0001"+
		"\u0000\u0000\u0000no\n\u0002\u0000\u0000op\u0005\u0013\u0000\u0000pr\u0003"+
		"\n\u0005\u0002qn\u0001\u0000\u0000\u0000ru\u0001\u0000\u0000\u0000sq\u0001"+
		"\u0000\u0000\u0000st\u0001\u0000\u0000\u0000t\u000b\u0001\u0000\u0000"+
		"\u0000us\u0001\u0000\u0000\u0000vw\u0006\u0006\uffff\uffff\u0000w\u007f"+
		"\u0003\u000e\u0007\u0000xy\u0005 \u0000\u0000y\u007f\u0003\f\u0006\u0002"+
		"z{\u0005\b\u0000\u0000{|\u0003\f\u0006\u0000|}\u0005\t\u0000\u0000}\u007f"+
		"\u0001\u0000\u0000\u0000~v\u0001\u0000\u0000\u0000~x\u0001\u0000\u0000"+
		"\u0000~z\u0001\u0000\u0000\u0000\u007f\u009d\u0001\u0000\u0000\u0000\u0080"+
		"\u0081\n\u000b\u0000\u0000\u0081\u0082\u0007\u0000\u0000\u0000\u0082\u009c"+
		"\u0003\f\u0006\f\u0083\u0084\n\n\u0000\u0000\u0084\u0085\u0007\u0001\u0000"+
		"\u0000\u0085\u009c\u0003\f\u0006\u000b\u0086\u0087\n\t\u0000\u0000\u0087"+
		"\u0088\u0005\u0018\u0000\u0000\u0088\u009c\u0003\f\u0006\n\u0089\u008a"+
		"\n\b\u0000\u0000\u008a\u008b\u0005\u0019\u0000\u0000\u008b\u009c\u0003"+
		"\f\u0006\t\u008c\u008d\n\u0007\u0000\u0000\u008d\u008e\u0005\u001a\u0000"+
		"\u0000\u008e\u009c\u0003\f\u0006\b\u008f\u0090\n\u0006\u0000\u0000\u0090"+
		"\u0091\u0005\u001b\u0000\u0000\u0091\u009c\u0003\f\u0006\u0007\u0092\u0093"+
		"\n\u0005\u0000\u0000\u0093\u0094\u0005\u001c\u0000\u0000\u0094\u009c\u0003"+
		"\f\u0006\u0006\u0095\u0096\n\u0004\u0000\u0000\u0096\u0097\u0005\u001d"+
		"\u0000\u0000\u0097\u009c\u0003\f\u0006\u0005\u0098\u0099\n\u0003\u0000"+
		"\u0000\u0099\u009a\u0007\u0002\u0000\u0000\u009a\u009c\u0003\f\u0006\u0004"+
		"\u009b\u0080\u0001\u0000\u0000\u0000\u009b\u0083\u0001\u0000\u0000\u0000"+
		"\u009b\u0086\u0001\u0000\u0000\u0000\u009b\u0089\u0001\u0000\u0000\u0000"+
		"\u009b\u008c\u0001\u0000\u0000\u0000\u009b\u008f\u0001\u0000\u0000\u0000"+
		"\u009b\u0092\u0001\u0000\u0000\u0000\u009b\u0095\u0001\u0000\u0000\u0000"+
		"\u009b\u0098\u0001\u0000\u0000\u0000\u009c\u009f\u0001\u0000\u0000\u0000"+
		"\u009d\u009b\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000\u0000\u0000"+
		"\u009e\r\u0001\u0000\u0000\u0000\u009f\u009d\u0001\u0000\u0000\u0000\u00a0"+
		"\u00a5\u0005%\u0000\u0000\u00a1\u00a5\u0005#\u0000\u0000\u00a2\u00a5\u0005"+
		"!\u0000\u0000\u00a3\u00a5\u0005\"\u0000\u0000\u00a4\u00a0\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a1\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a3\u0001\u0000\u0000\u0000\u00a5\u000f\u0001\u0000"+
		"\u0000\u0000\t\u0019EJls~\u009b\u009d\u00a4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}