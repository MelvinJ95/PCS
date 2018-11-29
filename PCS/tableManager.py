import ply.yacc as yacc
import ply.lex as lex
# Date	Item Name	Item Type	Quantity	Item Price	Sale Total
import texttable as ttable

tab = ttable.Texttable()
tab.header(['Item Name', 'Price'])
row = ['Caja Lapices', 2.5]
row = ['Caja Lapices', 2.5]
tab.add_row(row)

print(tab.draw())

