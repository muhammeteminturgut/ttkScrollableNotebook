from tkinter import *
from tkinter import ttk
from ScrollableNotebook import *

root=Tk()
root.title("Example")
notebook=ScrollableNotebook(root,wheelscroll=True,tabmenu=True)
frame1=Frame(notebook)
frame2=Frame(notebook)
frame3=Frame(notebook)
frame4=Frame(notebook)
notebook.add(frame1,text="I am Tab One")
notebook.add(frame2,text="I am Tab Two")
notebook.add(frame3,text="I am Tab Three")
notebook.add(frame4,text="I Forgot How to Count")
notebook.pack(fill="both",expand=True)
text=Text(frame1)
text.pack()
Label(frame2,text="I am Frame 2").pack()
Label(frame3,text="I am Frame 3").pack()
Label(frame4,text="You know i'm Frame 4").pack()
text.insert(INSERT,"Hello World!")
root.mainloop()
