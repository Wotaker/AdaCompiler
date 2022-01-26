import re
from lexer import tokens, reserved

ptype_dict = {
        "Integer": "%d",
        "Float":   "%f",
        "String":  "%s"
    }


rules = """Rule 0     S' -> prog
Rule 1     empty -> <empty>
Rule 2     prog -> subprogram
Rule 3     prog -> headers subprogram
Rule 4     headers -> headers header
Rule 5     headers -> header
Rule 6     header -> WITH pkg SEMICOLON
Rule 7     header -> WITH pkg SEMICOLON USE pkg SEMICOLON
Rule 8     pkg -> pkg DOT IDENT
Rule 9     pkg -> IDENT
Rule 10    subprogram -> procedure
Rule 11    subprogram -> function
Rule 12    function -> FUNC IDENT args_opt RETURN type IS declarations BEGIN ret_statements END IDENT SEMICOLON
Rule 13    function_call -> IDENT LEFT_PAR value RIGHT_PAR
Rule 14    procedure -> PROC IDENT args_opt IS declarations BEGIN statements END IDENT SEMICOLON
Rule 15    args_opt -> LEFT_PAR args RIGHT_PAR
Rule 16    args_opt -> empty
Rule 17    args -> args COMMA arg
Rule 18    args -> arg
Rule 19    arg -> IDENT COLON type
Rule 20    type -> TYPE_INT
Rule 21    type -> TYPE_FLOAT
Rule 22    type -> TYPE_BOOL
Rule 23    declarations -> declarations declaration
Rule 24    declarations -> declaration
Rule 25    declaration -> empty
Rule 26    declaration -> function
Rule 27    declaration -> procedure
Rule 28    declaration -> IDENT COLON type ASSIGN value SEMICOLON
Rule 29    value -> expr
Rule 30    value -> bool_expr
Rule 31    expr -> expr PLUS term
Rule 32    expr -> expr MINUS term
Rule 33    expr -> term
Rule 34    term -> term MUL factor
Rule 35    term -> term DIV factor
Rule 36    term -> factor
Rule 37    factor -> LEFT_PAR expr RIGHT_PAR
Rule 38    factor -> function_call
Rule 39    factor -> IDENT
Rule 40    factor -> NUMBER
Rule 41    bool_expr -> bool_term AND bool_term
Rule 42    bool_expr -> bool_term OR bool_term
Rule 43    bool_expr -> bool_term
Rule 44    bool_term -> NOT bool
Rule 45    bool_term -> bool
Rule 46    bool -> LEFT_PAR bool_expr RIGHT_PAR
Rule 47    bool -> BOOL_VAL
Rule 48    bool -> IDENT
Rule 49    bool -> rel_operand rel_operator rel_operand
Rule 50    rel_operand -> NUMBER
Rule 51    rel_operand -> IDENT
Rule 52    rel_operator -> EQUALS
Rule 53    rel_operator -> NOT_EQUALS
Rule 54    rel_operator -> GREATER
Rule 55    rel_operator -> LESS
Rule 56    rel_operator -> GTEQ
Rule 57    rel_operator -> LSEQ
Rule 58    statements -> statements statement
Rule 59    statements -> statement
Rule 60    statement -> assign
Rule 61    statement -> if
Rule 62    statement -> loop
Rule 63    statement -> put_line
Rule 64    statement -> function_call SEMICOLON
Rule 65    ret_statements -> ret_statements ret_statement
Rule 66    ret_statements -> ret_statement
Rule 67    ret_statement -> statement
Rule 68    ret_statement -> RETURN value SEMICOLON
Rule 69    assign -> IDENT ASSIGN value SEMICOLON
Rule 70    if -> IF bool_expr THEN ret_statements elsifs else END IF SEMICOLON
Rule 71    elsifs -> elsifs elsif
Rule 72    elsifs -> empty
Rule 73    elsif -> ELSIF bool_expr THEN ret_statements
Rule 74    else -> ELSE ret_statements
Rule 75    else -> empty
Rule 76    loop -> loop_body
Rule 77    loop -> for_range loop_body
Rule 78    loop -> while loop_body
Rule 79    loop_body -> LOOP statements END LOOP SEMICOLON
Rule 80    for_range -> FOR IDENT IN expr DUB_DOT expr
Rule 81    while -> WHILE bool_expr
Rule 82    put_line -> PUT_LINE LEFT_PAR str_expr RIGHT_PAR SEMICOLON
Rule 83    str_expr -> str_expr AMPERSAND str_term
Rule 84    str_expr -> str_term
Rule 85    str_term -> STRING
Rule 86    str_term -> type APOSTROPHE IMAGE LEFT_PAR value RIGHT_PAR"""

rules_split = rules.split("\n")
i = 0
for rule in rules_split:
    temp = rule.split()
    temp = temp[:2] + ["|"] + temp[2:]
    temp = " ".join(temp)
    rules_split[i] = temp
    i += 1

for rule in rules_split:
    print(rule)

