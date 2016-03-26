#!/usr/bin/python


# Check out: https://wiki.python.org/moin/PyQt/Tutorials
# SIP https://www.riverbankcomputing.com/software/sip/intro
# zetcode.com/gui/pyqt4/

# Class Reference:   http://pyqt.sourceforge.net/Docs/PyQt4/classes.html


import sys
from PyQt4.QtGui import QApplication, QMainWindow, QAction

from PyQt4.QtGui import QPixmap, QLabel, QPushButton, QLineEdit, QShortcut, QKeySequence
from PyQt4.QtCore import Qt

from PyQt4.QtCore import pyqtSignal, QThread

import time

class example1(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
#        self.setFixedSize(400, 400)
#        self.setGeometry(0, 0, 300, 300)
        # self.setGeometry(300, 300, 400, 400)


#        self.setFixedWidth(800)
#        self.setFixedHeight(800)

        # self.setWindowTitle("Hello NSL!")
        #
        # exitAction = QAction('&Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.triggered.connect(app.quit)
        #
        # self.menubar = self.menuBar()
        # self.file_menu = self.menubar.addMenu("&File")
        # self.file_menu.addAction(exitAction)


        # self.bg = QLabel(self)
#         self.bg.setStyleSheet("background-color: black;")


        # self.bg_img = QPixmap('img/stars2.jpg')
        # self.bg.setPixmap(self.bg_img)
        # self.bg.resize(400, 600)


        # self.textfield = QLineEdit("Enter your text", self)
        # self.textfield.move(90, 60)
        # self.textfield.setStyleSheet("background-color: white;")
        # self.textfield.setFixedWidth(220)


        # self.button = QPushButton("Print", self)
        # self.button.move(150, 400)
        # self.button.clicked.connect(self.button1_pressed)


        # self.label = QLabel("", self)
        # self.label.move(20, 200)
        # self.label.setFixedSize(350, 150)
        # self.label.setStyleSheet("color: white; font-size: 25px;")
        # self.label.setAlignment(Qt.AlignCenter)
#        self.label.setAlignment(Qt.AlignRight)


        # self.timer = QLabel("", self)
        # self.timer.move(90, 120)
        # self.timer.setFixedSize(220, 60)
        # self.timer.setStyleSheet("color: white; border: 1px Solid White; font-size: 40px")
        # self.timer.setAlignment(Qt.AlignCenter)


#        while True:
#            time.sleep(1)
#            date = time.strftime('%I:%M:%S')
#            self.timer.setStyleSheet("color: white; border: 1px Solid White; font-size: 25px")
#            self.timer.setText(date)
#            time.sleep(1)
#            date = time.strftime('%I %M %S')
#            self.timer.setStyleSheet("color: Red; border: 3px Solid Orange; font-size: 25px")
#            self.timer.setText(date)

        # QShortcut(QKeySequence("Return"), self.button, self.text_write)
        # self.thread = signals()
        # self.thread.time_signal.connect(self.timer.setText)
        # self.thread.time_signal.connect(self.write)
        #
        # self.thread.start()

        self.show()
        self.raise_()


    # def button1_pressed(self, event):
    #
    #     field = self.textfield.text()
    #
    #     text = ""
    #
    #     if len(field) > 25:
    #         for i in range(5):
    #             text += field[i*25:(i+1)*25]+"\n"
    #     else:
    #         text = field
    #
    #     print text
    #     self.label.setText(str(text))
    #
    #     self.textfield.clear()
    #
    #     self.thread.style_signal.connect(self.label.setStyleSheet)
    #
    # def text_write(self):
    #
    #     self.button1_pressed("1")
    #
    #
    # def write(self, message):
    #
    #     print message


# class signals(QThread):
#
#     time_signal = pyqtSignal(str)
#     style_signal = pyqtSignal(str)
#
#     def __init__(self):
#         QThread.__init__(self)
#
#     def run(self):
#         while True:
#             date = time.strftime('%I:%M:%S')
#             self.style_signal.emit("color: white; border: 1px Solid White; font-size: 25px")
#             self.time_signal.emit(date)
#
#             time.sleep(1)
#
#             date = time.strftime('%I %M %S')
#             self.style_signal.emit("color: Red; border: 3px Solid Orange; font-size: 25px")
#             self.time_signal.emit(date)
#
#             time.sleep(1)


app = QApplication(sys.argv)
window = example1()
sys.exit(app.exec_())



### QWidget to import into other scripts