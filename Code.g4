grammar Code;

program
    : moduleDefinition (functionDefinition)*
    ;

moduleDefinition: 'module' ID SEMI;

statement
    : assignmentStatement
    ;

assignmentStatement
    : assignmentType ID ':' type EQ expression SEMI
    ;

functionDefinition
    : 'fn' ID LPAREN arguments? RPAREN ('->' type)? LBRACKET functionBody? RBRACKET
    ;

functionBody
    : (statement | expression)+
    |
    ;

arguments
    :   ID ':' type
    |   arguments ',' ID ':' type
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

type
    : 'i32'
    | 'i16'
    | 'i8'
    | 'double'
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