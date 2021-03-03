import random
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
cont = 0
contx = 0
while True:
    comp = random.randint(0, 10)
    num = int(input('Diga um valor: '))
    esc = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]

    soma = comp + num
    contx += 1
    if soma % 2 == 0:
        print(f'Você jogou {num} e o computador {comp}. Total de {soma} DEU PAR')
    else:
        print(f'Você jogou {num} e o computador {comp}. Total de {soma} DEU ÍMPAR')
    if soma % 2 == 0 and esc == 'p':
        print('-' * 25)
        print('Você VENCEU')
        print('Vamos jogar novamente...')
        print('-' * 25)
        cont += 1
    elif soma % 2 == 0 and esc == 'i':
        print('-' * 50)
        print('Você perdeu')
        print('-' * 50)
        break
    elif soma % 2 == 1 and esc == 'p':
        print('-' * 50)
        print('Você PERDEU!')
        print('-' * 50)
        break
    elif soma % 2 == 1  and esc == 'i':
        print('-' * 25)
        print('Você VENCEU')
        print('Vamos jogar novamente...')
        print('-' * 25)
        cont += 1
if cont == 0:
    print('GAME OVER! Você não venceu nenhuma vez!')
else:
    print(f'Você jogou {contx} vezes e ganhou {cont}.')
