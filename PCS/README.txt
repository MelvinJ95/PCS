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


