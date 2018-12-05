import ply.lex as lex
import ply.yacc as yacc
from main_view import Ui_MainWindow
import functions as FT
# from receipt_view import Ui_Form as receipt

import tableManager as tm
from PyQt5 import QtCore, QtGui, QtWidgets
from store_item import store_item

# Object initializations

# Main View
ui = Ui_MainWindow()
ft = ui.guiMain()
ui.initialize_receipt()
ui.receipt()
# ui.setReceipt(receipt)

# Receipt View


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
    'EQUALS',
    'STRING',
    'TABLE_C',
    'TABLE_R',
    'COMMA',
    'HEAD',
    'BODY',
    'FOOTER',
    'RECEIPT',
    'APPEND',
    'CLEAR',
    'TO',
    'VIEW',
    'REPORT',
    'SET_SHOP_NAME',
    'SET_DIMENSION',
    'SET_CART_ROW_SIZE',
    'SET_CART_QUANTITY_ENABLE',
    'ADD_ITEM',
    'item_type_enable',
    'item_enable',
    'SPACE',
    'COLON',
    'EXIT'
  ]  # + list(reserved.values())


# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'\='
t_COMMA = r'\,'
t_PERIOD = r'\.'
t_COLON = r'\"'
t_SPACE = r'\ '


# A regular expression rule with some action code
def t_FLOAT(t):
    # same as ..
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_TRUE(t):
    r'true'
    t.value = True
    return t


def t_FALSE(t):
    r'false'
    t.value = False
    return t


# TableFunctions
def t_TABLE_C(t):
    r'table'
    return t


def t_TABLE_R(t):
    r'addRow'
    return t


# Main View Functions
def t_VIEW(t):
    r'view'
    return t


def t_REPORT(t):
    r'report'
    return t


def t_SET_SHOP_NAME(t):
    r'set_shop_name'
    return t


def t_SET_DIMENSION(t):
    r'set_dimension'
    return t


def t_SET_CART_ROW_SIZE(t):
    r'set_cart_row_size'
    return t


def t_SET_CART_QUANTITY_ENABLE(t):
    r'set_cart_quantity_enable'
    return t


def t_ADD_ITEM(t):
    r'add_item'
    return t


# HEAD_BODY_FOOTER
def t_HEAD(t):
    r'header'
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
    r'item_type_enable'
    return t


def t_item_enable(t):
    r'item_enable'
    return t


def t_EXIT(t):
    r'exit'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = '\t'
t_ignore_COMMENT = r'\#.*'


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # r'[a-zA-Z0-9_.][a-zA-Z0-9]*'
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


def p_expr(p):
    '''
    expr : expression
         | item_details
         | tableExp
         | receiptexpr
         | mainviewexpr
         | reportexpr
         | empty
         | EXIT
    '''
    # print(p[1], "| len =", len(p[1]))
    if p[1] == "exit":
        exit(0)
    if run(p[1]) is not None:
        # print("doing math expression")
        print(run(p[1]))
    else: None
        # print(" to be attended ")
    # print("2) ", run(p[1]))


def p_id(p):
    '''
    id : FLOAT
        | NUMBER
        | STRING
    '''
    p[0] = p[1]


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
    expression : FLOAT
               | NUMBER
    '''
    # print("this is float or int expression\n", p[1])
    p[0] = p[1]
    # print("this is float or int expression\n", p[1])


# Receipt Parsing
def p_receiptexpr_creat(p):
    '''
    receiptexpr : RECEIPT CLEAR HEAD
            | RECEIPT CLEAR BODY
            | RECEIPT CLEAR FOOTER
    '''
    print((p[1], p[2], p[3]))
    if p[3] == "HEAD":
        ui.clearHeader()
    p[0] = (p[1],p[2],p[3])

def p_receiptexpr_append(p):
    '''
    receiptexpr : RECEIPT SPACE APPEND SPACE paragraph SPACE TO SPACE HEAD
            | RECEIPT SPACE APPEND SPACE paragraph SPACE TO SPACE BODY
            | RECEIPT SPACE APPEND SPACE paragraph SPACE TO SPACE FOOTER
    '''
    # receipt append "The Head Text. Aqui." to header               # TODO
    # receipt append "The Body Text. Aqui." to body                 # TODO
    # receipt append "The Foot Text. Aqui." to footer               # TODO
    p[0] = (p[1], p[3], p[5], p[7], p[9])
    print(p[0])
    if p[9] == "header":
        print(".. Adding ", p[5], " to", p[9])
        # TODO: insert function here
    if p[9] == "body":
        print(".. Adding ", p[5], " to", p[9])
        # TODO: insert function here
    if p[9] == "footer":
        print(".. Adding ", p[5], " to", p[9])
        # TODO: insert function here


def p_mainviewexp(p) :
    '''
    mainviewexpr : VIEW SPACE STRING
                | VIEW SPACE ADD_ITEM SPACE item_details
                | VIEW SPACE SET_SHOP_NAME SPACE STRING
                | VIEW SPACE SET_DIMENSION SPACE NUMBER SPACE COMMA SPACE NUMBER
                | VIEW SPACE SET_CART_ROW_SIZE SPACE NUMBER
                | VIEW SPACE SET_CART_QUANTITY_ENABLE SPACE boolean
    '''
    # view shop                                         # DONE
    # view add_item papa, papa1, foo, 1.23              # DONE
    # view set_shop_name TheNameYouWant                 # DONE
    # view set_dimension 1000, 1200                     # TODO
    # view set_cart_row_size 4                          # TODO
    # view set_cart_quantity_enable true                # TODO
    # view set_dimension 1000, 1200                     # TODO
    if len(p) < 5:
        if p[3] == "shop":
            print(".. Showing main window")
            ui.show_main_window()
        else:
            print("Expected [ view shop ] but instead found [ view ", p[3], "]")
            p_error(p)
    else:
        if p[3] == "add_item":
            print(".. Adding item to items table")
            print(".. Showing main window")
            tm.add_item(ui, "items", p[5])
        elif p[3] == "set_shop_name":
            print(".. Setting shop named to:", p[5])
            print(".. Showing main window")
            ui.set_shop_name(p[5])
            ui.show_main_window()
        else:
            # str(p[2])
            print((p[1], p[3], p[5]))
            p[0] = (p[1], p[3], p[5])


def p_item_details(p):
    '''
    item_details : STRING COMMA SPACE STRING COMMA SPACE STRING COMMA SPACE FLOAT
    '''
    p[0] = (p[1], p[4], p[7], p[10])


# def p_table_to_view(p):
#     '''
#     mainviewexpr : VIEW TABLE_C STRING
#     '''
#     ui.table_to_view(tm.table_to_view(p[3]))


# def p_path_series(p):
#     '''
#     path_series : STRING
#                 | STRING DIVIDE STRING
#     '''
#     tempList = []
#     for thing in p:
#         if thing != None:
#             tempList.append(thing)
#     #print(tuple(tempList))
#     p[0] = (tuple(tempList))


# Table Parsing
def p_createTable(p):
    '''
    tableExp : TABLE_C SPACE STRING SPACE column
    '''
    # table items uno, dos, tres, cuatro                # DONE
    p[0] = (p[3], p[5])
    # print(p[0])
    tm.create_table(p[0])


def p_addRowToTable(p):
    '''
    tableExp : TABLE_R SPACE STRING SPACE column
    '''
    # addRow items jamonilla, dos, tres, 1.2            # DONE
    p[0] = (p[3], p[5])
    # print(p[0])
    tm.add_row(ui, p[0])


def p_showTable(p):
    '''
    tableExp : TABLE_C SPACE STRING
    '''
    # table items                                       # DONE
    tm.show_table(p[3])
    p[0] = (p[1], p[3])


def p_column(p):
    '''
    column : id
            | id COMMA SPACE column
    '''
    tempList = []
    for thing in p:
        if thing is not None:
            tempList.append(thing)
    # print(tuple(tempList))
    p[0] = (tuple(tempList))

# report create view functions

# def p_use_boolean(p):
#     '''
#     expression : boolean
#     '''
#     p[0] = p[1]

# reportCV_expression


def p_report_create_view(p):
    '''
    reportexpr : REPORT SPACE item_type_enable SPACE boolean
                | REPORT SPACE item_enable SPACE boolean
    '''
    # report item_type_enable true                              # TODO
    # report item_enable true                                   # TODO
    p[0] = (p[1], p[3], p[5])
    print(p[0])
    if p[3] == "item_type_enable":
        print(".. Item type enable set to:", p[5])
        # TODO: insert function here
    if p[3] == "item_enable":
        print(".. Item enable set to:", p[5])
        # TODO: insert function here

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


def p_error(p):
    print("Error: This is p:", p)
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
    else:
        return p


# while True:
#     try:
#         s = input('>> ')
#     except EOFError:  # ctr + D
#         pass
#     parser.parse(s)
