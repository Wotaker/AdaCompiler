## Opis Tokenów

### Słowa zarezerwowane:
id | token | wzór (słowo)
---|-------|---------------
1 | ABS | abs
2 | AND | and
3 | ARRAY | array
4 | BEGIN | begin
5 | DECLARE | declare
6 | ELSE | else
7 | ELSIF | elsif
8 | END | end
9 | FOR | for
10 | FUNC | function
11 | IF | if
12 | IN | in
13 | IS | is
14 | LOOP | loop
15 | MOD | mod
16 | NOT | not
17 | NULL | null
18 | OF | of
19 | OR | or
20 | PROC | procedure
21 | RETURN | return
22 | REVERSE | reverse
23 | THEN | then
24 | USE | use
25 | WHILE | while
26 | WITH | with
27 | XOR | xor
28 | BOOL_VAL | TRUE
29 | BOOL_VAL | FALSE
30 | TYPE_INT | Integer
31 | TYPE_BOOL | Boolean
32 | TYPE_FLOAT | Float
33 | IMAGE | Image
34 | PUT_LINE | Put_Line

### Reszta tokenów
id | token | wzór
---|-------|----------
1 | LEFT_PAR | "("
2 | RIGHT_PAR | ")"
3 | LEFT_SQ_PAR | "["
4 | RIGHT_SQ_PAR | "]"
5 | LEFT_CUR_PAR | "["
6 | RIGHT_CUR_PAR | "{"
7 | PLUS | "}"
8 | MINUS | "-"
9 | MUL | "*"
10 | DIV | "/"
11 | POW | "**"
12 | ASSIGN | ":="
13 | EQUALS | "="
14 | NOT_EQUALS | "\="
15 | LESS | "<"
16 | GREATER | ">"
17 | LSEQ | "<="
18 | GTEQ | ">="
19 | APOSTROPHE | "'"
20 | SEMICOLON | ";"
21 | DOT | "."
22 | COMMA | ","
23 | COLON | ":"
24 | DUB_DOT | ".."
25 | COMMENT | "--.*"
26 | AMPERSAND | "&"
27 | NUMBER | "[-]?(d+.)?d+"
28 | IDENT | "[A-Za-z_][A-Za-z0-9_]*"
29 | STRING | '"[^"]*"'