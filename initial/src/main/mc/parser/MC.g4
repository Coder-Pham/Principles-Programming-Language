grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
	language = Python3;
}

// program: mctype 'main' LB RB (LP RP | block_statement?) EOF;

program: declaration* EOF;

declaration: func_declare | var_declare;
//-----------------------------------------------------------------------------------------------------

//--------------------------------- KEYWORDS --------------------------------------
/* keywords */
Break: 'break';
Continue: 'continue';
Do: 'do';
While: 'while';
If: 'if';
Else: 'else';
For: 'for';
Return: 'return';

TRUE: 'true';
FALSE: 'false';
BooleanLIT: FALSE | TRUE;

ADD: '+';
SUB: '-';
DIV: '/';
MUL: '*';
MOD: '%';
AND: '&&';
NOT: '!';
OR: '||';
EQ: '==';
NOTEQ: '!=';
LT: '<';
LEQ: '<=';
GT: '>';
GEQ: '>=';
ASSIGN: '=';

BOOLTYPE: 'boolean';
INTTYPE: 'int';
VOIDTYPE: 'void';
FLOATTYPE: 'float';
STRINGTYPE: 'string';

BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

fragment LETTER: [a-zA-Z_];

fragment DIGIT: [0-9];

ID: LETTER (LETTER | DIGIT)*;

IntLIT: DIGIT+;

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

COMMA: ',';

LS: '[';

RS: ']';

FloatLIT: ((DIGIT+ '.'? DIGIT*) | (DIGIT* '.'? DIGIT+)) (
		[eE][-+]? DIGIT+
	)?;

fragment Escapesequence:
	| '\\"'
	| '\\\\'
	| '\\b'
	| '\\f'
	| '\\n'
	| '\\r'
	| '\\t'
	| '\'';

// StringLIT: '"' ([\b\t\f\\] | ~[\r\n"] | '\'')* '"';
StringLIT: '"' ( ~[\\\r\n"] | ( '\\' [btf'\\]))* '"';

LITs: IntLIT | BooleanLIT | FloatLIT | StringLIT;

// --------------------------------------------------------------------------------------------

ERROR_CHAR: ~["];
UNCLOSE_STRING:
	'"' (('\\' [btnfr'\\] | ~[\b\t\f\r\n\\"]) | '\n')*;
// UNCLOSE_STRING: '"' ~[\\"]* ( [\r\n] | '\0');
ILLEGAL_ESCAPE: '"' ( ~[\\]* ( '\\' ~[btf"'\\]));

// --------------------------------------- STATEMENTS -------------------------------------------

array_type: primitive_type LS IntLIT RS;

element_of_array: ID LS (IntLIT | ID) RS;

variable: (ID LS IntLIT RS) | ID;

multi_var: variable (COMMA variable)*;

var_declare: primitive_type multi_var SEMI;

input_parameter: primitive_type ID LB RB;
output_parameter: primitive_type LB RB;

array_point: input_parameter | output_parameter;

para_declare: primitive_type ID (LB RB)?;
multi_para: para_declare (COMMA para_declare)*;

//---------------------------------------------------------------------------------

expression:
	LB expression RB
	| expression LS expression RS
	| expression_SB (LS | RS)
	| assoc_expression
	| relational_expression (LT | LEQ | GT | GEQ) relational_expression
	| equality_expression (EQ | NOTEQ) equality_expression
	| <assoc = left> expression AND expression
	| <assoc = left> expression OR expression
	| <assoc = right> expression ASSIGN expression
	| operands;

assoc_expression:
	LB expression RB
	| assoc_expression LS assoc_expression RS
	| <assoc = left> assoc_expression (ADD | SUB) assoc_expression
	| <assoc = left> assoc_expression (MUL | DIV | MOD) assoc_expression
	| <assoc = right> (SUB | NOT) assoc_expression
	| operands;

expression_SB:
	LB expression RB
	| expression_SB LS expression_SB RS
	| relational_expression (LT | LEQ | GT | GEQ) relational_expression
	| equality_expression (EQ | NOTEQ) equality_expression
	| <assoc = left> expression_SB (ADD | SUB) expression_SB
	| <assoc = left> expression_SB (MUL | DIV | MOD) expression_SB
	| <assoc = right> (SUB | NOT) expression_SB
	| <assoc = left> expression_SB AND expression_SB
	| <assoc = left> expression_SB OR expression_SB
	| <assoc = right> expression_SB ASSIGN expression_SB
	| operands;

relational_expression:
	LB expression RB
	| relational_expression LS relational_expression RS
	| <assoc = left> relational_expression (ADD | SUB) relational_expression
	| <assoc = left> relational_expression (MUL | DIV | MOD) relational_expression
	| <assoc = right> (SUB | NOT) relational_expression
	| operands;

equality_expression:
	LB expression RB
	| equality_expression LS equality_expression RS
	| <assoc = right> (SUB | NOT) equality_expression
	| <assoc = left> equality_expression (ADD | SUB) equality_expression
	| <assoc = left> equality_expression (MUL | DIV | MOD) equality_expression
	| relational_expression (LT | LEQ | GT | GEQ) relational_expression
	| operands;

index_expression: expression LS expression RS;
invocation_expression: function_call;
list_expression: (expression (COMMA expression)*)?;
//---------------------------------------------------------------------------------

function_call: ID LB list_expression RB;

// ! Dont know why LITS & BooleanLIT dont work as expect
// operands: LITs | function_call | element_of_array | ID;
operands: IntLIT | FALSE | TRUE | FloatLIT | StringLIT | ID | function_call | element_of_array;
//---------------------------------------------------------------------------------
declare: var_declare*;

break_stmt: Break SEMI;
continue_stmt: Continue SEMI;
return_stmt: Return expression? SEMI;
expression_stmt: expression SEMI;
for_stmt:
	For LB expression SEMI expression SEMI expression RB stmt;
block_stmt: LP declare statement RP;
dowhile_stmt: Do statement While expression SEMI;
if_stmt: If LB expression RB stmt ( Else stmt)?;

stmt:
	if_stmt
	| dowhile_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| expression_stmt
	| block_stmt
	| index_expression SEMI;

statement: stmt*;

// block_statement: LP declare statement RP;

func_declare: (primitive_type | VOIDTYPE | output_parameter) ID LB multi_para? RB block_stmt;
//-----------------------------------------------------------------------------------------------------

primitive_type: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE;

//----------------------------------------------------------------------------

// UNCLOSE_STRING: '"' (('\\' [btnfr'\\] | ~[\b\t\f\r\n\\"]) | '\n')*; 
// ILLEGAL_ESCAPE: '"' ('\\'
// [btnfr"'\\] | ~[\b\t\f\r\n\\"])* '\\' ~[btnfr"'\\]?;