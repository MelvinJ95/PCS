# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receipt_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 457)
        self.header_label = QtWidgets.QLabel(Form)
        self.header_label.setGeometry(QtCore.QRect(10, 0, 47, 13))
        self.header_label.setObjectName("header_label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 271, 71))
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.header_label_2 = QtWidgets.QLabel(Form)
        self.header_label_2.setGeometry(QtCore.QRect(10, 360, 47, 13))
        self.header_label_2.setObjectName("header_label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 380, 271, 71))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_3.setEnabled(False)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 120, 271, 231))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.header_label_3 = QtWidgets.QLabel(Form)
        self.header_label_3.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.header_label_3.setObjectName("header_label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header_label.setText(_translate("Form", "<html><head/><body><p>header</p></body></html>"))
        self.header_label_2.setText(_translate("Form", "<html><head/><body><p>footer</p></body></html>"))
        self.header_label_3.setText(_translate("Form", "<html><head/><body><p>body</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

