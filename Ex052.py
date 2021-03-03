"""
Minha resposta:

num = int(input('Digite um número: '))

if num == 3 or num == 1:
    print('Primo')

elif num % 2 != 0 and num % 3 != 0:
    print('Primo')
else:
    print('Não é primo')
"""

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[32m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele NÃO é primo')
