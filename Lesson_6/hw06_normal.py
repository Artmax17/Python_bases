'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''

import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        # находим длины сторон по формулам
        #|AB|=(xB−xA)2+(yB−yA)2−−−√,|AC|=(xC−xA)2+(yC−yA)2−−−√,|BC|=(xC−xB)2+(yC−yB)2
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    # периметр - сумма длин сторон
    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return (self.perimetr)
    # площадь - по формуле Герона
    # Когда известны длины всех сторон, для нахождения площади используйте формулу Герона.
    # Найдите половину периметра треугольника, затем произведение полупериметра на его разность
    # с каждой из сторон p•(p-a)•(p-b)•(p-c). Из полученного числа извлеките квадратный корень.
    def ploshad(self):
        self.perimetr /=2
        self.ploshad =  round(math.sqrt(self.perimetr*(self.perimetr - self.AB)*(self.perimetr - self.BC)* (self.perimetr - self.CA)),2)
        return (self.ploshad)

    # высота - (2*площадь)/основание
    def vysota(self):
        self.ploshad *=2
        self.vysota =  round((self.ploshad / self.CA),2)
        return (self.vysota)

my_tri = Triangle(2,2,5,8,7,4)


print('Длинна строны АВ = {}, ВС = {}, СА = {}'.format(my_tri.AB, my_tri.BC,my_tri.CA))
print('Периметр треугольника АВС равен {}'.format(my_tri.perimetr()))
print('Площадь треугольника АВС равна {}'.format(my_tri.ploshad()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(my_tri.vysota()))