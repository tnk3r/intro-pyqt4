#!/usr/bin/python

import sys
from PyQt4.QtGui import QApplication, QMainWindow, QLabel, QPixmap, QLineEdit, QPushButton, QShortcut, QKeySequence

# from PyQt5.QtWidgets import QApplication, QMainWindow
class customQLabel(QLabel):

    def __init__(self, string, parent, x_move=0, y_move=0, x_size=100, y_size=50, stylesheet=""):
        QLabel.__init__(self, parent=parent)
        self.setText(string)
        self.setFixedSize(x_size, y_size)
        self.move(x_move, y_move)
        self.setStyleSheet(stylesheet)

class example1(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(0, 0, 400, 600)

        self.new_label = customQLabel("LABEL!", self, 50, 100, 100, 100, "color: red;")

        self.bg = QLabel(self)
        self.bg.setStyleSheet("background-color: rgb(255,123,100);")
        self.bg.setFixedSize(400, 600)

        # self.hello_label = QLabel("Hello NSL!!!", self)
        # self.hello_label.setStyleSheet("font-size: 50px;")
        # self.hello_label.setFixedSize(300, 50)
        # self.hello_label.move(250, 250)
        # self.hello_label.mousePressEvent = self.print_function

        self.bg_img = QPixmap('img/stars2.jpg')
        self.bg.setPixmap(self.bg_img)
        self.bg.resize(400, 600)

        self.textfield = QLineEdit("type your name..", self)
        self.textfield.move(20, 30)
        self.textfield.setFixedWidth(250)

        self.button = QPushButton("Save Name", self)
        self.button.move(300, 30)
        self.button.clicked.connect(self.print_name)

        QShortcut(QKeySequence("Return"), self.textfield, self.print_name)

        # self.timer = QLabel("", self)
        # self.timer.move(90, 120)
        # self.timer.setFixedSize(220, 60)
        # self.timer.setStyleSheet("color: white; border: 1px Solid White; font-size: 40px")
        # self.timer.setAlignment(Qt.AlignCenter)
        self.timer = customQLabel("", self, 90, 120, 220, 60 "color: white; border: 1px Solid White; font-size: 40px")


        self.show()
        self.raise_()

    def print_function(self, event):
        print "Pressed Hello NSL Button"

    def print_name(self):
        print self.textfield.text()


class signals(QThread):

    time_signal = pyqtSignal(str)
    style_signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            date = time.strftime('%I:%M:%S')
            self.style_signal.emit("color: white; border: 1px Solid White; font-size: 25px")
            self.time_signal.emit(date)

            time.sleep(1)

            date = time.strftime('%I %M %S')
            self.style_signal.emit("color: Red; border: 3px Solid Orange; font-size: 25px")
            self.time_signal.emit(date)

            time.sleep(1)





app = QApplication(sys.argv)
window = example1()
sys.exit(app.exec_())
