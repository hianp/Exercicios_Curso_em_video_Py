from random import randint

"""
tupla = tuple(range(randint(0, 11)))
n1 = n2 = n3 = n4 = n5 = randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11)
t = list(str(n1))
t1 = ''.join(t)
print(f"Os valores sorteados foram: {t1}")
print(t)
print(n1)


"""
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
