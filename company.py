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
            if any(map(str.isdigit, name_1)):
                label_exc = Label(win, font=("Verdana", 14, "bold"),
                                  text="Не добавляйте цифру в ФИО!", foreground="#FF0000")
                label_exc.pack()
            else:
                if position.lower() == 'наемный рабочий' or position.lower() == 'наёмный рабочий':
                    self.hire(name_1, position, self.workers)
                    lab_success.pack()
                elif position.lower() == 'почасовой рабочий':
                    self.hire(name_1, position, self.workers)
                    lab_success.pack()
                elif position.lower() == 'менеджер':
                    self.hire(name_1, position, self.workers)
                    lab_success.pack()
                elif position.lower() == 'руководитель':
                    self.hire(name_1, position, self.workers)
                    lab_success.pack()

            del evnt

        name = StringVar()
        pos = StringVar()
        ent = Entry(win, width=60, textvariable=name, font=("Verdana", 14, "bold"))
        ent2 = Entry(win, width=60, textvariable=pos, font=("Verdana", 14, "bold"))
        lab_success = Label(win, text="Сотрудник успешно добавлен", font=("Verdana", 14, "bold"), foreground="#008000")
        lab = Label(win, text="Введите ФИО нового сотрудника:", font=("Verdana", 14, "bold"))
        lab2 = Label(win, text="Введите должность:", font=("Verdana", 14, "bold"))
        t = "(Руководитель,Менеджер,Почасовой рабочий,Наемный рабочий)"
        lab_info = Label(win, text=t, font=("Verdana", 12, "bold"))
        btn = Button(win, text="Добавить сотрудника", font=("Verdana", 10))
        btn.bind('<Button-1>', caption)
        lab.pack()
        ent.pack()
        lab2.pack()
        lab_info.pack()
        ent2.pack()
        btn.pack()
        del event

    def command_3(self, event):
        amnt = worker.Hourlyworker.amount
        win = Toplevel(self.rt)
        win.title("Добавление сотрудника")
        win.minsize(width=600, height=400)

        def caption(evnt):
            h = ent.get()
            if h.isdigit():
                payment = int(amnt) * int(h)
                txt = f'Ваша оплата составит {payment}р.'
                lab_info = Label(win, text=txt, font=("Verdana", 14, "bold"))
                lab_info.pack()
            else:
                lab_err = Label(win, text="Введите корректное кол.во часов", font=("Verdana", 14, "bold"),
                                foreground="#FF0000")
                lab_err.pack()
            del evnt

        h1 = IntVar
        lab = Label(win, text="Сколько часов вы отработали?", font=("Verdana", 14, "bold"))
        lab2 = Label(win, text="Введите кол.во часов:", font=("Verdana", 12, "bold"))
        ent = Entry(win, width=60, textvariable=h1, font=("Verdana", 14, "bold"))
        btn = Button(win, text="Вычислить", font=("Verdana", 10), foreground="#4682B4")
        btn.bind('<Button-1>', caption)
        ent.bind('<Return>', caption)
        lab.pack()
        lab2.pack()
        ent.pack()
        btn.pack()
        del event

    def hire(self, name, position, workers):
        self.add_worker(name, position, workers)

    def add_worker(self, name, position, workers):
        if position.lower() == 'наемный рабочий' or position.lower() == 'наёмный рабочий':
            workers.append(worker.Wageworker(name, self.name))
        elif position.lower() == 'почасовой рабочий':
            workers.append(worker.Hourlyworker(name, self.name))
        elif position.lower() == 'менеджер':
            workers.append(worker.Manager(name, self.name))
        elif position.lower() == 'руководитель':
            workers.append(worker.Supervisor(name, self.name))

    def command_2(self, event):
        work.CurrentWork.unification(self.workers, self.rt)
        del event

    def exit_(self, event):
        if askyesno("Выход", "Вы уверены?"):
            self.rt.destroy()
            del event
