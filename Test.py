from tkinter import Tk, Text
from tkinter import ttk
from ScrollableNotebook import ScrollableNotebook
root = Tk()
root.title("Scrollable Notebook")
root.geometry("500x500")
s = ttk.Style()
s.theme_use("clam")
counter = 0
notebook = ScrollableNotebook(root, tabmenu=True)
notebook.pack(fill="both", expand=True)
frames = []
def remove_tab():
    current_index = notebook.index("current")
    notebook.forget(notebook.tabs()[current_index])
    try:
        frames[current_index-1].focus_set()
    except:
        pass
def add_tab():
    global counter
    frame = Text(notebook)
    frame.pack(fill="both", expand=True)
    frames.append(frame)
    notebook.add(frame, text="Tab {}".format(counter))
    tabid = notebook.tabs()[-1]
    notebook.select(tabid)
    frames[-1].focus_set()
    counter += 1
ttk.Button(root, text="Remove", command=remove_tab).pack()
ttk.Button(root, text="Add", command=add_tab).pack()
add_tab()
frames[0].focus_set()
def focus_current(event):
    current_focus = notebook.index("current")
    frames[current_focus].focus_set()
root.bind("<Button-1>", focus_current)
root.mainloop()