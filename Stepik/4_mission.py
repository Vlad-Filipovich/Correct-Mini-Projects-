# Шифр Цезаря
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
print('Enter Process Variant (encrypt = "e" or decipher = "d":')
var = input()
print('Enter language ("rus" or "eng"):')
lang = input()
print('Enter shift step:')
step = int(input())
print('Enter start string:')
start_str = [i for i in input()]


def encrypt():  # зашифровать
    if lang == 'rus':
        for i in range(len(start_str)):
            if start_str[i] in rus_upper_alphabet:
                start_str[i] = rus_upper_alphabet[(rus_upper_alphabet.index(start_str[i]) + step) % 32]
            if start_str[i] in rus_lower_alphabet:
                start_str[i] = rus_lower_alphabet[(rus_lower_alphabet.index(start_str[i]) + step) % 32]
        print(''.join(start_str))
    if lang == 'eng':
        for i in range(len(start_str)):
            if start_str[i] in eng_upper_alphabet:
                start_str[i] = eng_upper_alphabet[(eng_upper_alphabet.index(start_str[i]) + step) % 26]
            if start_str[i] in eng_lower_alphabet:
                start_str[i] = eng_lower_alphabet[(eng_lower_alphabet.index(start_str[i]) + step) % 26]
        print(''.join(start_str))


def decipher():  # расшифровать
    if lang == 'rus':
        for i in range(len(start_str)):
            if start_str[i] in rus_upper_alphabet:
                start_str[i] = rus_upper_alphabet[(rus_upper_alphabet.index(start_str[i]) - step) % 32]
            if start_str[i] in rus_lower_alphabet:
                start_str[i] = rus_lower_alphabet[(rus_lower_alphabet.index(start_str[i]) - step) % 32]
        print(''.join(start_str))
    if lang == 'eng':
        for i in range(len(start_str)):
            if start_str[i] in eng_upper_alphabet:
                start_str[i] = eng_upper_alphabet[(eng_upper_alphabet.index(start_str[i]) - step) % 26]
            if start_str[i] in eng_lower_alphabet:
                start_str[i] = eng_lower_alphabet[(eng_lower_alphabet.index(start_str[i]) - step) % 26]
        print(''.join(start_str))
if var == 'e':
    encrypt()
if var == 'd':
    decipher()