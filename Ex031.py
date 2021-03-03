d = int(input('Digite quantos km é a viagem: '))

if d <= 200:
    print(f'O preço da passagem é R${d * 0.5:.2f}')
else:
    print(f'O preço da passagem por passar de 200km é de R${d * 0.45:.2f}')

