import ply.lex as lex


class MyToken():
    colorBeg = "\33[95m"
    colorEnd = "\033[0m"

    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
    
    def __str__(self) -> str:
        return self.colorBeg + f"{self.name}|{self.value}" + self.colorEnd

reserved = {
    'abs':          'ABS',
    'and':          'AND',
    'array':        'ARRAY',
    'begin':        'BEGIN',
    'declare':      'DECLARE',
    'else':         'ELSE',
    'elseif':       'ELSIF',
    'end':          'END',
    'for':          'FOR',
    'function':     'FUNC',
    'if':           'IF',
    'in':           'IN',
    'is':           'IS',
    'loop':         'LOOP',
    'mod':          'MOD',
    'not':          'NOT',
    'null':         'NULL',
    'of':           'OF',
    'or':           'OR',
    'procedure':    'PROC',
    'return':       'RETURN',
    'reverse':      'REVERSE',
    'then':         'THEN',
    'use':          'USE',
    'while':        'WHILE',
    'with':         'WITH',
    'xor':          'XOR',
    'TRUE':         'BOOL_VAL',
    'FALSE':        'BOOL_VAL',
    'Integer':      'TYPE_INT',
    'Boolean':      'TYPE_BOOL',
    'Float':        'TYPE_FLOAT'
}


tokens = [
    # Parenthesis
    'LEFT_PAR',
    'RIGHT_PAR',
    'LEFT_SQ_PAR',
    'RIGHT_SQ_PAR',
    'LEFT_CUR_PAR',
    'RIGHT_CUR_PAR',

    # Operators
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'POW',
    'ASSIGN',

    # Relations
    'EQUALS',
    'NOT_EQUALS',
    'LESS',
    'GREATER',
    'LSEQ',
    'GTEQ',

    # Other
    'APOSTROPHE',
    'QUOTE',
    'SEMICOLON',
    'DOT',
    'COMMA',
    'COLON',
    'DUB_DOT',
    'COMMENT',
    'AMPERSAND',

    # Complex tokens
    'NUMBER',
    'IDENT',
    'TYPE',
    'BOOL'
] + list(reserved.values())


# Parenthesis
t_LEFT_PAR      = r'\('
t_RIGHT_PAR     = r'\)'
t_LEFT_SQ_PAR   = r'\['
t_RIGHT_SQ_PAR  = r'\]'
t_LEFT_CUR_PAR  = r'\{'
t_RIGHT_CUR_PAR = r'\}'

# Operators
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_MUL           = r'\*'
t_DIV           = r'/'
t_POW           = r'\*\*'
t_ASSIGN        = r':='

# Relations
t_EQUALS        = r'='
t_NOT_EQUALS    = r'\\='
t_LESS          = r'<'
t_GREATER       = r'>'
t_LSEQ          = r'<='
t_GTEQ          = r'>='

# Other
t_APOSTROPHE    = r"'"
t_QUOTE         = r'"'
t_SEMICOLON     = r';'
t_DOT           = r'\.'
t_COMMA         = r','
t_COLON         = r':'
t_DUB_DOT       = r'\.\.'
t_AMPERSAND     = r'&'

# Ignore those
t_ignore        = ' \t'
t_ignore_COMMENT = r'--.*'

def t_NUMBER(t):
    r'[-]?(\d+\.)?\d+'
    # t.value = int(t.value) if float(t.value) % 1 == 0 else float(t.value)
    t.value = t.value
    return t

def t_IDENT(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'IDENT')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("line %d: illegal character '%s'" %(t.lineno, t.value[0]) )
    t.lexer.skip(1)

lexer = lex.lex()