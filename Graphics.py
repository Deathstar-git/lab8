from tkinter import *
from company import Company
from tkinter.messagebox import showinfo


class GUI:
    root = Tk()

    def __init__(self, root):
        self.root = root

    @staticmethod
    def prog_info():
        t = "База данных компании \"Мебель-Хаус\"\n"
        t += "Предназначена для:\n"
        t += "Добавления новых сотрудников\n"
        t += "Получения информации о сотрудниках\n"
        t += "Расчёта оплаты\n"
        t += "Наша почта:mebel_house@mail.ru"
        showinfo("О программе", t)

    @staticmethod
    def show_root(root):
        root.title("Компания \"Мебель-Хаус\"")
        root.geometry("700x600")
        lab = Label(root, text="Компания \"Мебель-Хаус\"\nКоманды:", font=("Verdana", 20, "bold"))
        btn1 = Button(root, text="1.Нанять", font=("Verdana", 16, "bold"))
        btn2 = Button(root, text="2.Информация о сотрудниках", font=("Verdana", 16, "bold"))
        btn3 = Button(root, text="3.Рассчитать оплату(для почасовых работников)", font=("Verdana", 16, "bold"))
        btn4 = Button(root, text="4.О программе", font=("Verdana", 16, "bold"), command=GUI.prog_info)
        btn5 = Button(root, text="5.Выйти", font=("Verdana", 16, "bold"))
        lab.pack()
        btn1.pack()
        btn2.pack()
        btn3.pack()
        btn4.pack()
        btn5.pack()
        btn1.bind('<Button-1>', Company(root).command_1)
        btn2.bind('<Button-1>', Company(root).command_2)
        btn3.bind('<Button-1>', Company(root).command_3)
        btn4.bind('<Button-1>')
        btn5.bind('<Button-1>', Company(root).exit_)
        root.mainloop()
