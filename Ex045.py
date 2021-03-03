import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 2:
        print('EMPATE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 0:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')

else:
    print('Jogada invalida')
