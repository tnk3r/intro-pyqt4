#!/usr/bin/python

## Example of simple image loading Gui. Supports only QPixmap Format, listed below

#( BMP, GIF, JPG, JPEG, PNG, PBM, PGM, PPM, XBM, XPM )

import sys
from PyQt4.QtGui import QApplication, QMainWindow, QAction, QPixmap, QLabel, QFileDialog

class main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Images!")

    ## Create BackGround to Load images into

        self.bg = QLabel(self)
        self.bg.move(0, 30)
        self.bg.resize(400, 550)
        self.bg.setStyleSheet("background-color: black;")
        self.setGeometry(100, 100, 400, 600)

        self.button = QLabel("Open..", self)
        self.button.setFixedSize(55, 24)
        self.button.setStyleSheet("border: 1px solid black; font-size: 15px")
        self.button. move(330, 2)
        self.button.mousePressEvent = self.open_label

    ## Create File QAction for MenuBar

        openFileAction = QAction('&Open Image...', self)
        openFileAction.setShortcut('Ctrl+O')
        openFileAction.setStatusTip('Open Image File')

    ## Connect to the open_image function

        openFileAction.triggered.connect(self.open_file)

    #Exit Action

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(app.quit)

    ## Create Menu Bar and Add File Menu to it

        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu("&File")

    ## Link the File Menu to the QActions.

        self.file_menu.addAction(openFileAction)
        self.file_menu.addAction(exitAction)

    def open_label(self, event):

        self.open_file()

    def open_file(self):

        filename = QFileDialog.getOpenFileName()
        print filename

     ## import Image as a QPixMap

        self.bg_img = QPixmap(filename)

    ## Resize Window to the Size of opened image

        self.setFixedSize(self.bg_img.size())  #<---~ 'self is the QMainWindow'
        self.bg.setFixedSize(self.bg_img.size())


    ## set the Image to the background QLabel

        self.bg.setPixmap(self.bg_img)

        self.button.move(int(self.bg_img.width()) - 70, 2)


app = QApplication(sys.argv)
window = main()
window.show()
window.raise_()


sys.exit(app.exec_())

