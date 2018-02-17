#!/usr/bin/python

import sys
from PyQt4.QtGui import QApplication, QMainWindow

class example1(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # self.setFixedSize(400, 400)

        # self.setGeometry(0, 0, 300, 300)
        # self.setGeometry(300, 300, 400, 400)

        # self.setFixedWidth(800)
        # self.setFixedHeight(800)

        self.show()
        self.raise_()


app = QApplication(sys.argv)
window = example1()
sys.exit(app.exec_())



