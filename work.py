# from tkinter.messagebox import *
from tkinter import *


class Work:
    _duration = ' '

    def __init__(self, root, workers, duration=''):
        self._duration = duration
        self._workers = workers
        self.rt = root

    @property
    def duration(self):
        return self._duration

    @property
    def workers(self):
        return self._workers

    @duration.setter
    def duration(self, dur):
        self._duration = dur


class Hourlywork(Work):
    duration = "Доставка мелких заказов на дом"

    def __init__(self, duration):
        super().__init__(duration, workers=self.workers)


class Wagework(Work):
    duration = "Водитель транспорта для доставки товаров"

    def __init__(self, duration):
        super().__init__(duration, workers=self.workers)


class ManagerWork(Work):
    duration = "Продажа,ведение документационных дел,работа с персоналом"

    def __init__(self, duration):
        super().__init__(duration, workers=self.workers)


class SupervisorWork(Work):
    duration = "Контроль работы сотрудников - почасовых рабочих, наёмных рабочих, менеджеров "

    def __init__(self, duration):
        super().__init__(duration, workers=self.workers)


class CurrentWork(Work):
    pass
            # else:
            # lab2.pack()
            # btn.pack()
            # for j in range(len(self.workers)):
            #     workers_list.append("Сотрудник №" + str(j+1))
            # lab3.pack()
            # print(workers_list)
            # i = int(input("Введите номер сотрудника:"))
            # if 1 <= i <= len(self.workers):
            #     work = self.workers[i - 1].position
            #     name = self.workers[i - 1].name
            #     print(f'ФИО:{name}')
            #     print(f'Текущая должность:{work}')
            # else:
            #     print("Номер сотрудника не распознан.")

