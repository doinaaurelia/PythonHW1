# Напишите программу, которая принимает 
# на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# real = input()
# sum = 0

# for element in real:
#     if element.isnumeric(): #проверяем, если элемент является числом
#         sum += int(element) #преобразовываем каждый элемент в integer, иначе выдает ошибку

# print(sum)
    



########################################################################
########################################################################
# Напишите программу, которая принимает на 
# вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# num = int(input())
# x = 1 #все числа до num
# list = [] #создаем пустой список
# lastResult = 1 #каждый раз обновляем произведение нового числа

# while x <= num: 
#     lastResult *= x 
#     list.append(lastResult) #добавляем в список новое произведение
#     x += 1 

# print(list)





########################################################################
########################################################################
# 3.Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.




########################################################################
########################################################################
# 4. (ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ) 
# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов на 
# указанных позициях. Позиции хранятся в файле file.txt в 
# одной строке одно число.

########################################################################
########################################################################
# 5. Реализуйте алгоритм перемешивания списка.




from random import randint


list = [5, 7, 2, 4, 9]
newList = []

while len(list):
    ind = randint(0, len(list) - 1)
    newList.append(list[ind])
    list.pop(ind)

print(newList)