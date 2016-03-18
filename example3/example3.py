import sys
from PyQt4.QtGui import QApplication, QMainWindow, QFileDialog, QTextEdit, QAction

class main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Text!")

        self.textField = QTextEdit(self)

    # Setup the Menu Actions adn Shortcuts

        self.saveAction = QAction("Save...", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save_txt)

        self.quitAction = QAction("Exit", self)
        self.quitAction.setShortcut("Ctrl+Q")
        self.quitAction.triggered.connect(app.quit)

        self.openAction = QAction("Open...", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open_txt)

        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu("&File")
        self.file_menu.addAction(self.openAction)
        self.file_menu.addAction(self.saveAction)
        self.file_menu.addAction(self.quitAction)

    # sets the QTextEdit as the main and central Widget

        self.setCentralWidget(self.textField)

    # Add some keyboard shortcuts for Text Editing

        self.cutAction = QAction(self)
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.textField.cut)

        self.copyAction = QAction(self)
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.textField.copy)

        self.pasteAction = QAction("Paste from clipboard",self)
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.textField.paste)

        self.setGeometry(100, 100, 600, 600)

    def open_txt(self):

    # Get filename Dialog and show only .txt files

        self.filename = QFileDialog.getOpenFileName(self, 'Open File',".","(*.txt)")

    # Return if Filename is empty, to handle pressing 'Cancel'

        if self.filename == "":
            return 1
    # Put the contents of 'filename' into the QTextField with setText()

        if self.filename:
            with open(self.filename, "rt") as file:
                self.textField.setText(file.read())

    def write_file(self):

        self.filename = QFileDialog.getSaveFileName(self, 'Save File')

        if self.filename == "":
            return 1
    # Append .txt to filename
        if not self.filename.endsWith(".txt"):
            self.filename += ".txt"

    # Write to file, Contents of Text Field
        with open(self.filename,"wt") as file:
            file.write(self.textField.text)

    def save_txt(self):
        try:
            if not self.filename:
                self.write_file()
            else:
                with open(self.filename,"wt") as file:
                    file.write(self.textField.text)

        except StandardError as msg:
            print str(msg)
            self.write_file()

app = QApplication(sys.argv)
window = main()
window.show()
sys.exit(app.exec_())