import sys
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QPixmap, QColor, QTextCharFormat, QSyntaxHighlighter, QFont, QIcon
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QWidget,QVBoxLayout,QPushButton
from jolt_yacc import *
from jolt_lex import reserved

class MyHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(MyHighlighter, self).__init__(parent)
        self.highlighting_rules = []
        
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor('#9370DB'))
        #get reserved words from lex
        keywords = reserved 
        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            self.highlighting_rules.append((pattern, keyword_format))
        
        literal_format = QTextCharFormat()
        literal_format.setForeground(QColor(173,216,230))
        pattern = QRegExp("\\b[0-9]+\\b")
        self.highlighting_rules.append((pattern, literal_format))
        
        operator_format = QTextCharFormat()
        operator_format.setForeground(QColor(255,140,0))
        opertors =  ['+', '-', '*', '/', '%', '=', '==','<', '>','>=','<=', '?=', '?', '|', '@']
        for op in opertors:
            pattern = QRegExp("\\" + op)
            self.highlighting_rules.append((pattern, operator_format))
        
        bracket_format = QTextCharFormat()
        bracket_format.setForeground(QColor(255,200,0))
        bracket = ['(',')']
        for b in bracket:
            pattern = QRegExp("\\" + b)
            self.highlighting_rules.append((pattern, bracket_format))
        
        comment_format = QTextCharFormat()
        comment_format.setForeground(Qt.gray)
        pattern = QRegExp("~.*~")
        self.highlighting_rules.append((pattern, comment_format))
        pattern.setMinimal(True)

    def highlightBlock(self, text):
        for pattern, char_format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, char_format)
                index = expression.indexIn(text, index + length)
                
class IDE(QMainWindow):
    pause = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
         #testing welcome screen
        self.welcome_widget = QWidget(self)
        self.setCentralWidget(self.welcome_widget)
        self.welcome_widget.setGeometry(150, 30, 100, 100)
        self.welcome_widget.setStyleSheet("background-color: #6600cc")
        layout1 = QVBoxLayout(self.welcome_widget)

        self.welcome_stmt = QLabel("WELCOME", self.welcome_widget)
        self.welcome_stmt.setAlignment(Qt.AlignCenter)
        self.welcome_stmt.move(500,550)
        self.welcome_stmt.setFont(QFont('Verdana',32))
        self.welcome_stmt.setStyleSheet("color: #ffffff")
        layout1.addWidget(self.welcome_stmt) 

        logo = QLabel(self)
        # pixmap = QPixmap("logo1.png")
        pixmap = QPixmap("C:/Users/river/Downloads/APL/APL/Jolt-Compiler/logo1.png")
        pixmap = pixmap.scaled(400,400)
        logo.setAlignment(Qt.AlignCenter)
        logo.setPixmap(pixmap)
        layout1.addWidget(logo)

        self.welcome_stmt1 = QLabel("Jolt-Compiler V.1.0 \n Developed by Jada Bailey and Garcian Mairs", self.welcome_widget)
        self.welcome_stmt1.setAlignment(Qt.AlignCenter)
        self.welcome_stmt1.setFont(QFont('Verdana',12))
        self.welcome_stmt1.setStyleSheet("color: #ffffff")
        layout1.addWidget(self.welcome_stmt1)
        
        self.gotoeditor = QPushButton('Go To Compiler',self.welcome_widget)
        self.gotoeditor.setFont(QFont('Verdana',12))
        self.gotoeditor.setStyleSheet("background-color: #ffffff;border-radius: 12px")
        self.gotoeditor.clicked.connect(self.showwindows)
        self.gotoeditor.move(300,400)
        self.gotoeditor.resize(200,35)

        self.setGeometry(400, 100, 800, 600)
        self.setWindowTitle('Jolt IDE')
        self.setWindowIcon(QIcon("C:/Users/river/Downloads/APL/APL/Jolt-Compiler/logo1.png"))
        self.show()

    def openFile(self):
            fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'Text Files (*.jolt)')
            if fname[0]:
                with open(fname[0], 'r') as f:
                    text = f.read()
                    self.textEdit.setText(text)

    def newFile(self):
        self.textEdit.clear()

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.jolt)')
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())

    #Compiles code in editor when button clicked
    def compile(self):
        errors = 0
        content = self.textEdit.toPlainText().splitlines() #get text from editor
        output = parseInput(content) #pass data to parser
        self.output_editor.clear()
        for line in output: #loops through the parser results
            if "Error" in str(line): #prints errors & set color to red
                errors = errors + 1
                self.output_editor.setStyleSheet("background-color: #E0BBE4; color: #e60000")
                self.output_editor.insertPlainText(str(line))
                self.output_editor.insertPlainText("\n")
        if errors == 0: #if no errors found, set color back to default
            self.output_editor.setStyleSheet("background-color: #E0BBE4; color: #000000")
            self.output_editor.insertPlainText("Compiled Successfully!")
        err = ("Errors Found: ",errors)
        self.output_editor.insertPlainText(str(err))

    #Executes code in editor when button clicked
    def run(self):
        content = self.textEdit.toPlainText().splitlines() #get text from editor
        output = parseInput(content) #pass data to parser
        self.output_editor.clear()
        for line in output: #loops through the parser results
            if "loop" not in str(line):
                if "Error" in str(line): #prints errors & set color to red
                    self.output_editor.setStyleSheet("background-color: #E0BBE4; color: #e60000")
                    self.output_editor.insertPlainText(str(line))
                    self.output_editor.insertPlainText("\n")
                else:
                    self.output_editor.setStyleSheet("background-color: #E0BBE4; color: #000000")
                    self.output_editor.insertPlainText(str(line))
                    self.output_editor.insertPlainText("\n")

    def showwindows(self):
        self.welcome_widget.hide()

        #Create main widget and layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_widget.setStyleSheet("background-color: #303030")
        layout = QVBoxLayout(self.main_widget)

        #Create menu bar and file menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        menubar.setStyleSheet("color: #ffffff")
        menubar.setFont(QFont('Verdana', 10))

        #Create file menu actions
        newFileAction = QAction('&New', self)
        newFileAction.setShortcut('Ctrl+N')
        newFileAction.triggered.connect(self.newFile)

        openFileAction = QAction('&Open', self)
        openFileAction.setShortcut('Ctrl+O')
        openFileAction.triggered.connect(self.openFile)

        saveFileAction = QAction('&Save', self)
        saveFileAction.setShortcut('Ctrl+S')
        saveFileAction.triggered.connect(self.saveFile)

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)

        #Add actions to file menu
        fileMenu.addAction(newFileAction)
        fileMenu.addAction(openFileAction)
        fileMenu.addAction(saveFileAction)
        fileMenu.addAction(exitAction)

        layout.addWidget(menubar) #Add menu to window

        #Add text editor
        self.textEdit = QTextEdit()
        self.textEdit.setStyleSheet("background-color: #262626;color: #4874f4")
        self.textEdit.setFont(QFont('Verdana', 12))
        self.textEdit.setGeometry(0, 0, 400, 600)
        layout.addWidget(self.textEdit)

        #Add text editor
        self.output_editor = QTextEdit()
        self.output_editor.setStyleSheet("background-color: #E0BBE4; color: #000000")
        self.output_editor.setFont(QFont('Verdana', 12))
        self.output_editor.setReadOnly(True)
        layout.addWidget(self.output_editor)

        #Add button to widget
        self.button = QPushButton('Compile', self.main_widget)
        self.button.clicked.connect(self.compile)
        self.button.setStyleSheet("background-color: #ff471a; color: #ffffff;border-radius: 8px")
        self.button.setFont(QFont('Verdana',10))
        self.button.move(570, 3)

        #Add button to widget
        self.button = QPushButton('Run', self.main_widget)
        self.button.setStyleSheet("background-color: #ff471a; color: #ffffff;border-radius: 8px")
        self.button.setFont(QFont('Verdana',10))
        self.button.clicked.connect(self.run)
        self.button.move(680, 3)

        #invoke syntax highlighting
        self.highlighter = MyHighlighter(self.textEdit) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ide = IDE()
    ide.show() #displays widget
    sys.exit(app.exec_()) #executes events in gui
