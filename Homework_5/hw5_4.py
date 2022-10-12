# --------------------------------------------------
# 3 Напишите программу, удаляющую из текста все слова, содержащие "абв".
# ---------------------------------------------------

import random
from random import randint, choice
 
print(
    '"Игра с конфетами"\n'
    'В игре участвуют два игрока. Игроки ходят поочереди.\n'
    'За один ход можно забрать не более заранее определенного количества конфет.\n'
    'Тот, кому достанется последняя конфета, выиграл.\n'
    'Удачи!\n')
 
messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
            'сколько конфет берем?', 'берите еще', 'Ваш ход']
max_number_move = 0
 
def introduce_players():
    player1 = input('Первый игрок, представьтесь\n')
    player2 = 'SmartBOT'
    print(f'{player1}, сегодня с Вами играет {player2}')
    return [player1, player2]
 
def sweets_game(players):
    global max_number_move
    total_sweets = int(input('Введите cколько всего у нас конфет:\n'))
    max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [total_sweets, max_number_move, int(first)]
 
max_move = max_number_move
 
def game_player_vs_smart_bot(sweets, players, messages):
    global max_number_move
    count = sweets[2]
 
 
    while sweets[0] > 0:
        if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
            move = sweets[0] -1
            print(f'Я забираю {move}')
 
        elif not count % 2:
            move = random.randint(1, sweets[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(
                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                chance = 2
                while chance > 0:
                    if sweets[0] >= move <= sweets[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]
 
 
players = introduce_players()
sweets = sweets_game(players)
 
winer = game_player_vs_smart_bot(sweets, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Последнюю конфету забирает {winer}! А значит ему достаются все конфеты!')

