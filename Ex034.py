s = float(input('Qual seu sálario: R$'))

if s > 1250.00:
    a = ((s * 10) / 100) + s
    print(f'Você ganhou um aumento para {a:.2f}')
else:
    a = ((s * 15) / 100) + s
    print(f'Você ganhou um aumento para {a:.2f}')
