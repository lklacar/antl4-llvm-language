grammar Code;

program : functionDefinition*;

functionDefinition : FUNCTION Identifier LPAREN params RPAREN LBRACE functionBody RBRACE;

functionBody: (statement | expr)*;

expr: add value
    | expr mult expr
    | expr add expr
    | value
    ;
value: Identifier
     | NUMBER
     | '(' expr ')'
     ;
add: '+' | '-';
mult: '*' | '/';




statement
    : functionCall
    ;

arguments
    :   ( argument ( COMMA argument )* )?
    ;

argument
    :   Identifier | NUMBER
    ;

params
    :   ( param ( COMMA param )* )?
    ;

param
    :   INT Identifier
    ;

functionCall: Identifier LPAREN arguments RPAREN SEMI;


NUMBER: [0-9]+;

FUNCTION : 'function';
INT : 'int';

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
SEMI : ';';
COMMA : ',';

ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';

OPERATION:
    ADD | SUB | MUL | DIV;


Identifier
	:	Letter LetterOrDigit*
	;

fragment
Letter
	:	[a-zA-Z$_]
	;

fragment
LetterOrDigit
	:	[a-zA-Z0-9$_]
		{Character.isJavaIdentifierPart(Character.toCodePoint((char)_input.LA(-2), (char)_input.LA(-1)))}?
	;

WS  :  [ \t\r\n\u000C]+ -> skip
    ;

COMMENT
    :   '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;