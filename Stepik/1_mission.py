# 1 Числовая угадайка

from random import randint


def is_valid(number):
    return number.isdigit() and right_border.isdigit() and int(number) in range(1, int(right_border) + 1)


def game():
    print('Введите правую границу диапазона (натуральное число):')
    global right_border
    while True:
        right_border = input()
        if not right_border.isdigit():
            print('Что-то не так! Скорее всего Вы указали не натуральное число, попробуйте ещё раз!')
            continue
        else:
            n = randint(1, int(right_border))
            count = 1
            break
    while True:
        print('Введите число от 1 до', right_border, 'включительно:')
        num = input()
        if not is_valid(num):
            print('Что-то не так!', 'Возможно правая граница указана неверно или число вне диапозона.', sep='\n')
        else:
            num = int(num)
            if num < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                count += 1
                continue
            if num > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
                count += 1
                continue
            else:
                print('Вы угадали, поздравляем! Для этого вам потребовалось', count, 'попытка(ок)')
                break


def repeat_game():
    while True:
        print('Сыграем ещё разок?', 'Ответьте "ДА" или "НЕТ"', sep='\n')
        answer = input()
        if answer.upper() == 'ДА':
            game()
            continue
        if answer.upper() == 'НЕТ':
            break
        else:
            print('Я не понимаю Ваш ответ, ответьте еще раз')
            continue


print('Добро пожаловать в числовую угадайку!', '\n')
game()
repeat_game()