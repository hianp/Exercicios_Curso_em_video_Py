print('Valos validar seus dados')
soma = 0
soma2 = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c} nasceu: '))
    idade = 2021 - nasc
    if idade >= 21:
        soma = soma + 1

    else:
        soma2 = soma2 + 1


print(f'{soma} chegaram a maioridade')
print(f'{soma2} não chegaram na maioridade')

