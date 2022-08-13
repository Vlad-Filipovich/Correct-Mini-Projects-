# Secure Password Generator
from random import *

print('\n', 'Welcome to the "Secure Password Generator bot."', sep='')
print('Here you can generate the password you need.', '\n')
print("Let's start")
print('\n', 'Please only answer "Yes" or "No" to the questions.', '\n', sep='')
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_characters = 'il1Lo0O'
all_symb = [digits] + [lowercase_letters] + [uppercase_letters] + [punctuation]
password = []


def generate_password():
    chars = []
    while True:
        print("Enter the number of passwords to generate:")
        amount_pass = input()
        if not amount_pass.isdigit():
            print('Please enter a number.')
            continue
        else:
            break
    while True:
        print("Enter the length of one password:")
        len_pass = input()
        if not amount_pass.isdigit():
            print('Please enter a number.')
            continue
        else:
            break
    quest_1 = "Should numbers be included?"
    quest_2 = "Should capital letters be included?"
    quest_3 = "Should lowercase letters be included?"
    quest_4 = "Should symbols be included?"
    quest_5 = "Should ambiguous characters be excluded?"
    questions = [quest_1] + [quest_2] + [quest_3] + [quest_4] + [quest_5]
    for i in range(4):
        print(questions[i])
        answer = input()
        if answer.lower() == 'yes':
            chars += all_symb[i]
        else:
            continue
    print(questions[4])
    answer_5 = input()
    if answer_5 == 'yes':
        chars = ''.join([i for i in chars if i not in ambiguous_characters])
    else:
        chars = ''.join([i for i in chars])
    for _ in range(int(amount_pass)):
        for _ in range(int(len_pass)):
            password.append(choice(chars))
        print(''.join(password))
        password.clear()


generate_password()