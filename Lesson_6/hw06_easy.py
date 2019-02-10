'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).
Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.
На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
Применить к экземпляру
класса метод __dict__ и проверить какой будет результат применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''
class Worker:
    def __init__(self, name, surname, position, salary, bonus):
       self.name = name
       self.surname = surname
       self.position = position
       self._income = {'salary': salary, 'bonus': bonus}

worker1 = Worker("Андрей", "Сергеев", "Менеджер", 40000, 10000)
print(worker1.__dict__)
# Словарь  Пары название-значение всех атрибутов

'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
class Worker:
    def __init__(self, name, surname, position, salary, bonus):
       self.name = name
       self.surname = surname
       self.position = position
       self._income = {'salary': salary, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, salary, bonus, percent):
        Worker.__init__(self, name, surname, position, salary, bonus)
        self.percent = percent

    @property
    def middle_salary_calc(self):
        middle_salary = (self._income["salary"]*self.percent)/100 + self._income["salary"]
        return middle_salary

position1 = Position("Андрей", "Сергеев", "Менеджер", 40000, 1000, 15)
print(position1.middle_salary_calc)

'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
class Worker:
    def __init__(self, name, surname, position, salary, bonus):
       self.name = name
       self.surname = surname
       self.position = position
       self._income = {'salary': salary, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, salary, bonus, percent):
        Worker.__init__(self, name, surname, position, salary, bonus)
        self.percent = percent
        self.middle_salary = 0
        self.bonus = bonus

    @property
    def middle_salary_calc(self):
        self.middle_salary = (self._income["salary"]*self.percent)/100 + self._income["salary"]

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_full_salary(self):
        full_salary = self.middle_salary + self.bonus
        return full_salary

position1 = Position("Андрей", "Сергеев", "Менеджер", 40000, 1000, 15)
print(position1.middle_salary_calc)
print(position1.get_full_salary())
