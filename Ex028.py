import random

x = int(input('Advinhe o numero do computador: '))
num = random.randint(0, 5)

if x == num:
    print('Você venceu!')
else:
    print(f'Você perdeu, era {num}')
