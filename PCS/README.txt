11/9/2018 

-Added functionality to Add item(Pricing to be added when defined)  
-Added functionality to remove item from row 
-Added functionality to open report window 
-Added functionality to return total cart cost(once prices have been defined)
-Added Item class (store_item.py)  

11/10/2018 
-Added functionality to add Shop name 
-Added functionality to set dimension of elements_grid 
-Added functionality to set cart's row size vertically
-Added functionality to clear Receipt_view header text 
-Added functionality to change Recept_view header text 
-Added functionality to clear Recept_view Body's header text
-Added functionality to change Recept_view Body's header text  
-Added functionality to clear Recept_view footer's header text 
-Added functionality to change Recept_view footer's header text

Tokens:
NUMBER              ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
TRUE                ::= true
FALSE               ::= FALSE
PLUS                ::= '+'
MINUS               ::= '-'
MULTIPLY            ::= '*'
DIVIDE              ::= '/'
LPAREN              ::= '('
RPAREN              ::= ')'
EQUALS              ::= '='
STRING              ::= '[a-zA-Z_][a-zA-Z_0-9]*'
TABLE_C             ::= 'table'
TABLE_R             ::= 'addRow'
COMMA               ::= ','
PERIOD              ::= '.'
VIEW                ::= 'view'
SET_SHOP_NAME       ::= 'set_shop_name'
SET_DIMENSION       ::= 'set_dimension'
SET_CART_ROW_SIZE   ::= 'set_cart_row_size'
ELEMENT_GRID_ADD    ::= 'element_grid_add'
HEAD                ::= 'head'
BODY                ::= 'body'
FOOTER              ::= 'footer'
RECEIPT             ::= 'receipt'
APPEND              ::= 'append'
CLEAR               ::= 'clear'
TO                  ::= 'to'
ITEM_TYPE_ENABLE    ::= 'report\ item_type_enable'
ITEM_ENABLE         ::= 'report\ item_enable'
EXIT                ::= 'exit'
NEWLINE             ::= '\n+'
SET_CART_QUANTITY_ENABLE    ::= 'set_cart_quantity_enable'


GRAMMAR:
calc ::= expression
        | tableExp
        | pathexpr
        | receiptexpr
        | mainviewexpr
        | reportexpr
        | empty

boolean ::= TRUE
	    | FALSE


expression ::= expression MULTIPLY expression
        | expression DIVIDE expression
        | expression PLUS expression
        | expression MINUS expression
	    | NUMBER
        | FLOAT
	    | EXIT


pathexpr ::= PERIOD PERIOD DIVIDE pathexpr
        | PERIOD DIVIDE pathexpr
        | STRING DIVIDE pathexpr
        | STRING DIVIDE filename
filename ::= STRING PERIOD STRING
        | STRING


receiptexpr ::= RECEIPT CLEAR HEAD
        | RECEIPT CLEAR BODY
        | RECEIPT CLEAR FOOTER


receiptexpr ::= RECEIPT APPEND STRING TO HEAD
        | RECEIPT APPEND STRING TO BODY
        | RECEIPT APPEND STRING TO FOOTER


mainviewexpr ::= VIEW SET_SHOP_NAME STRING
        | VIEW SET_DIMENSION NUMBER COMMA NUMBER
        | VIEW SET_CART_ROW_SIZE NUMBER
        | VIEW SET_CART_QUANTITY_ENABLE boolean
        | VIEW ELEMENT_GRID_ADD path_series


path_series ::= STRING
        | STRING DIVIDE STRING


tableExp ::= TABLE_C column
	    | TABLE_R column


column ::= STRING
        | STRING COMMA column


reportexpr ::= item_type_enable boolean
        | item_enable boolean

FLOAT ::= NUMBER\.NUMBER
