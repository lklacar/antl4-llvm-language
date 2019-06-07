grammar Code;

program: function*;

function: functionHead LBRACE functionBody RBRACE;

functionHead: type ID LPAREN arguments RPAREN;

arg: type ID;
arguments: arg? (',' arg)*;

functionBody: (statement | expression)*;

statement
    : assignmentStatement
    | returnStatement
    ;

returnStatement: 'return' expression;

assignmentStatement: type ID EQ expression;

expression
   :  expression POW expression
   |  expression (TIMES | DIV)  expression
   |  expression (PLUS | MINUS) expression
   |  LPAREN expression RPAREN
   |  (PLUS | MINUS)* atom
   | functionCall
   ;


param: expression;
params: param? (',' param)*;

functionCall: ID LPAREN params RPAREN;


atom
    : INT
    | DECIMAL
    | ID
    ;

type
    : 'int'
    | 'double'
    ;

ID: [a-zA-Z]+ DIGIT*;
TIMES: '*';
DIV: '/';
PLUS: '+';
MINUS: '-';
LPAREN: '(';
RPAREN: ')';
POW: '^';
EQ: '=';
LBRACE: '{';
RBRACE: '}';

INT: SIGN DIGIT+;
DECIMAL: INT '.' INT;

fragment DIGIT: [0-9];
fragment SIGN: (MINUS)?;


WS
   : [ \r\n\t] + -> skip
   ;


COMMENT
    :   '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;