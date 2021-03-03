n1 = float(input('Digite o lado 1 do triangulo: '))
n2 = float(input('Digite o lado 2 do triangulo: '))
n3 = float(input('Digite o lado 3 do triangulo: '))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    if n1 == n2 == n3:
        print('Os segmentos a cima podem formar um triangulo equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Os segmentos a cima podem formar um triangulo Isósceles')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('Os segmentos a cima podem formar um triangulo Escaleno')
elif n1 == n2 and n1 == n3:
    print('Equilatero')


else:
    print('Não é possivel formar um triangulo')






