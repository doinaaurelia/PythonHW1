# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является 
# ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input(" Введитецифру, обозначающую день недели: "))
# if day <= 5 or day > 7:
#     print("нет")
# elif day == 6 or day == 7:
#     print("да")

########################################################################
########################################################################


# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#не знаю

########################################################################
########################################################################



# Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти 
# плоскости, в которой находится эта точка (или на какой оси 
# она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

# x = int(input("Введите точку x "))
# if x == 0:
#     print("try again")
# y = int(input("Введите точку y "))
# if y == 0:
#     print("try again")

# if x > 0 and y > 0:
#     print("1")
# elif y > 0 and x < 0:
#     print("2")
# elif x < 0 and y < 0:
#     print("3")
# elif x > 0 and y < 0:
#     print("4")


########################################################################
########################################################################


# Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).

# quadrant = int(input("Введите номер четверти "))
# if quadrant > 4 or quadrant < 1:
#     print("try again")

# if quadrant == 1:
#     print("x > 0, y > 0")
# elif quadrant == 2:
#     print("x < 0, y > 0")
# elif quadrant == 3:
#     print("x < 0, y < 0")
# elif quadrant == 4:
#     print("x > 0, y < 0")



########################################################################
########################################################################

# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
co1 = input("Введите точки координат x ")
co2 = input("Введите точку координат y ")
co1 = co1.split(",")
co2 = co2.split(",")
if co1 and co2 == 0:
    print("try again")

distance = math.sqrt(((int(co1[0])-int(co2[0]))**2)+((int(co1[1])-int(co2[1]))**2))
print(distance)