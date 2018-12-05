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
        Form.resize(287, 459)
        self.header_label = QtWidgets.QLabel(Form)
        self.header_label.setGeometry(QtCore.QRect(10, 0, 47, 13))
        self.header_label.setObjectName("header_label")
        self.header_text = QtWidgets.QPlainTextEdit(Form)
        self.header_text.setEnabled(False)
        self.header_text.setGeometry(QtCore.QRect(10, 20, 271, 71))
        self.header_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.header_text.setInputMethodHints(QtCore.Qt.ImhNone)
        self.header_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.header_text.setCenterOnScroll(False)
        self.header_text.setObjectName("header_text")
        self.header_label_2 = QtWidgets.QLabel(Form)
        self.header_label_2.setGeometry(QtCore.QRect(10, 360, 47, 13))
        self.header_label_2.setObjectName("header_label_2")
        self.footer_text = QtWidgets.QPlainTextEdit(Form)
        self.footer_text.setEnabled(False)
        self.footer_text.setGeometry(QtCore.QRect(10, 380, 271, 71))
        self.footer_text.setObjectName("footer_text")
        self.body_text = QtWidgets.QPlainTextEdit(Form)
        self.body_text.setEnabled(False)
        self.body_text.setGeometry(QtCore.QRect(10, 120, 271, 231))
        self.body_text.setObjectName("body_text")
        self.body_label = QtWidgets.QLabel(Form)
        self.body_label.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.body_label.setObjectName("body_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header_label.setText(_translate("Form", "<html><head/><body><p>header</p></body></html>"))
        self.header_text.setPlainText(_translate("Form", "header crap\n" ""))
        self.header_label_2.setText(_translate("Form", "<html><head/><body><p>footer</p></body></html>"))
        self.footer_text.setPlainText(_translate("Form", "footer crap\n"
""))
        # .center(271, " ")
        self.body_text.setPlainText(_translate("Form", "body crap\n"
""))
        self.body_label.setText(_translate("Form", "<html><head/><body><p>body</p></body></html>"))
        print("done setting up")

    def appendtoHeader(self, x):
        pass


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

