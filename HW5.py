#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = 'Напишите програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_words(text):
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return " ".join(text)

# text = del_words(text)
# print(text)


##################################################################
##################################################################

#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. П
# ервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


##################################################################
##################################################################

#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
 
with open('decoded.txt', 'r') as data:
    my_text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = encode_rle(my_text)
print(str_code)

with open('encoded.txt', 'r') as data:
    my_text2 = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(my_text2)
print(str_decode)
