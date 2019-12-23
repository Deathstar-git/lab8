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
                self.hire(name_1, position, amount, duration)
                lab_info.pack()
            elif position.lower() == 'почасовой рабочий':
                amount = worker.Hourlyworker.amount
                duration = work.Hourlywork.duration
                self.hire(name_1, position, amount, duration)
                lab_info.pack()
            elif position.lower() == 'менеджер':
                amount = worker.Manager.amount
                duration = work.ManagerWork.duration
                self.hire(name_1, position, amount, duration)
                lab_info.pack()
            elif position.lower() == 'руководитель':
                amount = worker.Supervisor.amount
                duration = work.SupervisorWork.duration
                self.hire(name_1, position, amount, duration)
                lab_info.pack()

            del evnt

        def exit_win(evnt):
            if askyesno("Выход", "Вы уверены?"):
                win.destroy()
                del evnt

        name = StringVar()
        pos = StringVar()
        ent = Entry(win, width=60, textvariable=name, font=("Verdana", 14, "bold"))
        ent2 = Entry(win, width=60, textvariable=pos, font=("Verdana", 14, "bold"))
        lab = Label(win, text="Введите имя нового сотрудника:", font=("Verdana", 14, "bold"))
        lab2 = Label(win, text="Введите должность:", font=("Verdana", 14, "bold"))
        lab_info = Label(win, text="Сотрудник добавлен", font=("Verdana", 14, "bold"), foreground="#008000")
        btn = Button(win, text="Добавить сотрудника")
        btn_exit = Button(win, text="Выйти", font=("Verdana", 16, "bold"))
        btn_exit.bind('<Button-1>', exit_win)
        btn.bind('<Button-1>', caption)
        lab.pack()
        ent.pack()
        lab2.pack()
        ent2.pack()
        btn.pack()
        btn_exit.pack()

        del event

    def unification(self, event):
        win2 = Toplevel(self.rt)
        win2.title("Информация о сотрудниках")
        win2.minsize(width=600, height=400)
        lb = Label(win2, font=("Verdana", 14, "bold"))
        for i in range(len(self.workers)):
            t = self.workers[i].position
            lb.configure(text=t)
        lb.pack()
        del event

    @staticmethod
    def command_3():
        amnt = worker.Hourlyworker.amount
        worker.Hourlyworker.hourly_pay(amnt)

    def hire(self, name, position, amount, duration):
        print(f'Добро пожаловать в нашу компанию, {name}.')
        self.add_worker(name, position, amount, duration)

    def add_worker(self, name, position, amount, duration):
        if position.lower() == 'наемный рабочий' or position.lower() == 'наёмный рабочий':
            self._workers.append(worker.Wageworker(name, self.name))
        elif position.lower() == 'почасовой рабочий':
            self._workers.append(worker.Hourlyworker(name, self.name))
        elif position.lower() == 'менеджер':
            self._workers.append(worker.Manager(name, self.name))
        elif position.lower() == 'руководитель':
            self._workers.append(worker.Supervisor(name, self.name))
        self.show_info(name, position, amount, duration)

    def show_info(self, name, position, amount, duration):
        print(f"Добавлен новый рабочий:{name}.")
        print(f"Должность:{position}")
        if position.lower() == 'почасовой рабочий':
            print(f"Почасовая оплата:{amount} руб/ч")
        else:
            print(f"Зарплата:{amount}р.")
        print(f'Деятельность:{duration}')
        print("Все работники:")
        for i in range(len(self.workers)):
            print(str(self.workers[i]))

    def exit_(self, event):
        if askyesno("Выход", "Вы уверены?"):
            self.rt.destroy()
            del event
