#Install Pygments- 'pip install pygments'

from tkinter import *
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import RtfFormatter
import tkinter.filedialog as fdialog
from jolt_yacc import *

root = Tk()
root.title("Jolt IDE")

file_path = ""

def openFile():
    file_path = fdialog.askopenfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "r") as f:
            contents = f.read()
        text_widget.delete("1.0", "end-1c")
        text_widget.insert("1.0", contents)

def saveToFile():
    # get the text content from the text widget
    contents = text_widget.get("1.0","end-1c")
     # open a file dialog to get the file name and location
    file_path = fdialog.asksaveasfilename(defaultextension=".txt")
    
    # write the text content to the file
    with open(file_path, "w") as file:
        file.write(contents)
    
    return file_path

def run():
    content = text_widget.get("1.0","end-1c").splitlines()
    # file = saveToFile()
    output = parseInput(content)
    output_widget.delete("1.0", "end-1c")

    for line in reversed(output):
        output_widget.insert("1.0", line)
        output_widget.insert("1.0", "\n")
        # print(line)
    return content

text_widget = Text(root, height = 30, width = 100)
output_widget = Text(root, height = 10, width = 100, bg="light blue")
l = Label(root,text= "Jolt Compiler")

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command = lambda:openFile())
file_menu.add_command(label="Save", command = lambda:saveToFile())
menu_bar.add_cascade(label="File", menu=file_menu)

runBtn = Button(text="Run", height = 2,width = 10, command = lambda:run())
# open = Button(text="Open File", height = 2,width = 10, command = lambda:openFile())

# l.pack()
# save.pack()
# open.pack()
runBtn.pack(side="right", anchor="nw")
# file_menu.pack()
text_widget.pack()
output_widget.pack()

root.config(menu=menu_bar)
root.mainloop()

# def on_key_press(event):
#     code = text_widget.get("1.0", "end")
#     lexer = PythonLexer()
#     formatter = RtfFormatter()
#     highlighted_code = highlight(code, lexer, formatter)
#     text_widget.delete("1.0", "end")
#     text_widget.insert("1.0", highlighted_code, "highlighted")

# text_widget.bind("<Key>", on_key_press)
# #text_widget.tag_configure("highlighted", background= HtmlFormatter.get_style_defs()["background-color"])