import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QWidget,QVBoxLayout,QPushButton
from jolt_yacc import *

class IDE(QMainWindow):
    def __init__(self):
        super().__init__()
         # Create text edit widgets
        # self.code_input = QTextEdit(self)
        # self.code_input.setGeometry(0, 0, 400, 600)
        # self.code_input.setPlainText('')

        # self.output_display = QTextEdit(self)
        # self.output_display.setGeometry(400, 0, 400, 600)
        # self.output_display.setReadOnly(True)

        # # Create main widget and layout
        # main_widget = QWidget(self)
        # self.setCentralWidget(main_widget)
        # layout = QVBoxLayout(main_widget)

        # # Create text editor for code
        # code_editor = QTextEdit()
        # layout.addWidget(code_editor)

        # # Create text editor for output
        # output_editor = QTextEdit()
        # output_editor.setReadOnly(True)
        # layout.addWidget(output_editor)

        self.initUI()

    def initUI(self):
        #Create main widget and layout
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        self.textEdit = QTextEdit()
        self.textEdit.setGeometry(0, 0, 400, 600)
        layout.addWidget(self.textEdit)

        self.output_editor = QTextEdit()
        self.output_editor.setReadOnly(True)
        layout.addWidget(self.output_editor)

        # create menu bar and file menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        # create file menu actions
        newFileAction = QAction('&New', self)
        newFileAction.setShortcut('Ctrl+N')
        newFileAction.triggered.connect(self.newFile)

        openFileAction = QAction('&Open', self)
        openFileAction.setShortcut('Ctrl+O')
        # openFileAction.triggered.connect(self.openFile)
        openFileAction.triggered.connect(self.openFile)

        saveFileAction = QAction('&Save', self)
        saveFileAction.setShortcut('Ctrl+S')
        saveFileAction.triggered.connect(self.saveFile)

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)

        # add actions to file menu
        fileMenu.addAction(newFileAction)
        fileMenu.addAction(openFileAction)
        fileMenu.addAction(saveFileAction)
        fileMenu.addAction(exitAction)

        # Add a button widget
        self.button = QPushButton('Run', self)
        self.button.clicked.connect(self.run)
        self.button.move(680, 3)

        self.setGeometry(400, 100, 800, 600)
        self.setWindowTitle('Python IDE')
        self.show()

    def openFile(self):
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/')
            if fname[0]:
                with open(fname[0], 'r') as f:
                    text = f.read()
                    self.textEdit.setText(text)

    def newFile(self):
        self.textEdit.clear()

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt)')
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def run(self):
        content = self.textEdit.get("1.0","end-1c").splitlines()
        # file = saveToFile()
        output = parseInput(content)
        self.output_editor.clear()
        # output_widget.delete("1.0", "end-1c")

        for line in reversed(output):
            self.output_editor.insert("1.0", line)
            self.textEdit.setText(line)
            # output_widget.insert("1.0", "\n")
            # print(line)
        return content

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ide = IDE()
    ide.show()
    sys.exit(app.exec_())
