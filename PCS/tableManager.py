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

itemsTable = ttable.Texttable() # primer valor es el icono
reportTable = ttable.Texttable()

iKey = "items"
rKey = "report"

tempList = []

# for testing purposes and demonstration
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
    if table_head[0] == iKey:
        break_tuple_3(table_head[1])
        itemsTable.header(tempList)
        print(itemsTable.draw())

    elif table_head[0] == rKey:
        break_tuple_3(table_head[1])
        reportTable.header(tempList)
        print(reportTable.draw())

# table items uno, dos
# addRow items one, two


def add_item(ui, table_name, table_row):
    # tempList.clear()
    print("    dalsdfi   ".strip())
    print("inside add_row: tname-", table_name.strip(), "trow-", table_row)
    print("1) inside add_row: tname-", table_name.strip())
    if table_name.strip() == iKey:
        try:
            ui.add_item(table_row, ".png")
            print(".. Searching .png image.")
        except FileNotFoundError:
            try:
                ui.add_item(table_row, ".jpg")
                print(".. Searching .jpg image.")
            except FileNotFoundError:
                print(" * Image not found * ")

        print("2) inside add_row: tname-", table_name.strip())
        itemsTable.add_row(table_row)
        print(itemsTable.draw())
    elif table_name.strip() == rKey:
        reportTable.add_row(table_row)
        print(reportTable.draw())


def add_row(ui, table_row):
    tempList.clear()
    if table_row[0] == iKey:
        break_tuple_3(table_row[1])
        try:
            ui.add_item(tempList, ".png")
            print(".. Searching .png image.")
        except FileNotFoundError:
            try:
                ui.add_item(tempList, ".jpg")
                print(".. Searching .jpg image.")
            except FileNotFoundError:
                print(" * Image not found * ")
        itemsTable.add_row(tempList)
        print(itemsTable.draw())
    elif table_row[0] == rKey:
        break_tuple_3(table_row[1])
        reportTable.add_row(tempList)
        print(reportTable.draw())


def show_table(table_name):
    if table_name == iKey:
        print(itemsTable.draw())
    elif table_name == rKey:
        print(reportTable.draw())
