from tkinter import *


def exit_(event):
    root.destroy()
    del event


def caption(event):
    t = ent.get()
    lbl.configure(text=t)
    del event


root = Tk()
ent = Entry(root, width=40)
lbl = Label(root, width=80)
btn4 = Button(root, text="4.Выйти", font=("Verdana", 16, "bold"))

ent.pack()
lbl.pack()
btn4.pack()
ent.bind('<Return>', caption)
btn4.bind('<Button-1>', exit_)

root.mainloop()
