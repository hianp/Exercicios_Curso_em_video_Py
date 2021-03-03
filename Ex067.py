cont = 0
while True:
    cont = 0
    num = int(input('Digite um numero para fazer a tabuada (negativos para finalizar): '))
    print('-' * 20)
    if num < 0:
        print('Programa tabuada ENCERRADO. Volte sempre!')
        break
    while cont < 10:
        cont += 1
        mult = num * cont
        print(f'{num:2}  x {cont:2} = {mult}')
    print('-' * 20)
