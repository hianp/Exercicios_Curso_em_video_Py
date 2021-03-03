print('Digite 3 numeros inteiros diferentes!')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))

if n1 > n2 and n1 > n3:
    print(f'O maior numero é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior numero é {n2}')
else:
    print(f'O maior numero é {n3}')

if n1 < n2 and n1 < n3:
    print(f'O menor valor é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor valor é {n2}')
else:
    print(f'O maior numero é {n3}')
