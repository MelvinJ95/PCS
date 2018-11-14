import ply.lex as lex
import ply.yacc as yacc

# -- Lexer --

reserved_keywords = ()  # function names and types shall be defined here

tokens = (
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'STRING'
)  # + list(reserved_keywords.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'\='


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'\d+\.\d'
    t.value = float(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # t.type = reserved_keywords.get(t.value, 'STRING')  # Check for reserved words
    t.type = 'STRING'
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# -- Parser --

# Setting Precedence to Operations
precedence = (

    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')

)

# def t_column


def p_calc(p):
    '''
    calc : expression
         | empty
    '''
    print(p[1])


def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
    '''
    p[0] = (p[2], p[1], p[3])


def p_expression_int_float(p):
    '''
    expression : NUMBER
               | FLOAT
    '''
    p[0] = p[1]


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


parser = yacc.yacc()

# TESTING Lexer
# lexer.input("1+2")
#
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

# TESTING Parser
while True:
    try:
        s = input('')
    except EOFError:  # ctr + D
        break
    parser.parse(s)
