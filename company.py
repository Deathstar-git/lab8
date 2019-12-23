from tkinter.messagebox import *
from tkinter import *
import work
import worker


class Company:
    _name = ''
    _POSITIONS = ['почасовой рабочий', 'наемный рабочий', 'наёмный рабочий', 'менеджер', 'руководитель']

    def __init__(self, root, name='', workers=None):
        if workers is None:
            workers = []
        self._name = name
        self._workers = workers
        self.rt = root

    @property
    def name(self):
        return self._name

    @property
    def workers(self):
        return self._workers

    def command_1(self, workers, rt):
        win = Toplevel(rt, relief=SUNKEN, bd=10, bg="lightblue")
        win.title("Добавление сотрудника")
        win.minsize(width=400, height=200)
        ent = Entry(rt, width=100)
        ent.pack()
        name_1 = input('Как вас зовут? ')
        position = input('Какую должность будете занимать? ')
        if not position.lower() in self._POSITIONS:
            print('Нет такой должности.')

        if position.lower() == 'наемный рабочий' or position.lower() == 'наёмный рабочий':
            amount = worker.Wageworker.amount
            duration = work.Wagework.duration
            self.hire(name_1, position, amount, duration, workers)
        elif position.lower() == 'почасовой рабочий':
            amount = worker.Hourlyworker.amount
            duration = work.Hourlywork.duration
            self.hire(name_1, position, amount, duration, workers)
        elif position.lower() == 'менеджер':
            amount = worker.Manager.amount
            duration = work.ManagerWork.duration
            self.hire(name_1, position, amount, duration, workers)
        elif position.lower() == 'руководитель':
            amount = worker.Supervisor.amount
            duration = work.SupervisorWork.duration
            self.hire(name_1, position, amount, duration, workers)

    @staticmethod
    def command_2(workers):
        work.CurrentWork.unification(workers)

    @staticmethod
    def command_3():
        amnt = worker.Hourlyworker.amount
        worker.Hourlyworker.hourly_pay(amnt)

    def hire(self, name, position, amount, duration, workers):
        print(f'Добро пожаловать в нашу компанию, {name}.')
        self.add_worker(name, position, amount, duration, workers)

    def add_worker(self, name, position, amount, duration, workers):
        if position.lower() == 'наемный рабочий' or position.lower() == 'наёмный рабочий':
            self._workers.append(worker.Wageworker(name, self.name))
        elif position.lower() == 'почасовой рабочий':
            self._workers.append(worker.Hourlyworker(name, self.name))
        elif position.lower() == 'менеджер':
            self._workers.append(worker.Manager(name, self.name))
        elif position.lower() == 'руководитель':
            self._workers.append(worker.Supervisor(name, self.name))
        self.show_info(name, position, amount, duration, workers)

    @staticmethod
    def show_info(name, position, amount, duration, workers):
        print(f"Добавлен новый рабочий:{name}.")
        print(f"Должность:{position}")
        if position.lower() == 'почасовой рабочий':
            print(f"Почасовая оплата:{amount} руб/ч")
        else:
            print(f"Зарплата:{amount}р.")
        print(f'Деятельность:{duration}')
        print("Все работники:")
        for i in range(len(workers)):
            print(str(workers[i]))

    def exit_(self, event):
        if askyesno("Выход", "Вы уверены?"):
            self.rt.destroy()
            del event
