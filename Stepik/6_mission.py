# Словестная угадайка (виселица)

from random import *

word_list = ['Дерево', 'Вина', 'Копьё', 'Горло', 'Синица', 'Каштан', 'Луноход', 'Рутина', 'Спинка', 'Тяжесть']
def get_word():
    return choice(word_list).upper()
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def play(word):
    word_completion = ['_'] * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    tries = 6
    print(display_hangman(tries))
    print(''.join(word_completion))
    while True:
        print('Введите букву или слово:')
        letter = input().upper()
        if len(letter) == 1:
            if letter in word and letter not in guessed_letters:
                for i in range(len(word)):
                    if word[i] == letter:
                        word_completion[i] = letter
                print('Нихуя себе! Как? Буква есть в слове!')
                print(''.join(word_completion))
                if ''.join(word_completion) == word:
                    print('С победой даун!')
                    break
            if letter in guessed_letters:
                print('Было, было!')
            else:
                tries -= 1
                print(display_hangman(tries))
                print(''.join(word_completion))
                print('Такой буквы нет, ха-ха-ха ВИСЕЛИЦА!!!')
            guessed_letters.append(letter)
        else:
            guessed_words.append(letter)
            if letter == word:
                print('Ты чё ебанутый(ая)! Поздравляю!')
                break
            else:
                tries -= 1
                print(display_hangman(tries))
                print(''.join(word_completion))
                print('А вот и хуй! ахахаха')
play(get_word())