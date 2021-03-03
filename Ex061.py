primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
termo = primeiro
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    cont += 1
print('FIM')
"""for c in range (primeiro, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('Acabou')
"""

