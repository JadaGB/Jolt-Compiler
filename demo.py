import sys
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QColor, QTextCharFormat, QSyntaxHighlighter, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QWidget,QVBoxLayout,QPushButton
from jolt_yacc import *
from jolt_lex import reserved

class MyHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(MyHighlighter, self).__init__(parent)
        self.highlighting_rules = []
        
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.blue)
        keyword_format.setFontWeight(QFont.Bold)
        keywords = reserved #['if', 'else', 'for', 'while']
        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            self.highlighting_rules.append((pattern, keyword_format))
        
        literal_format = QTextCharFormat()
        literal_format.setForeground(Qt.darkGreen)
        pattern = QRegExp("\\b[0-9]+\\b")
        self.highlighting_rules.append((pattern, literal_format))
        
        operator_format = QTextCharFormat()
        operator_format.setForeground(Qt.red)
        opertors =  ['+', '-', '*', '/', '%', '=', '==','<', '>','>=','<=', '?=', '?', '|', '@']
        for op in opertors:
            pattern = QRegExp("\\" + op)
            self.highlighting_rules.append((pattern, operator_format))
        
        comment_format = QTextCharFormat()
        comment_format.setForeground(Qt.gray)
        pattern = QRegExp("~.*~")
        self.highlighting_rules.append((pattern, comment_format))
        # pattern = QRegExp("/\*.*\*/")
        pattern.setMinimal(True)
        # self.highlighting_rules.append((pattern, comment_format))

    def highlightBlock(self, text):
        for pattern, char_format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, char_format)
                index = expression.indexIn(text, index + length)
                
class IDE(QMainWindow):
    def __init__(self):
        super().__init__()
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

        self.highlighter = MyHighlighter(self.textEdit)

        self.setGeometry(400, 100, 800, 600)
        self.setWindowTitle('Jolt IDE')
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
        content = self.textEdit.toPlainText().splitlines()
        output = parseInput(content)
        self.output_editor.clear()
        for line in output:
            self.output_editor.insertPlainText(str(line))
            self.output_editor.insertPlainText("\n")
        # return content

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ide = IDE()
    ide.show()
    sys.exit(app.exec_())
