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
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, LABEL=41, LABELUPPER=42, NUMBER=43, REAL=44, TYPE=45, 
		WS=46, COMMENT=47, LINE_COMMENT=48;
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
			null, "'contract'", "'{'", "'}'", "'int'", "'bool'", "'string'", "'address'", 
			"'('", "'->'", "')'", "'constraint'", "'function'", "'payable'", "'constructor'", 
			"'skip'", "'require'", "'if'", "'else'", "'='", "'['", "']'", "'!'", 
			"';'", "'*'", "'/'", "'+'", "'-'", "'=='", "'!='", "'<'", "'>'", "'<='", 
			"'>='", "'and'", "'&&'", "'not'", "'true'", "'True'", "'false'", "'False'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "LABEL", "LABELUPPER", "NUMBER", "REAL", 
			"TYPE", "WS", "COMMENT", "LINE_COMMENT"
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
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 23024L) != 0) );
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
	public static class BoolDeclContext extends DeclExprContext {
		public Token var;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public BoolDeclContext(DeclExprContext ctx) { copyFrom(ctx); }
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
	public static class MapAddrDeclIntContext extends DeclExprContext {
		public Token var;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public MapAddrDeclIntContext(DeclExprContext ctx) { copyFrom(ctx); }
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
			setState(77);
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
				_localctx = new BoolDeclContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				match(T__4);
				setState(30);
				((BoolDeclContext)_localctx).var = match(LABEL);
				}
				break;
			case 3:
				_localctx = new StrDeclContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(31);
				match(T__5);
				setState(32);
				((StrDeclContext)_localctx).var = match(LABEL);
				}
				break;
			case 4:
				_localctx = new AddrDeclContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(33);
				match(T__6);
				setState(34);
				((AddrDeclContext)_localctx).var = match(LABEL);
				}
				break;
			case 5:
				_localctx = new MapAddrDeclIntContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(35);
				match(T__7);
				setState(36);
				match(T__6);
				setState(37);
				match(T__8);
				setState(38);
				match(T__3);
				setState(39);
				match(T__9);
				setState(40);
				((MapAddrDeclIntContext)_localctx).var = match(LABEL);
				}
				break;
			case 6:
				_localctx = new ConstrDeclContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(41);
				match(T__10);
				setState(42);
				((ConstrDeclContext)_localctx).name = match(LABEL);
				setState(43);
				match(T__7);
				setState(44);
				((ConstrDeclContext)_localctx).args = argsExpr();
				setState(45);
				match(T__9);
				setState(46);
				match(T__1);
				setState(47);
				((ConstrDeclContext)_localctx).cmds = cmdExpr(0);
				setState(48);
				match(T__2);
				}
				break;
			case 7:
				_localctx = new PayableFunDeclContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(50);
				match(T__11);
				setState(51);
				((PayableFunDeclContext)_localctx).name = match(LABEL);
				setState(52);
				match(T__7);
				setState(53);
				((PayableFunDeclContext)_localctx).args = argsExpr();
				setState(54);
				match(T__9);
				setState(55);
				match(T__12);
				setState(56);
				match(T__1);
				setState(57);
				((PayableFunDeclContext)_localctx).cmds = cmdExpr(0);
				setState(58);
				match(T__2);
				}
				break;
			case 8:
				_localctx = new NonPayableFunDeclContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(60);
				match(T__11);
				setState(61);
				((NonPayableFunDeclContext)_localctx).name = match(LABEL);
				setState(62);
				match(T__7);
				setState(63);
				((NonPayableFunDeclContext)_localctx).args = argsExpr();
				setState(64);
				match(T__9);
				setState(65);
				match(T__1);
				setState(66);
				((NonPayableFunDeclContext)_localctx).cmds = cmdExpr(0);
				setState(67);
				match(T__2);
				}
				break;
			case 9:
				_localctx = new ConstructorDeclContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(69);
				match(T__13);
				setState(70);
				match(T__7);
				setState(71);
				((ConstructorDeclContext)_localctx).args = argsExpr();
				setState(72);
				match(T__9);
				setState(73);
				match(T__1);
				setState(74);
				((ConstructorDeclContext)_localctx).cmds = cmdExpr(0);
				setState(75);
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
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LABEL) {
				{
				{
				setState(79);
				argExpr();
				}
				}
				setState(84);
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
			setState(85);
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
	public static class IfCmdContext extends CmdExprContext {
		public ExpressionContext condition;
		public CmdExprContext ifcmd;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public CmdExprContext cmdExpr() {
			return getRuleContext(CmdExprContext.class,0);
		}
		public IfCmdContext(CmdExprContext ctx) { copyFrom(ctx); }
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
	@SuppressWarnings("CheckReturnValue")
	public static class AssignMapCmdContext extends CmdExprContext {
		public Token var;
		public ExpressionContext index;
		public ExpressionContext child;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AssignMapCmdContext(CmdExprContext ctx) { copyFrom(ctx); }
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
			setState(131);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				_localctx = new SkipCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(88);
				match(T__14);
				}
				break;
			case 2:
				{
				_localctx = new RequireCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(89);
				match(T__15);
				setState(90);
				match(T__7);
				setState(91);
				((RequireCmdContext)_localctx).child = expression(0);
				setState(92);
				match(T__9);
				}
				break;
			case 3:
				{
				_localctx = new IfelseCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(94);
				match(T__16);
				setState(95);
				match(T__7);
				setState(96);
				((IfelseCmdContext)_localctx).condition = expression(0);
				setState(97);
				match(T__9);
				setState(98);
				match(T__1);
				setState(99);
				((IfelseCmdContext)_localctx).ifcmd = cmdExpr(0);
				setState(100);
				match(T__2);
				setState(101);
				match(T__17);
				setState(102);
				match(T__1);
				setState(103);
				((IfelseCmdContext)_localctx).elsecmd = cmdExpr(0);
				setState(104);
				match(T__2);
				}
				break;
			case 4:
				{
				_localctx = new IfCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(106);
				match(T__16);
				setState(107);
				match(T__7);
				setState(108);
				((IfCmdContext)_localctx).condition = expression(0);
				setState(109);
				match(T__9);
				setState(110);
				match(T__1);
				setState(111);
				((IfCmdContext)_localctx).ifcmd = cmdExpr(0);
				setState(112);
				match(T__2);
				}
				break;
			case 5:
				{
				_localctx = new AssignCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(114);
				((AssignCmdContext)_localctx).var = match(LABEL);
				setState(115);
				match(T__18);
				setState(116);
				((AssignCmdContext)_localctx).child = expression(0);
				}
				break;
			case 6:
				{
				_localctx = new AssignMapCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(117);
				((AssignMapCmdContext)_localctx).var = match(LABEL);
				setState(118);
				match(T__19);
				setState(119);
				((AssignMapCmdContext)_localctx).index = expression(0);
				setState(120);
				match(T__20);
				setState(121);
				match(T__18);
				setState(122);
				((AssignMapCmdContext)_localctx).child = expression(0);
				}
				break;
			case 7:
				{
				_localctx = new SendCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(124);
				((SendCmdContext)_localctx).sender = match(LABEL);
				setState(125);
				match(T__21);
				setState(126);
				((SendCmdContext)_localctx).amount = expression(0);
				}
				break;
			case 8:
				{
				_localctx = new GroupCmdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(127);
				match(T__7);
				setState(128);
				cmdExpr(0);
				setState(129);
				match(T__9);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(138);
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
					setState(133);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(134);
					match(T__22);
					setState(135);
					((SeqCmdContext)_localctx).seq2 = cmdExpr(2);
					}
					} 
				}
				setState(140);
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
	public static class MapExprContext extends ExpressionContext {
		public Token mapVar;
		public ExpressionContext index;
		public TerminalNode LABEL() { return getToken(TxScriptParser.LABEL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public MapExprContext(ExpressionContext ctx) { copyFrom(ctx); }
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
			setState(154);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				_localctx = new ConstExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(142);
				((ConstExprContext)_localctx).child = constantExpr();
				}
				break;
			case 2:
				{
				_localctx = new MapExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(143);
				((MapExprContext)_localctx).mapVar = match(LABEL);
				setState(144);
				match(T__19);
				setState(145);
				((MapExprContext)_localctx).index = expression(0);
				setState(146);
				match(T__20);
				}
				break;
			case 3:
				{
				_localctx = new NotExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(148);
				match(T__35);
				setState(149);
				((NotExprContext)_localctx).child = expression(2);
				}
				break;
			case 4:
				{
				_localctx = new GroupExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(150);
				match(T__7);
				setState(151);
				((GroupExprContext)_localctx).child = expression(0);
				setState(152);
				match(T__9);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(185);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(183);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new MultDivEqExprContext(new ExpressionContext(_parentctx, _parentState));
						((MultDivEqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(156);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(157);
						((MultDivEqExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__23 || _la==T__24) ) {
							((MultDivEqExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(158);
						((MultDivEqExprContext)_localctx).right = expression(12);
						}
						break;
					case 2:
						{
						_localctx = new SumSubEqExprContext(new ExpressionContext(_parentctx, _parentState));
						((SumSubEqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(159);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(160);
						((SumSubEqExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__25 || _la==T__26) ) {
							((SumSubEqExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(161);
						((SumSubEqExprContext)_localctx).right = expression(11);
						}
						break;
					case 3:
						{
						_localctx = new EqExprContext(new ExpressionContext(_parentctx, _parentState));
						((EqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(162);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						{
						setState(163);
						match(T__27);
						}
						setState(164);
						((EqExprContext)_localctx).right = expression(10);
						}
						break;
					case 4:
						{
						_localctx = new NeqExprContext(new ExpressionContext(_parentctx, _parentState));
						((NeqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(165);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						{
						setState(166);
						match(T__28);
						}
						setState(167);
						((NeqExprContext)_localctx).right = expression(9);
						}
						break;
					case 5:
						{
						_localctx = new LessExprContext(new ExpressionContext(_parentctx, _parentState));
						((LessExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(168);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						{
						setState(169);
						match(T__29);
						}
						setState(170);
						((LessExprContext)_localctx).right = expression(8);
						}
						break;
					case 6:
						{
						_localctx = new GreaterExprContext(new ExpressionContext(_parentctx, _parentState));
						((GreaterExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(171);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						{
						setState(172);
						match(T__30);
						}
						setState(173);
						((GreaterExprContext)_localctx).right = expression(7);
						}
						break;
					case 7:
						{
						_localctx = new LessEqExprContext(new ExpressionContext(_parentctx, _parentState));
						((LessEqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(174);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						{
						setState(175);
						match(T__31);
						}
						setState(176);
						((LessEqExprContext)_localctx).right = expression(6);
						}
						break;
					case 8:
						{
						_localctx = new GreaterEqExprContext(new ExpressionContext(_parentctx, _parentState));
						((GreaterEqExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(177);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						{
						setState(178);
						match(T__32);
						}
						setState(179);
						((GreaterEqExprContext)_localctx).right = expression(5);
						}
						break;
					case 9:
						{
						_localctx = new AndExprContext(new ExpressionContext(_parentctx, _parentState));
						((AndExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(180);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(181);
						_la = _input.LA(1);
						if ( !(_la==T__33 || _la==T__34) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(182);
						((AndExprContext)_localctx).right = expression(4);
						}
						break;
					}
					} 
				}
				setState(187);
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
		int _la;
		try {
			setState(192);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				_localctx = new NumberConstantContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(188);
				((NumberConstantContext)_localctx).v = match(NUMBER);
				}
				break;
			case LABEL:
				_localctx = new StrConstantContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(189);
				((StrConstantContext)_localctx).v = match(LABEL);
				}
				break;
			case T__36:
			case T__37:
				_localctx = new TrueConstantContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(190);
				((TrueConstantContext)_localctx).v = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==T__36 || _la==T__37) ) {
					((TrueConstantContext)_localctx).v = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case T__38:
			case T__39:
				_localctx = new FalseConstantContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(191);
				((FalseConstantContext)_localctx).v = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==T__38 || _la==T__39) ) {
					((FalseConstantContext)_localctx).v = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
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
		"\u0004\u00010\u00c3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002N\b\u0002\u0001\u0003\u0005\u0003Q\b\u0003\n\u0003"+
		"\f\u0003T\t\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005\u0084\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005\u0089"+
		"\b\u0005\n\u0005\f\u0005\u008c\t\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u009b\b\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006\u00b8\b\u0006\n\u0006"+
		"\f\u0006\u00bb\t\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0003\u0007\u00c1\b\u0007\u0001\u0007\u0000\u0002\n\f\b\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0000\u0005\u0001\u0000\u0018\u0019\u0001\u0000\u001a"+
		"\u001b\u0001\u0000\"#\u0001\u0000%&\u0001\u0000\'(\u00db\u0000\u0010\u0001"+
		"\u0000\u0000\u0000\u0002\u0017\u0001\u0000\u0000\u0000\u0004M\u0001\u0000"+
		"\u0000\u0000\u0006R\u0001\u0000\u0000\u0000\bU\u0001\u0000\u0000\u0000"+
		"\n\u0083\u0001\u0000\u0000\u0000\f\u009a\u0001\u0000\u0000\u0000\u000e"+
		"\u00c0\u0001\u0000\u0000\u0000\u0010\u0011\u0005\u0001\u0000\u0000\u0011"+
		"\u0012\u0005*\u0000\u0000\u0012\u0013\u0005\u0002\u0000\u0000\u0013\u0014"+
		"\u0003\u0002\u0001\u0000\u0014\u0015\u0005\u0003\u0000\u0000\u0015\u0001"+
		"\u0001\u0000\u0000\u0000\u0016\u0018\u0003\u0004\u0002\u0000\u0017\u0016"+
		"\u0001\u0000\u0000\u0000\u0018\u0019\u0001\u0000\u0000\u0000\u0019\u0017"+
		"\u0001\u0000\u0000\u0000\u0019\u001a\u0001\u0000\u0000\u0000\u001a\u0003"+
		"\u0001\u0000\u0000\u0000\u001b\u001c\u0005\u0004\u0000\u0000\u001cN\u0005"+
		")\u0000\u0000\u001d\u001e\u0005\u0005\u0000\u0000\u001eN\u0005)\u0000"+
		"\u0000\u001f \u0005\u0006\u0000\u0000 N\u0005)\u0000\u0000!\"\u0005\u0007"+
		"\u0000\u0000\"N\u0005)\u0000\u0000#$\u0005\b\u0000\u0000$%\u0005\u0007"+
		"\u0000\u0000%&\u0005\t\u0000\u0000&\'\u0005\u0004\u0000\u0000\'(\u0005"+
		"\n\u0000\u0000(N\u0005)\u0000\u0000)*\u0005\u000b\u0000\u0000*+\u0005"+
		")\u0000\u0000+,\u0005\b\u0000\u0000,-\u0003\u0006\u0003\u0000-.\u0005"+
		"\n\u0000\u0000./\u0005\u0002\u0000\u0000/0\u0003\n\u0005\u000001\u0005"+
		"\u0003\u0000\u00001N\u0001\u0000\u0000\u000023\u0005\f\u0000\u000034\u0005"+
		")\u0000\u000045\u0005\b\u0000\u000056\u0003\u0006\u0003\u000067\u0005"+
		"\n\u0000\u000078\u0005\r\u0000\u000089\u0005\u0002\u0000\u00009:\u0003"+
		"\n\u0005\u0000:;\u0005\u0003\u0000\u0000;N\u0001\u0000\u0000\u0000<=\u0005"+
		"\f\u0000\u0000=>\u0005)\u0000\u0000>?\u0005\b\u0000\u0000?@\u0003\u0006"+
		"\u0003\u0000@A\u0005\n\u0000\u0000AB\u0005\u0002\u0000\u0000BC\u0003\n"+
		"\u0005\u0000CD\u0005\u0003\u0000\u0000DN\u0001\u0000\u0000\u0000EF\u0005"+
		"\u000e\u0000\u0000FG\u0005\b\u0000\u0000GH\u0003\u0006\u0003\u0000HI\u0005"+
		"\n\u0000\u0000IJ\u0005\u0002\u0000\u0000JK\u0003\n\u0005\u0000KL\u0005"+
		"\u0003\u0000\u0000LN\u0001\u0000\u0000\u0000M\u001b\u0001\u0000\u0000"+
		"\u0000M\u001d\u0001\u0000\u0000\u0000M\u001f\u0001\u0000\u0000\u0000M"+
		"!\u0001\u0000\u0000\u0000M#\u0001\u0000\u0000\u0000M)\u0001\u0000\u0000"+
		"\u0000M2\u0001\u0000\u0000\u0000M<\u0001\u0000\u0000\u0000ME\u0001\u0000"+
		"\u0000\u0000N\u0005\u0001\u0000\u0000\u0000OQ\u0003\b\u0004\u0000PO\u0001"+
		"\u0000\u0000\u0000QT\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000"+
		"RS\u0001\u0000\u0000\u0000S\u0007\u0001\u0000\u0000\u0000TR\u0001\u0000"+
		"\u0000\u0000UV\u0005)\u0000\u0000V\t\u0001\u0000\u0000\u0000WX\u0006\u0005"+
		"\uffff\uffff\u0000X\u0084\u0005\u000f\u0000\u0000YZ\u0005\u0010\u0000"+
		"\u0000Z[\u0005\b\u0000\u0000[\\\u0003\f\u0006\u0000\\]\u0005\n\u0000\u0000"+
		"]\u0084\u0001\u0000\u0000\u0000^_\u0005\u0011\u0000\u0000_`\u0005\b\u0000"+
		"\u0000`a\u0003\f\u0006\u0000ab\u0005\n\u0000\u0000bc\u0005\u0002\u0000"+
		"\u0000cd\u0003\n\u0005\u0000de\u0005\u0003\u0000\u0000ef\u0005\u0012\u0000"+
		"\u0000fg\u0005\u0002\u0000\u0000gh\u0003\n\u0005\u0000hi\u0005\u0003\u0000"+
		"\u0000i\u0084\u0001\u0000\u0000\u0000jk\u0005\u0011\u0000\u0000kl\u0005"+
		"\b\u0000\u0000lm\u0003\f\u0006\u0000mn\u0005\n\u0000\u0000no\u0005\u0002"+
		"\u0000\u0000op\u0003\n\u0005\u0000pq\u0005\u0003\u0000\u0000q\u0084\u0001"+
		"\u0000\u0000\u0000rs\u0005)\u0000\u0000st\u0005\u0013\u0000\u0000t\u0084"+
		"\u0003\f\u0006\u0000uv\u0005)\u0000\u0000vw\u0005\u0014\u0000\u0000wx"+
		"\u0003\f\u0006\u0000xy\u0005\u0015\u0000\u0000yz\u0005\u0013\u0000\u0000"+
		"z{\u0003\f\u0006\u0000{\u0084\u0001\u0000\u0000\u0000|}\u0005)\u0000\u0000"+
		"}~\u0005\u0016\u0000\u0000~\u0084\u0003\f\u0006\u0000\u007f\u0080\u0005"+
		"\b\u0000\u0000\u0080\u0081\u0003\n\u0005\u0000\u0081\u0082\u0005\n\u0000"+
		"\u0000\u0082\u0084\u0001\u0000\u0000\u0000\u0083W\u0001\u0000\u0000\u0000"+
		"\u0083Y\u0001\u0000\u0000\u0000\u0083^\u0001\u0000\u0000\u0000\u0083j"+
		"\u0001\u0000\u0000\u0000\u0083r\u0001\u0000\u0000\u0000\u0083u\u0001\u0000"+
		"\u0000\u0000\u0083|\u0001\u0000\u0000\u0000\u0083\u007f\u0001\u0000\u0000"+
		"\u0000\u0084\u008a\u0001\u0000\u0000\u0000\u0085\u0086\n\u0002\u0000\u0000"+
		"\u0086\u0087\u0005\u0017\u0000\u0000\u0087\u0089\u0003\n\u0005\u0002\u0088"+
		"\u0085\u0001\u0000\u0000\u0000\u0089\u008c\u0001\u0000\u0000\u0000\u008a"+
		"\u0088\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000\u008b"+
		"\u000b\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000\u0000\u008d"+
		"\u008e\u0006\u0006\uffff\uffff\u0000\u008e\u009b\u0003\u000e\u0007\u0000"+
		"\u008f\u0090\u0005)\u0000\u0000\u0090\u0091\u0005\u0014\u0000\u0000\u0091"+
		"\u0092\u0003\f\u0006\u0000\u0092\u0093\u0005\u0015\u0000\u0000\u0093\u009b"+
		"\u0001\u0000\u0000\u0000\u0094\u0095\u0005$\u0000\u0000\u0095\u009b\u0003"+
		"\f\u0006\u0002\u0096\u0097\u0005\b\u0000\u0000\u0097\u0098\u0003\f\u0006"+
		"\u0000\u0098\u0099\u0005\n\u0000\u0000\u0099\u009b\u0001\u0000\u0000\u0000"+
		"\u009a\u008d\u0001\u0000\u0000\u0000\u009a\u008f\u0001\u0000\u0000\u0000"+
		"\u009a\u0094\u0001\u0000\u0000\u0000\u009a\u0096\u0001\u0000\u0000\u0000"+
		"\u009b\u00b9\u0001\u0000\u0000\u0000\u009c\u009d\n\u000b\u0000\u0000\u009d"+
		"\u009e\u0007\u0000\u0000\u0000\u009e\u00b8\u0003\f\u0006\f\u009f\u00a0"+
		"\n\n\u0000\u0000\u00a0\u00a1\u0007\u0001\u0000\u0000\u00a1\u00b8\u0003"+
		"\f\u0006\u000b\u00a2\u00a3\n\t\u0000\u0000\u00a3\u00a4\u0005\u001c\u0000"+
		"\u0000\u00a4\u00b8\u0003\f\u0006\n\u00a5\u00a6\n\b\u0000\u0000\u00a6\u00a7"+
		"\u0005\u001d\u0000\u0000\u00a7\u00b8\u0003\f\u0006\t\u00a8\u00a9\n\u0007"+
		"\u0000\u0000\u00a9\u00aa\u0005\u001e\u0000\u0000\u00aa\u00b8\u0003\f\u0006"+
		"\b\u00ab\u00ac\n\u0006\u0000\u0000\u00ac\u00ad\u0005\u001f\u0000\u0000"+
		"\u00ad\u00b8\u0003\f\u0006\u0007\u00ae\u00af\n\u0005\u0000\u0000\u00af"+
		"\u00b0\u0005 \u0000\u0000\u00b0\u00b8\u0003\f\u0006\u0006\u00b1\u00b2"+
		"\n\u0004\u0000\u0000\u00b2\u00b3\u0005!\u0000\u0000\u00b3\u00b8\u0003"+
		"\f\u0006\u0005\u00b4\u00b5\n\u0003\u0000\u0000\u00b5\u00b6\u0007\u0002"+
		"\u0000\u0000\u00b6\u00b8\u0003\f\u0006\u0004\u00b7\u009c\u0001\u0000\u0000"+
		"\u0000\u00b7\u009f\u0001\u0000\u0000\u0000\u00b7\u00a2\u0001\u0000\u0000"+
		"\u0000\u00b7\u00a5\u0001\u0000\u0000\u0000\u00b7\u00a8\u0001\u0000\u0000"+
		"\u0000\u00b7\u00ab\u0001\u0000\u0000\u0000\u00b7\u00ae\u0001\u0000\u0000"+
		"\u0000\u00b7\u00b1\u0001\u0000\u0000\u0000\u00b7\u00b4\u0001\u0000\u0000"+
		"\u0000\u00b8\u00bb\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000"+
		"\u0000\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba\r\u0001\u0000\u0000\u0000"+
		"\u00bb\u00b9\u0001\u0000\u0000\u0000\u00bc\u00c1\u0005+\u0000\u0000\u00bd"+
		"\u00c1\u0005)\u0000\u0000\u00be\u00c1\u0007\u0003\u0000\u0000\u00bf\u00c1"+
		"\u0007\u0004\u0000\u0000\u00c0\u00bc\u0001\u0000\u0000\u0000\u00c0\u00bd"+
		"\u0001\u0000\u0000\u0000\u00c0\u00be\u0001\u0000\u0000\u0000\u00c0\u00bf"+
		"\u0001\u0000\u0000\u0000\u00c1\u000f\u0001\u0000\u0000\u0000\t\u0019M"+
		"R\u0083\u008a\u009a\u00b7\u00b9\u00c0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}