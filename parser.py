import ply.yacc as yacc
from lexer import MyToken, tokens
from deriviation_tree import DeriveTree

# === Empty production ===
def p_empty(p):
    'empty :'
    p[0] = DeriveTree('empty', [DeriveTree(MyToken('EMPTY', 'ε'))])

# === Start production ===
def p_prog(p):
    '''prog : subprogram
            | headers subprogram'''
    if len(p) == 2:
        p[0] = DeriveTree('prog', [p[1]])
    else:
        p[0] = DeriveTree('prog', [p[1], p[2]])

def p_headers(p):
    '''headers : headers header
               | header'''
    if len(p) == 3:
        p[0] = DeriveTree('headers', [p[1], p[2]])
    else:
        p[0] = DeriveTree('headers', [p[1]])

def p_header(p):
    '''header : WITH pkg SEMICOLON
              | WITH pkg SEMICOLON USE pkg SEMICOLON'''
    if len(p) == 4:
        p[0] = DeriveTree(
            'header', 
            [DeriveTree(MyToken("WITH", p[1])), p[2], DeriveTree(MyToken("SEMICOLON", p[3]))]
        )
    else:
        p[0] = DeriveTree(
            'header', 
            [DeriveTree(MyToken("WITH", p[1])), p[2], DeriveTree(MyToken("SEMICOLON", p[3])), 
            DeriveTree(MyToken("USE", p[4])), p[5], DeriveTree(MyToken("SEMICOLON", p[6]))]
        )

def p_pkg(p):
    '''pkg : pkg DOT IDENT
           | IDENT'''
    if len(p) == 4:
        p[0] = DeriveTree('pkg', [p[1], DeriveTree(MyToken("DOT", p[2])), DeriveTree(MyToken("IDENT", p[3]))])
    else:
        p[0] = DeriveTree('pkg', [DeriveTree(MyToken("IDENT", p[1]))])

# === Debug Rule ===
# def p_subprogram(p):
#     '''subprogram : IDENT'''
#     p[0] = DeriveTree("Subprogram", [DeriveTree(MyToken("IDENT", p[1]))])

def p_subprogram(p):
    '''subprogram : procedure
                  | function'''
    p[0] = DeriveTree('subprogram', [p[1]])

def p_function(p):
    '''function : IDENT'''
    # TODO end this!!!
    p[0] = DeriveTree("function", [DeriveTree(MyToken("IDENT", p[1]))])

def p_procedure(p):
    '''procedure : PROC IDENT args_opt IS declarations BEGIN statements END IDENT SEMICOLON'''
    if p[2] is not p[9]:
        # TODO Error with incosistand proc declaration
        pass
    p[0] = DeriveTree("procedure", [
        DeriveTree(MyToken("PROC", p[1])), DeriveTree(MyToken("IDENT", p[2])), p[3],
        DeriveTree(MyToken("IS", p[4])), p[5], DeriveTree(MyToken("BEGIN", p[6])),
        p[7], DeriveTree(MyToken("END", p[8])), DeriveTree(MyToken("IDENT", p[9])),
        DeriveTree(MyToken("SEMICOLON", p[10]))
    ])

def p_args_opt(p):
    '''args_opt : LEFT_PAR args RIGHT_PAR
                | empty'''
    if len(p) == 4:
        p[0] = DeriveTree("args_opt", [DeriveTree(MyToken("LEFT_PAR", p[1])), p[2],
        DeriveTree(MyToken("LEFT_PAR", p[3]))])
    else:
        p[0] = DeriveTree("args_opt", [p[1]])

def p_args(p):
    """args : args COMMA arg
            | arg"""
    if len(p) == 4:
        p[0] = DeriveTree("args", [p[1], DeriveTree(MyToken("COMMA", p[2])), p[3]])
    else:
        p[0] = DeriveTree("args". p[1])

def p_arg(p):
    """arg : IDENT COLON type"""
    p[0] = DeriveTree("arg", [DeriveTree(MyToken("IDENT", p[1])), DeriveTree(MyToken("COLON", p[2])), p[3]])

def p_type(p):
    """type : TYPE_INT
            | TYPE_FLOAT
            | TYPE_BOOL"""
    if p[1] == "Integer":
        p[0] = DeriveTree("type", [DeriveTree(MyToken("TYPE_INT", p[1]))])
    elif p[1] == "Float":
        p[0] = DeriveTree("type", [DeriveTree(MyToken("TYPE_FLOAT", p[1]))])
    else:
        p[0] = DeriveTree("type", [DeriveTree(MyToken("TYPE_BOOL", p[1]))])

def p_declarations(p):
    """declarations : declarations declaration
                    | declaration"""
    if len(p) == 3:
        p[0] = DeriveTree("declarations", [p[1], p[2]])
    else:
        p[0] = DeriveTree("declarations", [p[1]])

def p_declaration(p):
    """declaration : IDENT COLON type ASSIGN value SEMICOLON"""
    p[0] = DeriveTree("declaration", [
        DeriveTree(MyToken("IDENT", p[1])), DeriveTree(MyToken("COLON", p[2])),
        p[3], DeriveTree(MyToken("ASSIGN", p[4])), p[5], DeriveTree(MyToken("SEMICOLON", p[6]))
    ])

def p_value(p):
    """value : expr
             | bool_expr"""
    p[0] = DeriveTree("value", [p[1]])

def p_expr(p):
    """expr : expr PLUS term
            | expr MINUS term
            | term"""
    if len(p) == 4 and p[2] == "+":
        p[0] = DeriveTree("expr", [p[1], DeriveTree(MyToken("PLUS", p[2])), p[3]])
    elif len(p) == 4:
        p[0] = DeriveTree("expr", [p[1], DeriveTree(MyToken("MINUS", p[2])), p[3]])
    else:
        p[0] = DeriveTree("expr", [p[1]])

def p_term(p):
    """term : term MUL factor
            | term DIV factor
            | factor"""
    if len(p) == 4 and p[2] == "*":
        p[0] = DeriveTree("term", [p[1], DeriveTree(MyToken("MUL", p[2])), p[3]])
    elif len(p) == 4:
        p[0] = DeriveTree("term", [p[1], DeriveTree(MyToken("DIV", p[2])), p[3]])
    else:
        p[0] = DeriveTree("term", [p[1]])

def p_factor(p):
    """factor : LEFT_PAR expr RIGHT_PAR
              | IDENT
              | NUMBER"""    # TODO add function_call
    if len(p) == 4:
        p[0] = DeriveTree("factor", [DeriveTree(MyToken("LEFT_PAR", p[1])), p[2],
        DeriveTree(MyToken("RIGHT_PAR", p[3]))])
    elif p[1] in r'[A-Za-z_][A-Za-z0-9_]*':
        p[0] = DeriveTree("factor", [DeriveTree(MyToken("IDENT", p[1]))])
    else:
        p[0] = DeriveTree("factor", [DeriveTree(MyToken("NUMBER", p[1]))])

def p_bool_expr(p):
    """bool_expr : bool_term AND bool_term
                 | bool_term OR bool_term
                 | bool_term"""
    if len(p) == 4:
        p[0] = DeriveTree("bool_expr", [p[1], DeriveTree(MyToken("AND" if p[2] == "and" else "OR", p[2])), p[3]])
    else:
        p[0] = DeriveTree("bool_expr", [p[1]])

def p_bool_term(p):
    """bool_term : NOT bool
                 | bool"""
    if len(p) == 3:
        p[0] = DeriveTree("bool_term", [DeriveTree(MyToken("NOT", p[1])), p[2]])
    else:
        p[0] = DeriveTree("bool_term", [p[1]])

def p_bool(p):
    """bool : LEFT_PAR bool_expr RIGHT_PAR
            | BOOL_VAL
            | IDENT"""
    if len(p) == 4:
        p[0] = DeriveTree("bool", [DeriveTree(MyToken("LEFT_PAR", p[1])), p[2],
        DeriveTree(MyToken("RIGHT_PAR", p[3]))])
    elif p[1] == "TRUE" or p[1] == "FALSE":
        p[0] = DeriveTree("bool", [DeriveTree(MyToken("BOOL_VAL", p[1]))])
    else:
        p[0] = DeriveTree("bool", [DeriveTree(MyToken("IDENT", p[1]))])

def p_statements(p):
    """statements : statements statement
                  | statement"""
    if len(p) == 3:
        p[0] = DeriveTree("statements", [p[1], p[2]])
    else:
        p[0] = DeriveTree("statements", [p[1]])


def p_statement(p):
    """statement : assign
                 | if
                 | loop"""
    p[0] = DeriveTree("statement", [p[1]])

def p_assign(p):
    """assign : IDENT ASSIGN value SEMICOLON"""
    p[0] = DeriveTree("assign", [
        DeriveTree(MyToken("IDENT", p[1])), DeriveTree(MyToken("ASSIGN", p[2])), p[3],
        DeriveTree(MyToken("SEMICOLON", p[4]))])

def p_if(p):
    """if : IF bool_expr THEN statements elsifs else END IF SEMICOLON"""
    p[0] = DeriveTree("if", [
        DeriveTree(MyToken("IF", p[1]), p[2], DeriveTree(MyToken("THEN", p[3]))), p[4], p[5], p[6],
        DeriveTree(MyToken("END", p[7])), DeriveTree(MyToken("IF", p[8])), 
        DeriveTree(MyToken("SEMICOLON", p[9]))
    ])

def p_eslifs(p):
    """elsifs : elsifs elsif
              | empty"""
    if len(p) == 3:
        p[0] = DeriveTree("elsifs", [p[1], p[2]])
    else:
        p[0] = DeriveTree("elsifs", p[1])

def p_elsif(p):
    """elsif : ELSIF bool_expr THEN statements"""
    p[0] = DeriveTree("elsif", [
        DeriveTree(MyToken("ELSIF", p[1])), p[2], DeriveTree(MyToken("THEN", p[3])), p[4]
    ])

def p_else(p):
    """else : ELSE statements
            | empty"""
    if len(p) == 3:
        p[0] = DeriveTree("else", [DeriveTree(MyToken("ELSE", p[1])), p[2]])
    else:
        p[0] = DeriveTree("else", p[1])

def p_loop(p):
    """loop : WHILE bool_expr loop_body
            | FOR IDENT IN expr DUB_DOT expr loop_body
            | FOR IDENT OF IDENT loop_body"""
    if len(p) == 3:
        p[0] = DeriveTree("loop", [
            DeriveTree(MyToken("WHILE", p[1])), p[2], p[3]
        ])
    elif len(p) == 8:
        p[0] = DeriveTree("loop", [
            DeriveTree(MyToken("FOR", p[1])), DeriveTree(MyToken("IDENT", p[2])),
            DeriveTree(MyToken("IN", p[3])), p[4], DeriveTree(MyToken("DUB_DOT", p[5])), p[6], p[7]
        ])
    else:
        p[0] = DeriveTree("loop", [
            DeriveTree(MyToken("FOR", p[1])), DeriveTree(MyToken("IDENT", p[2])),
            DeriveTree(MyToken("OF", p[3])), DeriveTree(MyToken("IDENT", p[4])), p[5]
        ])

def p_loop_body(p):
    """loop_body : LOOP statements END LOOP SEMICOLON"""
    p[0] = DeriveTree("loop_body", [
        DeriveTree(MyToken("LOOP", p[1])), p[2], DeriveTree(MyToken("END", p[3])),
        DeriveTree(MyToken("LOOP", p[4])), DeriveTree(MyToken("SEMICOLON", p[5]))
    ])

# === Error Handling Productions ===
# def p_error(p):
#     # TODO Expand error handling
#     print("Syntax error in input, check your grammar!")
    

parser = yacc.yacc(start='prog')
