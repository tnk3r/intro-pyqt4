#!/usr/bin/python


import sys
from PyQt4.QtGui import QApplication, QMainWindow, QAction

from PyQt4.QtGui import QPixmap, QLabel, QPushButton, QLineEdit

class main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(400, 600)


        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(app.quit)

        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu("&File")
        self.file_menu.addAction(exitAction)

        #self.setWindowTitle("Hello NSL!")

        # # 2
        # self.bg_img = QPixmap('img/stars2.jpg')
        # self.bg = QLabel(self)
        # self.bg.setPixmap(self.bg_img)
        # self.bg.resize(400, 600)

        # # 1
        # self.textfield = QLineEdit(self)
        # self.textfield.move(90, 60)
        # self.textfield.setStyleSheet("background-color: white;")
        # self.textfield.setFixedWidth(220)

        # # 3
        # self.button = QPushButton("Print", self)
        # self.button.move(150, 350)
        # self.button.clicked.connect(self.console_print)

        # # 4
        # self.label = QLabel("", self)
        # self.label.move(90, 150)
        # self.label.setFixedSize(220, 60)
        # self.label.setStyleSheet("color: red; font-size: 40px;")


    def console_print(self, event):
        print "Hello NSL"

        # # 3
        # print self.textfield.text()

        # # 4
        # self.label.setText(self.textfield.text())

        # # 5
        # self.textfield.clear()


app = QApplication(sys.argv)
window = main()
window.show()

sys.exit(app.exec_())

