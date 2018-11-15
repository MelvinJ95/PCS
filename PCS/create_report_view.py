# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_report_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_reportCreateView(object):
    def setupUi(self, reportCreateView):
        reportCreateView.setObjectName("reportCreateView")
        reportCreateView.resize(522, 118)
        self.date_start_selector = QtWidgets.QDateEdit(reportCreateView)
        self.date_start_selector.setGeometry(QtCore.QRect(10, 40, 110, 22))
        self.date_start_selector.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_start_selector.setObjectName("date_start_selector")
        self.date_start_label = QtWidgets.QLabel(reportCreateView)
        self.date_start_label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.date_start_label.setObjectName("date_start_label")
        self.date_end_selector = QtWidgets.QDateEdit(reportCreateView)
        self.date_end_selector.setGeometry(QtCore.QRect(140, 40, 110, 22))
        self.date_end_selector.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_end_selector.setObjectName("date_end_selector")
        self.date_end_label = QtWidgets.QLabel(reportCreateView)
        self.date_end_label.setGeometry(QtCore.QRect(140, 20, 61, 16))
        self.date_end_label.setObjectName("date_end_label")
        self.item_type_label = QtWidgets.QLabel(reportCreateView)
        self.item_type_label.setGeometry(QtCore.QRect(270, 20, 61, 16))
        self.item_type_label.setObjectName("item_type_label")
        self.item_type_combo_box = QtWidgets.QComboBox(reportCreateView)
        self.item_type_combo_box.setGeometry(QtCore.QRect(270, 40, 101, 22))
        self.item_type_combo_box.setObjectName("item_type_combo_box")
        self.item_type_combo_box.addItem("")
        self.item_combo_label = QtWidgets.QLabel(reportCreateView)
        self.item_combo_label.setGeometry(QtCore.QRect(400, 20, 61, 16))
        self.item_combo_label.setObjectName("item_combo_label")
        self.item_combo_box = QtWidgets.QComboBox(reportCreateView)
        self.item_combo_box.setGeometry(QtCore.QRect(400, 40, 101, 22))
        self.item_combo_box.setObjectName("item_combo_box")
        self.item_combo_box.addItem("")
        self.report_create_button = QtWidgets.QPushButton(reportCreateView)
        self.report_create_button.setGeometry(QtCore.QRect(410, 80, 91, 21))
        self.report_create_button.setObjectName("report_create_button")

        self.retranslateUi(reportCreateView)
        QtCore.QMetaObject.connectSlotsByName(reportCreateView)

    def retranslateUi(self, reportCreateView):
        _translate = QtCore.QCoreApplication.translate
        reportCreateView.setWindowTitle(_translate("reportCreateView", "Form"))
        self.date_start_label.setText(_translate("reportCreateView", "<html><head/><body><p>Date start</p></body></html>"))
        self.date_end_label.setText(_translate("reportCreateView", "<html><head/><body><p>Date end</p></body></html>"))
        self.item_type_label.setText(_translate("reportCreateView", "<html><head/><body><p>item type</p></body></html>"))
        self.item_type_combo_box.setItemText(0, _translate("reportCreateView", " ---"))
        self.item_combo_label.setText(_translate("reportCreateView", "<html><head/><body><p>item</p></body></html>"))
        self.item_combo_box.setItemText(0, _translate("reportCreateView", " ---"))
        self.report_create_button.setText(_translate("reportCreateView", "create report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reportCreateView = QtWidgets.QWidget()
    ui = Ui_reportCreateView()
    ui.setupUi(reportCreateView)
    reportCreateView.show()
    sys.exit(app.exec_())

