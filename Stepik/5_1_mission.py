# Перевод из десятичной системы счисления в двоичную, 8-ую и 16-ую сразу

print('Enter the number:')
num = int(input())
print(bin(num)[2:], oct(num)[2:], hex(num)[2:].upper(), sep='\n')
