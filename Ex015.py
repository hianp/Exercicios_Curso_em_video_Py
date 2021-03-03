dias = int(input('Quantos dais alugados? '))
km = float(input('Quantos km rodado? '))
pago = (dias + 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')
