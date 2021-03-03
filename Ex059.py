from time import sleep
y = 10
while y == 10:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    x = 10
    while x == 10:

        print(f"""
Seus numeros são {n1} e {n2}.
O que deseja fazer:

[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - maior
[ 4 ] - Novos números
[ 5 ] - Sair do programa
""")
        op = int(input('Digite sua escolha: '))
        if op == 1:
            somar = n1 + n2
            print(f'A soma entre {n1} + {n2} é {somar}')

        elif op == 2:
            mult = n1 * n2
            print(f'A multiplicação entre {n1} x {n2} é {mult}')

        elif op == 3:
            if n1 > n2:
                print(f'{n1} é maior que {n2}')

            else:
                print(f'{n2} é maior que {n1}')

        elif op == 4:
            print('Um momento...')
            x += 1

        elif op == 5:
            print('Finalizando...')
            sleep(2)
            print('Fim do programa! Volte sempre!')
            x += 1
            y += 1
        else:
            print('Opçao invalida. Tente novamente')
            x += 1


        sleep(3)
        print('=-=='*10)
