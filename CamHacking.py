# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CH.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(480, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        dialog.setStyleSheet("    background-color: #3a3a47;")
        self.frame = QtWidgets.QFrame(dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 270))
        self.frame.setStyleSheet("background-color: #fb5b5d")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 30, 360, 50))
        self.label.setStyleSheet("font: 750 28pt  \"Monserrat\";\n"
"color: white;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 191, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("wireless-security-camera-illustration-surveillance-cameras-removebg-preview-removebg-preview-removebg-preview-removebg-preview-removebg-preview.png"))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 320, 380, 60))
        self.lineEdit.setStyleSheet("font: 750 14pt  \"Monserrat\";\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 430, 181, 61))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font: 700 14pt  \"Monserrat\";\n"
"    color: white;\n"
"    background-color: #fb5b5d;\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 30;\n"
"}\n"
"QPushButton:hover {\n"
"    font: 700 14pt  \"Monserrat\";\n"
"    color: white;\n"
"    background-color: #fa4a4d;\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 30;\n"
"}\n"
"QPushButton:pressed {\n"
"    font: 700 14pt  \"Monserrat\";\n"
"    color: white;\n"
"    background-color: #fa3c3f;\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 30;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 430, 191, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    font: 700 14pt  \"Monserrat\";\n"
"    color: white;\n"
"    background-color: #fb5b5d;\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 30;\n"
"}\n"
"QPushButton:hover {\n"
"    font: 700 14pt  \"Monserrat\";\n"
"    color: white;\n"
"    background-color: #fa4a4d;\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 30;\n"
"}\n"
"QPushButton:pressed {\n"
"    font: 700 14pt  \"Monserrat\";\n"
"    color: white;\n"
"    background-color: #fa3c3f;\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 30;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 520, 270, 60))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    font: 700 14pt  \"Monserrat\";\n"
"    color: white;\n"
"    background-color: #fb5b5d;\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 30;\n"
"}\n"
"QPushButton:hover {\n"
"    font: 700 14pt  \"Monserrat\";\n"
"    color: white;\n"
"    background-color: #fa4a4d;\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 30;\n"
"}\n"
"QPushButton:pressed {\n"
"    font: 700 14pt  \"Monserrat\";\n"
"    color: white;\n"
"    background-color: #fa3c3f;\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 30;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "LF Cam Hacking"))
        self.label.setText(_translate("dialog", "ВЗЛОМ КАМЕР"))
        self.pushButton.setText(_translate("dialog", "Search"))
        self.pushButton_2.setText(_translate("dialog", "Explore"))
        self.pushButton_4.setText(_translate("dialog", "Hack"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())