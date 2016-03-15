from PyQt4 import QtGui, QtCore
from fontlib import fontlib

class notify_dialog(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setFixedSize(800, 480)
        self.move(0, 0)
        self.background = QtGui.QLabel(self)
        self.setStyleSheet("background-color: rgba(0,0,0,200);")
        self.fontlib = fontlib()

        self.alert_ok_button = QtGui.QLabel(" OK ", self)
        self.alert_ok_button.setStyleSheet(self.fontlib.alert_ok)
        self.alert_ok_button.move(340, 350)
        self.alert_ok_button.setAlignment(QtCore.Qt.AlignVCenter)
        self.alert_ok_button.setFixedSize(120, 60)
        self.alert_ok_button.mousePressEvent = self.alert_close

        self.alert_text = QtGui.QLabel("", self)
        self.alert_text.setFixedSize(760,200)
        self.alert_text.setStyleSheet(self.fontlib.alert_text)
        self.alert_text.move(20, 100)

    def alert(self, message):
        lines = []
        for i in xrange(0, len(str(message)), 40):
            lines.append(str(message)[i:i+40])
        self.alert_text.setAlignment(QtCore.Qt.AlignCenter)
        print lines
        self.alert_text.setText('\n'.join(lines))
        self.show()
        self.raise_()

    def alert_close(self, event):
        self.hide()


