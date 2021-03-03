primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
termo = primeiro
contador_termos = 0
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    cont += 1
    contador_termos += 1
print('Pausa')
x1 = 0
while x1 == 0:
    mais = int(input('Quantos termos você quer mostrar a mais: '))
    x = termo + (5 * mais)

    while termo < x:
        print(f'{termo} -> ', end='')
        termo += razao
        contador_termos += 1
    if mais != 0:
        print('Pausa')

    if mais == 0:
        x1 += 1
print(f'Progressão finalizada com {contador_termos} termos mostrados')
