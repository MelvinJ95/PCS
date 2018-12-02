from typing import List, Any

# Date	Item Name	Item Type	Quantity	Item Price	Sale Total
import texttable as ttable
import main_view as mv

def test():
    tab = ttable.Texttable()
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
    tab.add_row("ddd")

    print(tab.draw())


#test()

itemsTable = ttable.Texttable() #primer valor es el icono
reportTable = ttable.Texttable()

iKey = "items"
rKey = "report"

tempList = []

#for testing purposes and demonstration
itemsTable.header(["file path","article name","type","price"])
itemsTable.add_row(["jamonilla.jpg", "jamonilla", "food", 2.15])
itemsTable.add_row(["rice.jpg", "rice", "food", 5.14])
itemsTable.add_row(["coke.jpg", "coke", "food", 1.00])
itemsTable.add_row(["papa.png", "papa", "food", 1.15])


def break_tuple_3(tuplo):
    if len(tuplo) == 3 and tuplo[2] is not None:
        tempList.append(tuplo[0])
        break_tuple_3(tuplo[2])
    else:
        tempList.append(tuplo[0])

def create_table(table_head):
    #print(table_head)
    if(table_head[0] == iKey):
        break_tuple_3(table_head[1])

        #print(tempHead)

        itemsTable.header(tempList)
        print(itemsTable.draw())

    elif(table_head[0] == rKey):
        break_tuple_3(table_head[1])

        #print(tempHead)

        reportTable.header(tempList)
        print(reportTable.draw())

#table items uno, dos
#addRow items one, two


def add_row(ui, table_head):
    #print(table_head)
    tempList.clear()
    if(table_head[0] == iKey):
        break_tuple_3(table_head[1])

        #print(tempHead)

        itemsTable.add_row(tempList)
        #item = store_item.makeItem("jamonilla.jpg", "jamonilla", "food", 2.15)
        #ui.addElement(item)
        ui.add_item()
        print(itemsTable.draw())
    elif (table_head[0] == rKey):
        break_tuple_3(table_head[1])

        # print(tempHead)

        reportTable.add_row(tempList)
        print(reportTable.draw())

def show_table(name):
    if (name == iKey):
        print(itemsTable.draw())
    elif (name == rKey):
        print(reportTable.draw())

def table_to_view(name):
    print(name)
    return "papa.png", "papa", "food", 1.15
    # item = store_item.makeItem("jamonilla.jpg", "jamonilla", "food", 2.15)
    # ui.addElement(item)
    # item = store_item.makeItem("rice.jpg", "rice", "food", 5.14)
    # ui.addElement(item)
    # item = store_item.makeItem("coke.jpg", "coke", "food", 1.00)
    # ui.addElement(item)
    # item = store_item.makeItem("papa.png", "papa", "food", 1.15)
    # ui.addElement(item)

