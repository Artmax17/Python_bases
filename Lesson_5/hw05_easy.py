# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.

import os

x = 1
while x <= 9:
    dir_path = os.path.join(os.getcwd(), 'dir_' + str(x))
    print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print ('Такая директория уже существует')
    x += 1

# И второй скрипт, удаляющий эти папки.

x = 1
while x <= 9:
    dir_path = os.path.join(os.getcwd(), 'dir_' + str(x))
    print(dir_path)
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print ('Такая директория отсутствует')
    x += 1

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

files = os.listdir(path = os.getcwd())
print(files)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

import os

dir_path = os.path.abspath('hw05_easy')
if not os.path.exists(dir_path):
    os.system('copy %s %s' % (__file__, dir_path))