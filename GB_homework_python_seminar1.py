'''
Задача 1.
Напишите программу, которая принимает на вход цифру, обозначающую 
день недели, и проверяет, является ли этот день выходным.

Пример:
6 -> да
7 -> да
1 -> нет
'''
'''
print("Является ли день недели выходным")
number_day_week = int(input("Введите номер дня недели: "))

if 0 < number_day_week < 6:
    print("нет")
elif 5 < number_day_week < 8:
    print("да")
else:
    print("Вы ввели неверный номер дня недели")
'''

'''
Задача 2.
Напишите программу, которая принимает на вход координаты точки (X и Y), 
и выдаёт номер четверти плоскости, в которой находится эта точка 
(или на какой оси она находится).

Пример:

x=34; y=-30 -> 4
x=2; y=4-> 1
x=-34; y=-30 -> 3
'''

'''
print("Найдём в какой четверти координатной плоскости находится ночка")
x = int(input("Введите координаты точки по оси x: "))
y = int(input("Введите координаты точки по оси y: "))

if x == 0 or y == 0:
    if x != 0:
        print("Точка находится на оси x")
    elif y != 0:
        print("Точка находится на оси y")
    else:
        print("Точка находится в центре координатной плоскости")
elif x > 0:
    if y > 0:
        print("1")
    else:
        print("4")
elif x < 0:
    if y > 0:
        print("2")
    else:
        print("3")
else:
    print("Error")
'''

'''
Задача 3.
Напишите программу, которая по заданному номеру четверти, показывает 
диапазон возможных координат точек в этой четверти (x и y).
'''

'''
print("Найдём диапозон координат в нужной четверти")
number = int(input("Введине номер четверти: "))

if number == 1:
    print("Все значения x и y от 0 до бесконечности прложительные")
elif number == 2:
    print("Все значения y от 0 до бесконечности прложительные\n"
          "Все значения x от 0 до бесконечности отрецательные")
elif number == 3:
    print("Все значения x и y от 0 до бесконечности отрецательные")
elif number == 4:
    print("Все значения x от 0 до бесконечности положительные\n"
          "Все значения y от 0 до бесконечности отрецательные")
else:
    print("Вы ввели неверный номер четверти")
'''

'''
Задача 4.
Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.

Пример:

A (3,6); B (2,1) -> 5,09
A (7,-5); B (1,-1) -> 7,21
'''

import math
print("Найдём растояние между двумя точками в 2D пространстве")
xa = int(input("Введите х точки А: "))
ya = int(input("Введите y точки А: "))
xb = int(input("Введите х точки B: "))
yb = int(input("Введите y точки B: "))

'''
Формулы вычисления расстояния между двумя точками:
AB = √(xb - xa)**2 + (yb - ya)**2
'''
result_ab = math.sqrt((xb - xa)**2 + (yb - ya)**2)
print(round(result_ab, 3))
