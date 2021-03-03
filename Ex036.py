v = float(input('Qual o valor da casa: R$'))
s = float(input('Qual seu sálario: R$'))
a = int(input('Vai pagar em quantos anos? '))
m = a * 12
prest = v / m
porc = (s * 30)/100
print(f'Para pagar uma casa de R${v:.2f} em {a} anos a prestação será de R${prest:.2f}')
if prest > porc:
    print('Empréstimo negado')
else:
    print('Emprestimo pode ser CONCEDIDO')

