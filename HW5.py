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

import random

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
    'Основные правила игры: '
    'Нам будет дано некоторое количество конфет, '
    'за один ход мы можем взять не более определённого количества, '
    'о котором мы с вами договоримся.'
    'Итак, начнём!')
            

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def play_game(n, m, players, messages):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'а'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(greeting)

player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
players = [player1, player2]

n = int(input('Сколько конфет будем разыгрывать?\n '))
m = int(input('Сколько максимально будем брать конфет за один ход?\n '))

winer = play_game(n, m, players, messages)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


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
