grammar grammarJava;

DEF: 'def';
RETURN: 'return';
PRINT: 'print';

IDCLASS: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBERS: [0-9]+;

PLUS : '+' ;
MINUS : '-' ;
MULTIPLY : '*' ;
DIVIDE : '/';
ASIGNAN: '=';
EQUAL: '==';
LPAREN: '(';
RPAREN: ')';
COLON: ':';
COMMA: ',';

BLANKSPACE: ' ' -> skip;
TAB: '\t' -> skip;
RCAR: ('\r'? '\n')+ -> skip;

program: (function | print)+;

print: PRINT LPAREN callfunction RPAREN RCAR?;

callfunction: IDCLASS LPAREN parameters? RPAREN;

function: DEF IDCLASS LPAREN parameters? RPAREN COLON block;

parameters: parameter (COMMA parameter)*;

parameter: IDCLASS | NUMBERS;

block: (statement RCAR?)+;

statement: assignment | returnStmt | printStmt;

assignment: IDCLASS ASIGNAN expression;

expression: IDCLASS | NUMBERS | expression (PLUS|MINUS|DIVIDE|MULTIPLY) expression;

returnStmt: RETURN expression;

printStmt: PRINT LPAREN expression RPAREN;
