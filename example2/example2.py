#!/usr/bin/python

## Example of simple image loading Gui. Supports only QPixmap Format, listed below

#( BMP, GIF, JPG, JPEG, PNG, PBM, PGM, PPM, XBM, XPM )

import sys
from PyQt4.QtGui import QApplication, QMainWindow, QAction, QPixmap, QLabel, QFileDialog


class main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(400, 600)
        self.setWindowTitle("Images!")

    ## Create BackGround to Load images into

        self.bg = QLabel(self)
        self.bg.resize(400, 600)
        self.bg.setStyleSheet("background-color: black;")

    ## Create File QAction for MennuBar

        openFileAction = QAction('&Open Image...', self)
        openFileAction.setShortcut('Ctrl+O')
        openFileAction.setStatusTip('Open Image File')

    ## Connect to the open_image function

        openFileAction.triggered.connect(self.open_file)

    #Exit Action

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(app.quit)

    ## Create Menu Bar and Add File Menu to it

        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu("&File")

    ## Link the File Menu to the QActions.

        self.file_menu.addAction(openFileAction)
        self.file_menu.addAction(exitAction)


    def open_file(self):

        filename = QFileDialog.getOpenFileName()
        print filename

     ## import Image as a QPixMap

        self.bg_img = QPixmap(filename)

    ## Resize Window to the Size of opened image

        self.setFixedSize(self.bg_img.size())  #<---~ 'self is the QMainWindow'
        self.bg.resize(self.bg_img.size())

    ## set the Image to the background QLabel

        self.bg.setPixmap(self.bg_img)

app = QApplication(sys.argv)
window = main()
window.show()

sys.exit(app.exec_())

