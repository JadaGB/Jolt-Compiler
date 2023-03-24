from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QColor, QTextCharFormat, QSyntaxHighlighter, QFont
from PyQt5.QtWidgets import QApplication, QTextEdit
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

class MyEditor(QTextEdit):
    def __init__(self, parent=None):
        super(MyEditor, self).__init__(parent)
        self.highlighter = MyHighlighter(self.document())

if __name__ == '__main__':
    app = QApplication([])
    editor = MyEditor()
    editor.show()
    app.exec_()

