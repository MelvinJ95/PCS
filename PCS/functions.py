from PyQt5 import QtCore, QtGui, QtWidgets
from report_view import Ui_report_view
# from main_view import Ui_MainWindow
from create_report_view import Ui_reportCreateView as RCV
from receipt_view import Ui_Form
# from store_item import store_item


total_cost = 0
class function(object):
    global Ui_MainWindow
    global Ui_Form
    global total_cost

    def returnObj(self,object): #COPY OF MAIN VIEW INSTANCE
        global Ui_MainWindow #Declared again to edit value
        Ui_MainWindow = object

    def return_receipt(self,object):
        global Ui_Form
        Ui_Form = object

    def addtoCart(self, object, item):
        global total_cost  #Declared again to edit value

        rowCount = Ui_MainWindow.cart_table.rowCount()
        Ui_MainWindow.cart_table.insertRow(rowCount)
        rowCount -= 1
        Ui_MainWindow.cart_table.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(item.name))
        Ui_MainWindow.cart_table.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(item.price)))
        #Ui_MainWindow.cart_table.item(rowCount, 1).setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        # rowCount = rowCount + 1
        total_cost += item.price   #TO BE EDITED
        Ui_MainWindow.total_table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(round(total_cost, 2))))
       # Ui_MainWindow.total_table.item(0, 1).setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        # Ui_MainWindow.total_table.setItem(main_view.total_table.rowCount()-1, 1, QtWidgets.QTableWidgetItem(total_cost)) REMOVE COMMENT ONCED TOTAL COST IS DEFINED


    def deleteItem(self,row):
        global total_cost
        item_cost = Ui_MainWindow.cart_table.item(row-1,1).text()
        total_cost = total_cost - float(item_cost)
        Ui_MainWindow.total_table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(round(total_cost, 2))))
        # main_view.total_table.setItem(main_view.total_table.rowCount()-1, 1, QtWidgets.QTableWidgetItem(total_cost)) REMOVE COMMENT ONCED TOTAL COST IS DEFINED

        Ui_MainWindow.cart_table.removeRow(row-1)

    def report(self):
        Ui_MainWindow.window = QtWidgets.QMainWindow()
        Ui_MainWindow.ui = RCV()
        Ui_MainWindow.ui.setupUi(Ui_MainWindow.window)
        Ui_MainWindow.window.show()

    def total(self):
        return total_cost

    def setshopName(self, name):
        Ui_MainWindow.shop_name_label.setText(QtCore.QCoreApplication.translate("Mainwindow", name))

    def setElementsGridDimensions(self, x, y):
        Ui_MainWindow.setGridSize(QtCore.QSize(x,y))

    def setCartRowSize(self, x):
        Ui_MainWindow.cart_table.verticalHeader().setDefaultSectionSize(x);

    def clearHeader(self): #RECEIPT
        Ui_Form.header_label.setText(QtCore.QCoreApplication.translate("Form", "<html><head/><body><p>"+" "+"</p></body></html>"))

    def appendToHeader(self, x):
        Ui_Form.header_label.setText(QtCore.QCoreApplication.translate("Form", "<html><head/><body><p align = \'center\'>"+x+"</p></body></html>")) #centered

    def clearBody(self):
        Ui_Form.header_label_3.setText(QtCore.QCoreApplication.translate("Form", "<html><head/><body><p>"+" "+"</p></body></html>"))

    def appendToBody(self,x):
        Ui_Form.header_label_3.setText(QtCore.QCoreApplication.translate("Form", "<html><head/><body><p align = \'center\'>" + x + "</p></body></html>")) #centered

    def clearFooter(self):
        Ui_Form.header_label_2.setText(QtCore.QCoreApplication.translate("Form", "<html><head/><body><p>"+" "+"</p></body></html>"))

    def appendToFooter(self,x):
        Ui_Form.header_label_2.setText(QtCore.QCoreApplication.translate("Form", "<html><head/><body><p align = \'center\'>" + x + "</p></body></html>")) #centered

    # def addElement(self, element):