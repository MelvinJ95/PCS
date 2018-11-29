from typing import List, Any

import ply.yacc as yacc
import ply.lex as lex
# Date	Item Name	Item Type	Quantity	Item Price	Sale Total
import texttable as ttable

def test():
    tab.header(['Item Name', 'Price'])

    print(tab.draw())

    tab.header(["juan", "ai"])

    thisthing = tab.HEADER
    print(thisthing)
    row = ['Caja Lapices', 2.5]
    row = ['Caja Lapices', 2.5]
    tab.add_row(row)

    print(tab.draw())

    row = ['Cosa', 2.5]
    tab.add_row(row)

    print(tab.draw())


tab = ttable.Texttable()
#test()

itemsTable = ttable.Texttable() #primer valor es el icono
reportTable = ttable.Texttable()

iKey = "items"
rKey = "report"

tempHead: List[Any] = []

def break_tuple_3(tuplo):
    if len(tuplo) == 3 and tuplo[2] is not None:
        tempHead.append(tuplo[0])
        break_tuple_3(tuplo[2])
    else: tempHead.append(tuplo[0])

def create_table(table_head):
    print(table_head)
    if(table_head[0] == iKey):
        break_tuple_3(table_head[1])

        #print(tempHead)

        itemsTable.header(tempHead)
        print(itemsTable.draw())

#table items uno, dos
#addRow items one, two

def add_row(table_head):
    print(table_head)
    tempHead.clear()
    if(table_head[0] == iKey):
        break_tuple_3(table_head[1])

        #print(tempHead)

        itemsTable.add_row(tempHead)
        print(itemsTable.draw())


