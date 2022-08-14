# Шифр Цезаря
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
orig_str = input().split()
answer = []
for s in orig_str:
    next_word = [i for i in s]
    len_word = [i for i in s if i.isalpha()]
    for j in range(len(next_word)):
        if next_word[j] in eng_upper_alphabet:
            next_word[j] = eng_upper_alphabet[(eng_upper_alphabet.index(next_word[j]) + len(len_word)) % 26]
        if next_word[j] in eng_lower_alphabet:
            next_word[j] = eng_lower_alphabet[(eng_lower_alphabet.index(next_word[j]) + len(len_word)) % 26]
    str_next_word = ''.join(next_word)
    answer.append(str_next_word)
print(' '.join(answer))
