# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import functions as FT


class Ui_report_view(object):
    def setupUi(self, report_view):
        report_view.setObjectName("report_view")
        report_view.resize(550, 304)
        self.report_list = QtWidgets.QTableWidget(report_view)
        self.report_list.setGeometry(QtCore.QRect(10, 10, 531, 191))
        self.report_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.report_list.setAlternatingRowColors(False)
        self.report_list.setObjectName("report_list")
        self.report_list.setColumnCount(4)
        self.report_list.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.report_list.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_list.setHorizontalHeaderItem(3, item)
        self.report_list.horizontalHeader().setCascadingSectionResizes(False)
        self.report_list.horizontalHeader().setDefaultSectionSize(128)
        self.report_list.verticalHeader().setDefaultSectionSize(20)
        self.total_label = QtWidgets.QLabel(report_view)
        self.total_label.setGeometry(QtCore.QRect(240, 210, 47, 13))
        self.total_label.setObjectName("total_label")
        self.totals_table = QtWidgets.QTableWidget(report_view)
        self.totals_table.setGeometry(QtCore.QRect(240, 230, 301, 51))
        self.totals_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.totals_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.totals_table.setCornerButtonEnabled(False)
        self.totals_table.setObjectName("totals_table")
        self.totals_table.setColumnCount(2)
        self.totals_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.totals_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.totals_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.totals_table.setHorizontalHeaderItem(1, item)
        self.totals_table.horizontalHeader().setDefaultSectionSize(150)
        self.totals_table.verticalHeader().setVisible(False)
        self.totals_table.verticalHeader().setHighlightSections(True)
        self.print_button = QtWidgets.QPushButton(report_view)
        self.print_button.setGeometry(QtCore.QRect(310, 300, 111, 51))
        self.print_button.setObjectName("print_button")
        self.close_button = QtWidgets.QPushButton(report_view)
        self.close_button.setGeometry(QtCore.QRect(430, 300, 111, 51))
        self.close_button.setObjectName("close_button")

        self.retranslateUi(report_view)
        QtCore.QMetaObject.connectSlotsByName(report_view)

    def retranslateUi(self, report_view):
        _translate = QtCore.QCoreApplication.translate
        report_view.setWindowTitle(_translate("report_view", "Form"))
        item = self.report_list.verticalHeaderItem(0)
        item.setText(_translate("report_view", "1"))
        item = self.report_list.horizontalHeaderItem(0)
        item.setText(_translate("report_view", "Date"))
        item = self.report_list.horizontalHeaderItem(1)
        item.setText(_translate("report_view", "Item"))
        item = self.report_list.horizontalHeaderItem(2)
        item.setText(_translate("report_view", "Quantity"))
        item = self.report_list.horizontalHeaderItem(3)
        item.setText(_translate("report_view", "Purchase"))
        self.total_label.setText(_translate("report_view", "Total"))
        item = self.totals_table.verticalHeaderItem(0)
        item.setText(_translate("report_view", "1"))
        item = self.totals_table.horizontalHeaderItem(0)
        item.setText(_translate("report_view", "Quantity"))
        item = self.totals_table.horizontalHeaderItem(1)
        item.setText(_translate("report_view", "Purchase"))
        self.print_button.setText(_translate("report_view", "Print"))
        self.close_button.setText(_translate("report_view", "Close"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    report_view = QtWidgets.QWidget()
    ui = Ui_report_view()
    ui.setupUi(report_view)
    report_view.show()
    sys.exit(app.exec_())
