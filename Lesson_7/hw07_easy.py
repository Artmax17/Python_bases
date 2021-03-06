'''
Задача-1: Реализовать индексацию элементов списка не с нуля, а с 5, т.е. 5, 6, 7
и т.д.
'''

class MyList(list):
    def __getitem__(self, offset):
     print('Изменяется индексация')
     return list.__getitem__(self, offset - 5)


ML = MyList('abcdfegh')
print(ML[5])

'''
Задача-2: Придумать любую структуру данных. Она должна содержать два атрибута.
Значение одного атрибута передается в конструктор, а значение другого - определяетсяъ
прямо в конструкторе класса. Для этой структуры данных написать метод,
который должен выполнять какой-то функционал. Создать экземпляр класса, передать
данные. Вызывать метод. Проверить, что находится в переменной-экземпляре класса.
Переопределить метод __str__. Этот метод должен возвращать тот результат,
который вы захотите. Проверить еще раз. В комментарии написать, в чем разница
между подходом с использованием метода __str__ и без него.
'''
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return self.name + ' ' + self.surname

    @staticmethod
    def change_class(class_num):
        return {"Перевод в следующий класс": int(class_num) + 1}

# Формируем удобное отображение объекта при выводе функцией print()
    def __str__(self):
        return "Имя ученика: {}, Фамилия: {})".format(self.name, self.surname)

Pupil = Person("Иван", "Сидоров")
print(Pupil.get_full_name())
print(Pupil)

'''
Задача-3: Продолжить работу над задачей 2. Добавить еще один метод. Он должен
вывзваться из экземпляра класса. В этот метод нужно передать некое значение.
Сам метод должен ловить значение и что-то с ним делать и возвращать результат.
Реализовать для этого метода декоратор @staticmethod
'''
print(Pupil.change_class("5"))