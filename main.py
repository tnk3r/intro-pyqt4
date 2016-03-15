#!/usr/bin/python

import sys
from PyQt4.QtGui import QApplication, QLabel, QWidget, QLineEdit, QPushButton


class main_window(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Hello NSL")
        self.resize(400, 400)
        self.move(0, 0)
        self.button_font = "font-family: Helvetica;"\
                           "font-size: 40px;"\
                           "border: 2px solid black;"\
                           "border-radius: 5px;"\
                           "background-color: white;"


        self.textfield = QLineEdit(self)
        self.textfield.move(10, 20)
        self.textfield.setFixedWidth(220)

        self.button = QPushButton("Clear", self)
        self.button.move(250, 15)
        self.button.clicked.connect(self.clearField)



    def clearField(self, event):
        self.textfield.setText("")

    def quit(self, event):
        self.close()


app = QApplication(sys.argv)
window = main_window()
window.show()


sys.exit(app.exec_())