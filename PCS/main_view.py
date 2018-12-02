# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import functions as FT
from store_item import store_item

class Ui_MainWindow(object):
    global element_index
    global ui
    global app
    global MainWindow
    global cart_list  # VARIABLE HOLDING CART ITEM
    cart_list = []

    def checkout(self):
        global cart_list
        row = ""
        File = open("checkout.txt", "w")
        # File.write(word)
        for irow in range(self.cart_table.rowCount() - 1):
            item = self.cart_table.item(irow, 0).text()
            price = self.cart_table.item(irow, 1).text()
            File.write((item + " " + price) + "\n")
        File.close()
        FT.function().receipt()

    def add_toCart(self, item):
        item_to_send = item.data(QtCore.Qt.UserRole)
        print(str(item.data(QtCore.Qt.UserRole)))
        FT.function().addtoCart(self, item_to_send)

    def report(self):
        FT.function().report()

    def delete_fromCart(self):
        global cart_list
        try:
            index = self.cart_table.currentRow()
            item_to_delete = self.cart_table.item(index, 0).text()
            # print(("item to del %s",item_to_delete))
            # cart_list.remove((item_to_delete))
            for i in range(0, self.cart_table.rowCount() - 1):  # DELETE FROM LIST TOO
                # print(i)
                # print(self.cart_table.rowCount())
                # print(cart_list[i].name)
                if (cart_list[i].name == item_to_delete):
                    #   print("popping %s", cart_list[i].name)
                    cart_list.pop(i)
                    break

            FT.function().deleteItem(index + 1)

        except:
            # print("Oops! Selected Wrong Item")
            pass

    # print('after popping list is:')
    # for i in range(0,len(cart_list)):
    #   print(cart_list[i].name)

    def addElement(self, sitem):
        item = QtWidgets.QListWidgetItem()
        item.setData(QtCore.Qt.UserRole, sitem)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(sitem.icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.elements_grid.addItem(item)

        # element_index = element_index + 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(647, 443)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 641, 421))
        self.main_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_frame.setObjectName("main_frame")
        self.shop_name_label = QtWidgets.QLabel(self.main_frame)
        self.shop_name_label.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.shop_name_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shop_name_label.setFrameShape(QtWidgets.QFrame.Box)
        self.shop_name_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.shop_name_label.setLineWidth(1)
        self.shop_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_label.setObjectName("shop_name_label")
        self.elements_grid = QtWidgets.QListWidget(self.main_frame)
        self.elements_grid.setGeometry(QtCore.QRect(0, 20, 421, 401))
        self.elements_grid.setMinimumSize(QtCore.QSize(421, 0))
        self.elements_grid.setAutoScrollMargin(16)
        self.elements_grid.setAlternatingRowColors(False)
        self.elements_grid.setIconSize(QtCore.QSize(100, 50))
        self.elements_grid.setMovement(QtWidgets.QListView.Snap)
        self.elements_grid.setFlow(QtWidgets.QListView.LeftToRight)
        self.elements_grid.setProperty("isWrapping", True)
        self.elements_grid.setResizeMode(QtWidgets.QListView.Fixed)
        self.elements_grid.setLayoutMode(QtWidgets.QListView.Batched)
        self.elements_grid.setGridSize(QtCore.QSize(93, 50))
        self.elements_grid.setViewMode(QtWidgets.QListView.IconMode)
        self.elements_grid.setModelColumn(0)
        self.elements_grid.setUniformItemSizes(False)
        self.elements_grid.setWordWrap(False)
        self.elements_grid.setSelectionRectVisible(True)
        self.elements_grid.setObjectName("elements_grid")
        # item = QtWidgets.QListWidgetItem()
        # self.elements_grid.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.elements_grid.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # font = QtGui.QFont()
        # font.setPointSize(7)
        # item.setFont(font)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("jamonilla.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # item.setIcon(icon)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item.setBackground(brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item.setForeground(brush)
        # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        # self.elements_grid.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # font = QtGui.QFont()
        # font.setPointSize(7)
        # item.setFont(font)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("papa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # item.setIcon(icon)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item.setBackground(brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item.setForeground(brush)
        # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        # self.elements_grid.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.elements_grid.addItem(item)
        self.cart_table = QtWidgets.QTableWidget(self.main_frame)
        self.cart_table.setGeometry(QtCore.QRect(430, 20, 201, 251))
        self.cart_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cart_table.setAlternatingRowColors(False)
        self.cart_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.cart_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cart_table.setGridStyle(QtCore.Qt.NoPen)
        self.cart_table.setObjectName("cart_table")
        self.cart_table.setColumnCount(2)
        self.cart_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table.setHorizontalHeaderItem(1, item)
        self.cart_table.verticalHeader().setVisible(False)
        self.cart_table.verticalHeader().setDefaultSectionSize(30)
        self.check_out_button = QtWidgets.QPushButton(self.main_frame)
        self.check_out_button.setGeometry(QtCore.QRect(430, 320, 201, 41))
        self.check_out_button.setObjectName("check_out_button")
        self.total_table = QtWidgets.QTableWidget(self.main_frame)
        self.total_table.setGeometry(QtCore.QRect(430, 280, 201, 31))
        self.total_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.total_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.total_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.total_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.total_table.setShowGrid(False)
        self.total_table.setGridStyle(QtCore.Qt.SolidLine)
        self.total_table.setCornerButtonEnabled(True)
        self.total_table.setObjectName("total_table")
        self.total_table.setColumnCount(2)
        self.total_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.total_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_table.setItem(0, 0, item)
        self.total_table.horizontalHeader().setVisible(False)
        self.total_table.horizontalHeader().setHighlightSections(True)
        self.total_table.verticalHeader().setVisible(False)
        self.check_out_button_2 = QtWidgets.QPushButton(self.main_frame)
        self.check_out_button_2.setGeometry(QtCore.QRect(430, 370, 201, 41))
        self.check_out_button_2.setObjectName("check_out_button_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.elements_grid.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # initializing element index
        # element_index = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.shop_name_label.setText(_translate("MainWindow", "shop_name"))
        self.elements_grid.setSortingEnabled(True)
        __sortingEnabled = self.elements_grid.isSortingEnabled()
        self.elements_grid.setSortingEnabled(False)
        # item = self.elements_grid.item(0)
        # item.setText(_translate("MainWindow", "hola 3"))
        # item = self.elements_grid.item(1)
        # item.setText(_translate("MainWindow", "hola 4"))
        # item = self.elements_grid.item(2)
        # item.setText(_translate("MainWindow", "hola 5"))
        # item = self.elements_grid.item(3)
        # # item.setText(_translate("MainWindow", "hola1"))
        # item = self.elements_grid.item(4)
        # item.setText(_translate("MainWindow", "hola2"))
        self.elements_grid.setSortingEnabled(__sortingEnabled)
        item = self.cart_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.cart_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "item"))
        item = self.cart_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "cost"))
        self.check_out_button.setText(_translate("MainWindow", "Check out"))
        item = self.total_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.total_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "total_text"))
        item = self.total_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "total_value"))
        __sortingEnabled = self.total_table.isSortingEnabled()
        self.total_table.setSortingEnabled(False)
        item = self.total_table.item(0, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.total_table.setSortingEnabled(__sortingEnabled)
        self.check_out_button_2.setText(_translate("MainWindow", "Report"))

        # ITEM EVENT ACTION
        self.elements_grid.itemClicked.connect(self.add_toCart)
        
        #USER CANT EDIT ITEM/COST HEADERS
        self.cart_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # BUTTON EVENTS
        self.check_out_button.clicked.connect(self.checkout)
        self.check_out_button_2.clicked.connect(self.report)

        # Give function an Instance of Main Window to have access to UI Elements
        FT.function().returnObj(self)



    def guiMain(self):
        import sys
        global app
        global ui
        global MainWindow
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        # ui = Ui_MainWindow()
        self.setupUi(MainWindow)

        # Adding items
        item = store_item.makeItem("jamonilla.jpg", "jamonilla", "food", 2.15)
        self.addElement(item)
        item = store_item.makeItem("rice.jpg", "rice", "food", 5.14)
        self.addElement(item)
        item = store_item.makeItem("coke.jpg", "coke", "food", 1.00)
        self.addElement(item)
        # item = store_item.makeItem("papa.png", "papa", "food", 1.15)
        # ui.addElement(item)

        # MainWindow.show()
        # app.exec_()
        # sys.exit(app.exec_())

    def show_main_window(self):
        MainWindow.show()
        app.exec_()

    def table_to_view(self, input):
        global app
        global ui
        print("entro a table view")
        item = store_item.makeItem(input[0], input[0], input[0], input[0])
        self.addElement(item)
        MainWindow.show()
        app.exec_()

