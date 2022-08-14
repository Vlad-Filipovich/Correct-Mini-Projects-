eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = []
num = int(input())
system = int(input())
while num >= system:
    ostatok = num % system
    if ostatok > 9:
        answer.append(eng_upper_alphabet[ostatok - 10])
        num //= system
    else:
        answer.append(str(ostatok))
        num //= system
answer.append(str(num))
print(''.join(answer[::-1]))