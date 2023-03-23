
#Install Pygments- 'pip install pygments'

from tkinter import *
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import RtfFormatter
import tkinter.filedialog as fdialog
from jolt_yacc import parseifileinput 

root = Tk()

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
    
    file = saveToFile()
    code = parseifileinput(file)
    
    output_widget.insert(str(code))



text_widget = Text(root, height = 30, width = 100)
output_widget = Text(root, height = 10, width = 100, bg="light blue")
l = Label(root,text= "Hi")




save = Button(text="Save", height = 2,width = 10, command = lambda:run())



l.pack()
save.pack()
text_widget.pack()
output_widget.pack()



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
