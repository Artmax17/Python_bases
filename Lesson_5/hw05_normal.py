# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
# ИСПОЛЬЗОВАТЬ МОДУЛЬ OS и SHUTIL

import os
import sys
import hw05_easy

user_choice = 'b'
while user_choice != '0':
    print('Press 1 for change directory')
    print('Press 2 for explore current directory')
    print('Press 3 for remove directory')
    print('Press 4 for create directory')
    print('Press q for q1uit')
    user_choice = input()
    print(user_choice)

    if user_choice == 'q':
        print('Quit is succesful')
        break

    elif user_choice == '1':
        user_dir = input('Наберите полный путь папки:')
        hw05_easy.change_dir(user_dir)

    elif user_choice == '2':
        dir_name = os.getcwd()
        hw05_easy.list_dir(dir_name)

    elif user_choice == '3':
        dir_name = input('Наберите полный путь папки: ')
        hw05_easy.rmv_dir(dir_name)

    elif user_choice == '4':
        dir_name = input('Наберите полный путь папки: ')
        hw05_easy.make_dir(dir_name)