from tkinter.messagebox import *
from tkinter import *
import work
import worker


class Company:
    _name = ''
    _POSITIONS = ['почасовой рабочий', 'наемный рабочий', 'наёмный рабочий', 'менеджер', 'руководитель']

    def __init__(self, root, workers=[], name=''):
        self._name = name
        self.rt = root
        self.workers = workers

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self.workers[i] for i in range(*index.indices(len(self.workers)))]
        elif isinstance(index, int):
            if index < 0:
                index += len(self.workers)
            if index < 0 or index >= len(self.workers):
                raise IndexError(f"Индекса {index} не существует.")
            return self.workers[index]
        else:
            raise TypeError("Неправильный тип аргумента.")

    @property
    def name(self):
        return self._name

    def command_1(self, event):
        win = Toplevel(self.rt)
        win.title("Добавление сотрудника")
        win.minsize(width=600, height=400)

        def caption(evnt):
            name_1 = name.get()
            position = pos.get()
            if not position.lower() in self._POSITIONS and not position == '':
                lab_no = Label(win, font=("Verdana", 14, "bold"), text="Нет такой должности", foreground="#FF0000")
                lab_no.pack()

            if position.lower() == 'наемный рабочий' or position.lower() == 'наёмный рабочий':
                amount = worker.Wageworker.amount
                duration = work.Wagework.duration
                self.hire(name_1, position, amount, duration, self.workers)
                lab_success.pack()
            elif position.lower() == 'почасовой рабочий':
                amount = worker.Hourlyworker.amount
                duration = work.Hourlywork.duration
                self.hire(name_1, position, amount, duration, self.workers)
                lab_success.pack()
            elif position.lower() == 'менеджер':
                amount = worker.Manager.amount
                duration = work.ManagerWork.duration
                self.hire(name_1, position, amount, duration, self.workers)
                lab_success.pack()
            elif position.lower() == 'руководитель':
                amount = worker.Supervisor.amount
                duration = work.SupervisorWork.duration
                self.hire(name_1, position, amount, duration, self.workers)
                lab_success.pack()

            del evnt

        name = StringVar()
        pos = StringVar()
        ent = Entry(win, width=60, textvariable=name, font=("Verdana", 14, "bold"))
        ent2 = Entry(win, width=60, textvariable=pos, font=("Verdana", 14, "bold"))
        lab_success = Label(win, text="Сотрудник успешно добавлен", font=("Verdana", 14, "bold"), foreground="#008000")
        lab = Label(win, text="Введите имя нового сотрудника:", font=("Verdana", 14, "bold"))
        lab2 = Label(win, text="Введите должность:", font=("Verdana", 14, "bold"))
        btn = Button(win, text="Добавить сотрудника")
        btn.bind('<Button-1>', caption)
        lab.pack()
        ent.pack()
        lab2.pack()
        ent2.pack()
        btn.pack()
        del event

    @staticmethod
    def command_3():
        amnt = worker.Hourlyworker.amount
        worker.Hourlyworker.hourly_pay(amnt)

    def hire(self, name, position, amount, duration, workers):
        print(f'Добро пожаловать в нашу компанию, {name}.')
        self.add_worker(name, position, amount, duration, workers)

    def add_worker(self, name, position, amount, duration, workers):
        if position.lower() == 'наемный рабочий' or position.lower() == 'наёмный рабочий':
            workers.append(worker.Wageworker(name, self.name))
        elif position.lower() == 'почасовой рабочий':
            workers.append(worker.Hourlyworker(name, self.name))
        elif position.lower() == 'менеджер':
            workers.append(worker.Manager(name, self.name))
        elif position.lower() == 'руководитель':
            workers.append(worker.Supervisor(name, self.name))
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

    def command_2(self, event):
        print(self.workers)
        work.CurrentWork.unification(self.workers, self.rt)
        del event

    def exit_(self, event):
        if askyesno("Выход", "Вы уверены?"):
            self.rt.destroy()
            del event
