import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QAction, QFileDialog, QMenuBar, QMenu, QMainWindow

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Two Widgets with QTextEdit')
        self.setGeometry(100, 100, 500, 500)

        # Create the first QTextEdit widget
        self.text_edit1 = QTextEdit(self)
        self.text_edit1.setPlaceholderText('Enter some text here...')

        # Create the second QTextEdit widget
        self.text_edit2 = QTextEdit(self)
        self.text_edit2.setPlaceholderText('Enter some more text here...')

        menubar = QMenuBar(self)
        fileMenu = menubar.addMenu('File')

        openFile = QAction('Open', self)
        openFile.triggered.connect(open_file)
        fileMenu.addAction(openFile)
        # openFile.triggered.connect(showDialog)
        # fileMenu.addAction(openFile)

        exitApp = QAction('Exit', self)
        exitApp.triggered.connect(self.close)
        fileMenu.addAction(exitApp)

        # Create a layout and add the widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit1)
        layout.addWidget(self.text_edit2)

        # Set the layout for the window
        self.setLayout(layout)

def open_file(self):
        # fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        # if fileName:
        #     print(fileName)
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if filename:
            with open(filename, "r") as file:
                self.text_edit.setPlainText(file.read())

def showDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
