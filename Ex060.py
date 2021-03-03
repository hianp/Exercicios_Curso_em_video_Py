num = int(input('Digite um numero: '))
c = num
f = 1
print(f'Calculando {num}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')


print('UTILIZANDO FOR')
"""for cont in range(num, 0, -1):
    print(f'{cont}', end='')
    print(' x ' if i > 1 else ' = ', end='')

print(f'{cont}')"""
f1 = 1
for cont in range(num, 0, -1):
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f1 *= cont
print(f'{f}')

