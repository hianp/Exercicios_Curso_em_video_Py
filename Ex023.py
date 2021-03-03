n = int(input('Digite um numero: '))
print(f'Analisando o numero {n}')
print(f'Unidade {n % 10}')
print(f'Dezena {(n % 100) // 10}')
print(f'Centena {(n % 1000) // 100}')
print(f'Milhar {(n % 10000) // 1000}')

