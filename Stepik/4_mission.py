# Шифр Цезаря
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
print('Enter Process Variant (encrypt = "e" or decipher = "d":')
var = input()
while not var == 'e' and not var == 'd':
    print('Something is wrong, you did not meet the input conditions. Try again:')
    print('Enter Process Variant (encrypt = "e" or decipher = "d":')
    var = input()
print('Enter language ("rus" or "eng"):')
lang = input()
while not lang == 'eng' and not lang == 'rus':
    print('Something is wrong, you did not meet the input conditions. Try again:')
    print('Enter language ("rus" or "eng"):')
    lang = input()
print('Enter shift step:')
step = input()
while not step.isdigit():
    print('Something is wrong, you did not meet the input conditions. Try again:')
    print('Enter shift step:')
    step = input()
print('Enter start string:')
start_str = input()
while start_str.isdigit():
    print("So far I can't work with numbers. Try again:")
    print('Enter start string:')
    start_str = input()
start_str = [i for i in start_str]

def encrypt():  # зашифровать
    if lang == 'rus':
        for i in range(len(start_str)):
            if start_str[i] in rus_upper_alphabet:
                start_str[i] = rus_upper_alphabet[(rus_upper_alphabet.index(start_str[i]) + int(step)) % 32]
            if start_str[i] in rus_lower_alphabet:
                start_str[i] = rus_lower_alphabet[(rus_lower_alphabet.index(start_str[i]) + int(step)) % 32]
        print(''.join(start_str))
    if lang == 'eng':
        for i in range(len(start_str)):
            if start_str[i] in eng_upper_alphabet:
                start_str[i] = eng_upper_alphabet[(eng_upper_alphabet.index(start_str[i]) + int(step)) % 26]
            if start_str[i] in eng_lower_alphabet:
                start_str[i] = eng_lower_alphabet[(eng_lower_alphabet.index(start_str[i]) + int(step)) % 26]
        print(''.join(start_str))


def decipher():  # расшифровать
    if lang == 'rus':
        for i in range(len(start_str)):
            if start_str[i] in rus_upper_alphabet:
                start_str[i] = rus_upper_alphabet[(rus_upper_alphabet.index(start_str[i]) - int(step)) % 32]
            if start_str[i] in rus_lower_alphabet:
                start_str[i] = rus_lower_alphabet[(rus_lower_alphabet.index(start_str[i]) - int(step)) % 32]
        print(''.join(start_str))
    if lang == 'eng':
        for i in range(len(start_str)):
            if start_str[i] in eng_upper_alphabet:
                start_str[i] = eng_upper_alphabet[(eng_upper_alphabet.index(start_str[i]) - int(step)) % 26]
            if start_str[i] in eng_lower_alphabet:
                start_str[i] = eng_lower_alphabet[(eng_lower_alphabet.index(start_str[i]) - int(step)) % 26]
        print(''.join(start_str))
if var == 'e':
    encrypt()
if var == 'd':
    decipher()