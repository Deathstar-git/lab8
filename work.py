from tkinter import *


class Work:
    _duration = ' '

    def __init__(self, duration=''):
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, dur):
        self._duration = dur


class Hourlywork(Work):
    duration = "Доставка мелких заказов на дом"

    def __init__(self, duration):
        super().__init__(duration)


class Wagework(Work):
    duration = "Водитель транспорта для доставки товаров"

    def __init__(self, duration):
        super().__init__(duration)


class ManagerWork(Work):
    duration = "Продажа,ведение документационных дел,работа с персоналом"

    def __init__(self, duration):
        super().__init__(duration)


class SupervisorWork(Work):
    duration = "Контроль работы сотрудников - почасовых рабочих, наёмных рабочих, менеджеров "

    def __init__(self, duration):
        super().__init__(duration)


class CurrentWork:

    @staticmethod
    def unification(workers, rt):
        win = Toplevel(rt)
        win.title("Информация о сотрудниках")
        win.minsize(width=600, height=400)
        lab_err = Label(win, font=("Verdana", 14, "bold"), text="Cписок сотрудников пуст", foreground="#FF0000")
        lab1 = Label(win, font=("Verdana", 20, "bold"), text="Текущие сотрудники:", foreground="#0000FF")
        workers_list = []
        if not workers:
            lab_err.pack()
        else:
            lab1.pack()
            xt = "Кол-во текущих сотрудников:" + str(len(workers))
            lab_curr = Label(win, text=xt, font=("Verdana", 14, "bold"), foreground="#FF7F50")
            lab_curr.pack()

            for j in range(len(workers)):
                workers_list.append("Сотрудник №" + str(j + 1))

            i_var = IntVar()
            ent = Entry(win, width=60, textvariable=i_var, font=("Verdana", 14, "bold"))

            def caption(evnt):
                i = i_var.get()
                if i > len(workers) or i == 0:
                    l_exc = Label(win, font=("Verdana", 14, "bold"), text="Сотрудника с таким номером нет",
                                  foreground="#FF0000")
                    l_exc.pack()
                else:
                    t = workers_list[i - 1]
                    tx = workers[i - 1]
                    lab_work = Label(win, font=("Verdana", 14, "bold"))
                    lab_list = Label(win, font=("Verdana", 14, "bold"), foreground="#FF7F50")
                    lab_work.configure(text=tx)
                    lab_list.configure(text=t)
                    lab_list.pack()
                    lab_work.pack()

                del evnt

            lab_ent = Label(win, text="Введите номер сотрудника:", font=("Verdana", 14, "bold"), foreground="#FF7F50")
            btn = Button(win, text="Показать сотрудника", font=("Verdana", 10), foreground="#4682B4")
            btn.bind('<Button-1>', caption)
            lab_ent.pack()
            ent.pack()
            btn.pack()
