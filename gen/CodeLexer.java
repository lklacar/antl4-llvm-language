// Generated from /home/luka/Projects/antl4-llvm-language/Code.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CodeLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, ID=12, Constant=13, LPAREN=14, RPAREN=15, MUL=16, DIV=17, 
		PLUS=18, MINUS=19, EQ=20, LBRACKET=21, RBRACKET=22, SEMI=23, WS=24, COMMENT=25, 
		LINE_COMMENT=26;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "ID", "Constant", "DOUBLE_CONSTANT", "INTEGER_CONSTANT", 
			"DECIMAL", "DIGIT", "NON_ZERO_DIGIT", "LPAREN", "RPAREN", "MUL", "DIV", 
			"PLUS", "MINUS", "EQ", "LBRACKET", "RBRACKET", "SEMI", "WS", "COMMENT", 
			"LINE_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'module'", "':'", "'fn'", "'->'", "','", "'const'", "'let'", "'i32'", 
			"'i16'", "'i8'", "'double'", null, null, "'('", "')'", "'*'", "'/'", 
			"'+'", "'-'", "'='", "'{'", "'}'", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"ID", "Constant", "LPAREN", "RPAREN", "MUL", "DIV", "PLUS", "MINUS", 
			"EQ", "LBRACKET", "RBRACKET", "SEMI", "WS", "COMMENT", "LINE_COMMENT"
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


	public CodeLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Code.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\34\u00cb\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3"+
		"\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\6\rp\n\r\r\r\16\rq\3"+
		"\r\7\ru\n\r\f\r\16\rx\13\r\3\16\3\16\5\16|\n\16\3\17\7\17\177\n\17\f\17"+
		"\16\17\u0082\13\17\3\17\3\17\7\17\u0086\n\17\f\17\16\17\u0089\13\17\3"+
		"\20\3\20\3\21\3\21\7\21\u008f\n\21\f\21\16\21\u0092\13\21\3\22\3\22\3"+
		"\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3"+
		"\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\6\36\u00ad\n\36\r\36\16\36"+
		"\u00ae\3\36\3\36\3\37\3\37\3\37\3\37\7\37\u00b7\n\37\f\37\16\37\u00ba"+
		"\13\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \7 \u00c5\n \f \16 \u00c8\13"+
		" \3 \3 \3\u00b8\2!\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r"+
		"\31\16\33\17\35\2\37\2!\2#\2%\2\'\20)\21+\22-\23/\24\61\25\63\26\65\27"+
		"\67\309\31;\32=\33?\34\3\2\7\5\2C\\aac|\3\2\62;\3\2\63;\5\2\13\f\17\17"+
		"\"\"\4\2\f\f\17\17\2\u00ce\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2"+
		"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2"+
		"\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\'\3\2\2\2\2)\3\2"+
		"\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3"+
		"\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\3A\3\2"+
		"\2\2\5H\3\2\2\2\7J\3\2\2\2\tM\3\2\2\2\13P\3\2\2\2\rR\3\2\2\2\17X\3\2\2"+
		"\2\21\\\3\2\2\2\23`\3\2\2\2\25d\3\2\2\2\27g\3\2\2\2\31o\3\2\2\2\33{\3"+
		"\2\2\2\35\u0080\3\2\2\2\37\u008a\3\2\2\2!\u008c\3\2\2\2#\u0093\3\2\2\2"+
		"%\u0095\3\2\2\2\'\u0097\3\2\2\2)\u0099\3\2\2\2+\u009b\3\2\2\2-\u009d\3"+
		"\2\2\2/\u009f\3\2\2\2\61\u00a1\3\2\2\2\63\u00a3\3\2\2\2\65\u00a5\3\2\2"+
		"\2\67\u00a7\3\2\2\29\u00a9\3\2\2\2;\u00ac\3\2\2\2=\u00b2\3\2\2\2?\u00c0"+
		"\3\2\2\2AB\7o\2\2BC\7q\2\2CD\7f\2\2DE\7w\2\2EF\7n\2\2FG\7g\2\2G\4\3\2"+
		"\2\2HI\7<\2\2I\6\3\2\2\2JK\7h\2\2KL\7p\2\2L\b\3\2\2\2MN\7/\2\2NO\7@\2"+
		"\2O\n\3\2\2\2PQ\7.\2\2Q\f\3\2\2\2RS\7e\2\2ST\7q\2\2TU\7p\2\2UV\7u\2\2"+
		"VW\7v\2\2W\16\3\2\2\2XY\7n\2\2YZ\7g\2\2Z[\7v\2\2[\20\3\2\2\2\\]\7k\2\2"+
		"]^\7\65\2\2^_\7\64\2\2_\22\3\2\2\2`a\7k\2\2ab\7\63\2\2bc\78\2\2c\24\3"+
		"\2\2\2de\7k\2\2ef\7:\2\2f\26\3\2\2\2gh\7f\2\2hi\7q\2\2ij\7w\2\2jk\7d\2"+
		"\2kl\7n\2\2lm\7g\2\2m\30\3\2\2\2np\t\2\2\2on\3\2\2\2pq\3\2\2\2qo\3\2\2"+
		"\2qr\3\2\2\2rv\3\2\2\2su\5#\22\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2"+
		"\2w\32\3\2\2\2xv\3\2\2\2y|\5\37\20\2z|\5\35\17\2{y\3\2\2\2{z\3\2\2\2|"+
		"\34\3\2\2\2}\177\5%\23\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080"+
		"\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0087\7\60"+
		"\2\2\u0084\u0086\5#\22\2\u0085\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087"+
		"\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\36\3\2\2\2\u0089\u0087\3\2\2"+
		"\2\u008a\u008b\5!\21\2\u008b \3\2\2\2\u008c\u0090\5%\23\2\u008d\u008f"+
		"\5#\22\2\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090"+
		"\u0091\3\2\2\2\u0091\"\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\t\3\2\2"+
		"\u0094$\3\2\2\2\u0095\u0096\t\4\2\2\u0096&\3\2\2\2\u0097\u0098\7*\2\2"+
		"\u0098(\3\2\2\2\u0099\u009a\7+\2\2\u009a*\3\2\2\2\u009b\u009c\7,\2\2\u009c"+
		",\3\2\2\2\u009d\u009e\7\61\2\2\u009e.\3\2\2\2\u009f\u00a0\7-\2\2\u00a0"+
		"\60\3\2\2\2\u00a1\u00a2\7/\2\2\u00a2\62\3\2\2\2\u00a3\u00a4\7?\2\2\u00a4"+
		"\64\3\2\2\2\u00a5\u00a6\7}\2\2\u00a6\66\3\2\2\2\u00a7\u00a8\7\177\2\2"+
		"\u00a88\3\2\2\2\u00a9\u00aa\7=\2\2\u00aa:\3\2\2\2\u00ab\u00ad\t\5\2\2"+
		"\u00ac\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af"+
		"\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\b\36\2\2\u00b1<\3\2\2\2\u00b2"+
		"\u00b3\7\61\2\2\u00b3\u00b4\7,\2\2\u00b4\u00b8\3\2\2\2\u00b5\u00b7\13"+
		"\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b8"+
		"\u00b6\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bc\7,"+
		"\2\2\u00bc\u00bd\7\61\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\b\37\2\2\u00bf"+
		">\3\2\2\2\u00c0\u00c1\7\61\2\2\u00c1\u00c2\7\61\2\2\u00c2\u00c6\3\2\2"+
		"\2\u00c3\u00c5\n\6\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4"+
		"\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9"+
		"\u00ca\b \2\2\u00ca@\3\2\2\2\f\2qv{\u0080\u0087\u0090\u00ae\u00b8\u00c6"+
		"\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}