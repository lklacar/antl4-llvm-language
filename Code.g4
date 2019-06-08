grammar Code;

program: function*;

function: functionHead LBRACE functionBody RBRACE;

functionHead: type ID LPAREN arguments RPAREN;

arg: type ID;
arguments: arg? (',' arg)*;

functionBody: (statement)*;

statement
    : assignmentStatement
    | returnStatement
    ;

returnStatement: 'return' expression;

assignmentStatement: type ID EQ expression;

expression
   :  expression op=POW expression            #expressionPow
   | functionCall                             #expressionFunctionCall
   |  expression op=(TIMES | DIV)  expression #expressionMul
   |  expression op=(PLUS | MINUS) expression #expressionAdd
   |  LPAREN expression RPAREN                #expressionNested
   |  (PLUS | MINUS)* atom                    #expressionNumber
   ;


param: expression;
params: param? (',' param)*;

functionCall: ID LPAREN params RPAREN;


atom
    : op=INT
    | op=DECIMAL
    | op=ID
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