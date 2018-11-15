import ply.lex as lex
import ply.yacc as yacc

# -- Lexer --

# reserved = {
#     'true' : 'TRUE',
#     'false' : 'FALSE',
#     'item_type_enable' : "ITEM_TYPE_ENABLE",
#     'item_enable' : "ITEM_TYPE"
# }  # function names and types shall be defined here

tokens = [
    'NUMBER',
    'FLOAT',
    'TRUE',
    'FALSE',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'PERIOD',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'STRING',
    'TABLE_C',
    'TABLE_R',
    'COLUMN',
    'COMMA',
    'PATHNAME',
    'HEAD',
    'BODY',
    'FOOTER',
    'RECEIPT',
    'APPEND',
    'CLEAR',
    'TO',
    'item_type_enable',
    'item_enable',
    'EXIT'
  ]  #+ list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'\='
t_COMMA = r'\,'
t_PERIOD = r'\.'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'\d+\.\d'
    t.value = float(t.value)
    return t


def t_TRUE(t):
    r'(true)'
    t.value = True
    return t


def t_FALSE(t):
    r'(false)'
    t.value = False
    return t


# TableFunctions
def t_TABLE_C(t):
    r'table'
    return t


def t_TABLE_R(t):
    r'addRow'
    return t


# HEAD_BODY_FOOTER
def t_HEAD(t):
    r'head'
    return t


def t_BODY(t):
    r'body'
    return t


def t_FOOTER(t):
    r'footer'
    return t


# ReceiptFunctions
def t_RECEIPT(t):
    r'receipt'
    return t


def t_APPEND(t):
    r'append'
    return t


def t_CLEAR(t):
    r'clear'
    return t


def t_TO(t):
    r'to'
    return t


def t_item_type_enable(t):
    r'report\ item_type_enable'
    return t

def t_item_enable(t):
    r'report\ item_enable'
    return t

def t_EXIT(t):
    r'exit'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'


def t_PATHNAME(t):
    r'add'
    return t


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
         | tableExp
         | pathexpr
         | receiptexpr
         | boolean
         | empty
    '''
    print(run(p[1]))


def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''
    p[0] = p[1]


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
               | PATHNAME
    '''
    p[0] = p[1]

# Path Parsing
def p_pathexpr(p):
    '''
    pathexpr : PERIOD PERIOD DIVIDE pathexpr
           | PERIOD DIVIDE pathexpr
           | STRING DIVIDE pathexpr
           | STRING DIVIDE filename
    filename : STRING PERIOD STRING
           | STRING
    '''
    p[0] = p[1]

# Receipt Parsing
def p_receiptexpr_creat(p):
    '''
    receiptexpr : RECEIPT CLEAR HEAD
            | RECEIPT CLEAR BODY
            | RECEIPT CLEAR FOOTER
    '''
    print((p[1], p[2], p[3]))
    p[0] = (p[1],p[2],p[3])

def p_receiptexpr_append(p):
    '''
    receiptexpr : RECEIPT APPEND STRING TO HEAD
            | RECEIPT APPEND STRING TO BODY
            | RECEIPT APPEND STRING TO FOOTER
    '''
    print((p[1],p[2],p[3],p[4],p[5]))
    p[0] = (p[1],p[2],p[3],p[4],p[5])

# Table Parsing
def p_createTable(p):
    '''
    tableExp : TABLE_C column
    '''
    print((p[1], p[2]))
    p[0] = (p[1], p[2])


def p_addRowToTable(p):
    '''
    tableExp : TABLE_R column
    '''
    print((p[1], p[2]))
    p[0] = (p[1], p[2])


def p_Column(p):
    '''
    column : STRING
            | STRING COMMA column
    '''
    tempList = []
    for thing in p:
        if thing != None:
            tempList.append(thing)
    #print(tuple(tempList))
    p[0] = (tuple(tempList))

#report create view functions

# def p_use_boolean(p):
#     '''
#     expression : boolean
#     '''
#     p[0] = p[1]

#reportCV_expression
def p_report_create_view(p):
    '''
    expression : item_type_enable boolean 
                | item_enable boolean
    '''
    print((p[1], p[2]))
    p[0] = (p[1], p[2])
    # print(p[1])
    # p[0] = p[1]


def p_exit(p):
    '''
    expression : EXIT
    '''
    exit(0)


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


def p_error(p):
    print("Syntax error found!")

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

def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == 'table' :
            return print("funciono")
    else:
        return p

while True:
    try:
        s = input('>> ')
    except EOFError:  # ctr + D
        break
    parser.parse(s)


# cashaer shopName 1000x1000
# itemArea