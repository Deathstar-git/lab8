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
            for j in range(len(workers)):
                workers_list.append("Сотрудник №" + str(j+1))
                t = workers_list[-1]
                lab_list = Label(win, font=("Verdana", 14, "bold"))
                lab_list.configure(text=t)
                lab_list.pack()
