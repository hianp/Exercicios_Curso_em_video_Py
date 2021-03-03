n1 = float(input('Digite o lado 1 do triangulo: '))
n2 = float(input('Digite o lado 2 do triangulo: '))
n3 = float(input('Digite o lado 3 do triangulo: '))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('Os segmentos a cima podem formar um triangulo')
else:
    print('Não é possivel formar um triangulo')
