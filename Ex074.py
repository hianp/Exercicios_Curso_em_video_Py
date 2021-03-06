from random import randint

n1 = randint(0, 11)
n2 = randint(0, 11)
n3 = randint(0, 11)
n4 = randint(0, 11)
n5 = randint(0, 11)

num = n1, n2, n3, n4, n5
print(f'Os valores sorteados foram: {n1}, {n2}, {n3}, {n4}, {n5}')
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
print(type(num))


#  Outra forma de fazer
print("=-"*25)


numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print("Os numeros sorteador foram: ", end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
print(type(numeros))
