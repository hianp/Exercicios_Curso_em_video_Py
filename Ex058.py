import random

num = random.randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
x = int(input('Advinhe o numero do computador: '))
tent = 0
while x != num:
    if x < num:
        print('ERROU')
        print('Mais...')
    else:
        print('ERROU')
        print('Menos...')
    tent += 1

    x = int(input('Digite novamente: '))

print(f'Você tentou {tent + 1} vezes até acertar.')

"""if x == num:
    print('Você venceu!')
else:
    print(f'Você perdeu, era {num}')
"""