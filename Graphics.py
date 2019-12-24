from tkinter import *
from company import Company


class GUI:
    root = Tk()

    def __init__(self, root):
        self.root = root

    @staticmethod
    def show_root(root):
        root.title("Компания \"Мебель-Хаус\"")
        root.geometry("700x600")
        lab = Label(root, text="Компания \"Мебель-Хаус\"\nКоманды:", font=("Verdana", 20, "bold"))
        btn1 = Button(root, text="1.Нанять", font=("Verdana", 16, "bold"))
        btn2 = Button(root, text="2.Информация о сотрудниках", font=("Verdana", 16, "bold"))
        btn3 = Button(root, text="3.Рассчитать оплату(для почасовых работников)", font=("Verdana", 16, "bold"))
        btn4 = Button(root, text="4.Выйти", font=("Verdana", 16, "bold"))
        lab.pack()
        btn1.pack()
        btn2.pack()
        btn3.pack()
        btn4.pack()
        btn1.bind('<Button-1>', Company(root).command_1)
        btn2.bind('<Button-1>', Company(root).command_2)
        btn4.bind('<Button-1>', Company(root).exit_)
        root.mainloop()
