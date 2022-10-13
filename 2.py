# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
print('\nПрограмма для игры с конфетами. \n\n"Человек против человека". Условие задачи: \nна столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга. \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход. \nСколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?')
n = 2021
m = 28
players = ['Первый игрок', 'Второй игрок']

def play_game(n, m, players):
    first = random.randint(0, 1)
    move = int(input(f'\nПервый ход определён жеребьёвкой, начинает игрок № {first + 1}. \n{players[first]}: '))
    count = 1
    while n > 0:
        move = int(input(f'{players[count%2 -1]}: '))
        while move > n or move > m:
            move = int(input(f'Неверный ход, можно взять не более {m}, сейчас осталось {n}. Попробуйте ещё раз: '))
        n = n - move
        if n > 0: print(f'Осталось конфет: {n}')
        else: print('Конфеты закончились.')
        count +=1
    return players[not count%2]

winer = play_game(n, m, players)

if not winer:
    print('Нет победителя.')
else: print(f'Победил: {winer}! Ему достаются все конфеты!')

###############################################################################

print('\n\na) "Человек против бота". ')

players = ['Человек', 'Бот']

def play_game(n, m, players):
    first = random.randint(0, 1)
    if first == 0:
        move = int(input(f'\nПервый ход определён жеребьёвкой, начинает {players[first]}. \n{players[first]}: '))
    else:
        move = random.randint(1, 28)
    count = 1
    while n > 0:
        if count%2 == 0:
            move = int(input(f'{players[count%2]}: '))
            while move > n or move > m:
                print(f'Неверный ход, можно взять не более {m}, сейчас осталось {n}')
                move = int(input(f'Попробуйте ещё раз: '))
        else:
            move = random.randint(1, 28)
        n = n - move
        if n > 0: print(f'Осталось конфет: {n}')
        else: print('Конфеты закончились.')
        count +=1
    return players[not count%2]

winer = play_game(n, m, players)

if not winer:
    print('Нет победителя.')
else: print(f'Победил: {winer}! Ему достаются все конфеты!')

###############################################################################

print('\n\nb) "Человек против бота с интеллектом". ')

players = ['Человек', 'Бот']

def play_game(n, m, players):
    first = random.randint(0, 1)
    print(f'\nПервый ход определён жеребьёвкой, начинает {players[first]}. \n{players[first]}: ')
    if first == 1:
        move = 20
    move = (input(f'{players[0]}: '))
    while move > n or move > m:
        print(f'Неверный ход, можно взять не более {m}, сейчас осталось {n}')
        move = int(input(f'Попробуйте ещё раз: '))
    if first == 0: 
        move = 20
    count = 1 
    while n > 0:
        if count == 0:
            
        if count%2 == 0:
            move = int(input(f'{players[count%2]}: '))
            while move > n or move > m:
                print(f'Неверный ход, можно взять не более {m}, сейчас осталось {n}')
                move = int(input(f'Попробуйте ещё раз: '))
        else:
            move = random.randint(1, 280)
        n = n - move
        if n > 0: print(f'Осталось конфет: {n}')
        else: print('Конфеты закончились.')
        count +=1
    return players[not count%2]

winer = play_game(n, m, players)

if not winer:
    print('Нет победителя.')
else: print(f'Победил: {winer}! Ему достаются все конфеты!')