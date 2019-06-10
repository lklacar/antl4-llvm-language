grammar Code;

program
    : (functionDefinition)*
    ;

statement
    : assignmentStatement
    ;

assignmentStatement
    : assignmentType ID ':' TYPE EQ expression SEMI
    ;

functionDefinition
    : 'fn' ID LPAREN arguments? RPAREN ('->' TYPE)? LBRACKET (statement | expression)* RBRACKET
    ;

arguments
    :   ID ':' TYPE
    |   arguments ',' ID ':' TYPE
    ;

expression
   : expression op=(MUL | DIV)  expression   #expressionMul
   | expression op=(PLUS | MINUS) expression #expressionAdd
   | LPAREN expression RPAREN                #expressionNested
   | (PLUS | MINUS)* atom                    #expressionNumber
   ;

atom
    : op=Constant
    | op=ID
    ;

assignmentType
    : 'const'
    | 'let'
    ;

TYPE
    : 'i32'
    | 'i16'
    | 'i8'
    | 'double'
    | 'bool'
    ;

ID: [a-zA-Z_]+ DIGIT*;

Constant
    :   INTEGER_CONSTANT
    |   DOUBLE_CONSTANT
    ;

fragment
DOUBLE_CONSTANT
    : NON_ZERO_DIGIT* '.' DIGIT*
    ;

fragment
INTEGER_CONSTANT
    :   DECIMAL
    ;

fragment
DECIMAL
    :   NON_ZERO_DIGIT DIGIT*
    ;

fragment
DIGIT
    :   [0-9]
    ;
fragment
NON_ZERO_DIGIT
    :   [1-9]
    ;

LPAREN: '(';
RPAREN: ')';
MUL: '*';
DIV: '/';
PLUS: '+';
MINUS: '-';
EQ: '=';
LBRACKET: '{';
RBRACKET: '}';
SEMI: ';';

WS
   : [ \r\n\t] + -> skip
   ;

COMMENT
    :   '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;