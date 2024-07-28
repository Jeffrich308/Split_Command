# -------------------------------------------------------------------------------
# Name:             Generic Startup Loading a UI File
# Purpose:          Simplify a GUI interface app
#
# Author:           Jeffreaux
#
# Created:          20Mar23
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLineEdit, QPlainTextEdit
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("Split_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")

        self.txtInputSpace = self.findChild(QLineEdit, "txtInputSpace")
        self.txtInputComma = self.findChild(QLineEdit, "txtInputComma")
        self.pteResults = self.findChild(QPlainTextEdit, "pteResults")

        self.actExit = self.findChild(QAction, "actExit")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)

        self.txtInputSpace.returnPressed.connect(self.split_space)
        self.txtInputComma.returnPressed.connect(self.split_comma)

        self.actExit.triggered.connect(self.closeEvent)

        # Show the app
        self.show()

    def split_space(self):
        print("Will split on spaces")
        string = self.txtInputSpace.text()  # Gets text from LineEdit box, assigns to var
        print(string)
        spaces = string.split(' ')  # Parses string at spaces.  Returns a List
        print(spaces)
        for space in spaces:  # Cycles through list and print each variable to a line
            self.pteResults.appendPlainText(space)

    def split_comma(self):
        print("Will split on commas")
        string = self.txtInputComma.text()  # Gets text from LineEdit box, assigns to var
        print(string)
        commas = string.split(',')  # Parses string at commas.  Returns a List
        print(commas)
        for comma in commas:  # Cycles through list and print each variable to a line
            self.pteResults.appendPlainText(comma)

    
    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
