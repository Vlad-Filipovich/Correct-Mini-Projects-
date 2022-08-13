# Шифр Цезаря
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]
keys = int(input())
orig_str = [i for i in input()]

for i in range(len(orig_str)):
    if orig_str[i] in rus_upper_alphabet:
        orig_str[i] = rus_upper_alphabet[(rus_upper_alphabet.index(orig_str[i]) + keys) % 32]
    if orig_str[i] in rus_lower_alphabet:
        orig_str[i] = rus_lower_alphabet[(rus_lower_alphabet.index(orig_str[i]) + keys) % 32]
print(''.join(orig_str))

for i in range(len(orig_str)):
    if orig_str[i] in eng_upper_alphabet:
        orig_str[i] = eng_upper_alphabet[(eng_upper_alphabet.index(orig_str[i]) + keys) % 26]
    if orig_str[i] in eng_lower_alphabet:
        orig_str[i] = eng_lower_alphabet[(eng_lower_alphabet.index(orig_str[i]) + keys) % 26]
print(''.join(orig_str))