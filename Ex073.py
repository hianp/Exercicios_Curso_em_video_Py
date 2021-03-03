tabela = ('Flamengo', 'Internacional', 'AtleticoMG', 'São Paulo', 'Fluminense', 'Gremio', 'Palmeiras', 'Santos', 'AthleticoPR', 'Bragantino')
print('=-' * 20)

print('Os 5 primeros colocados da tabela são: ')
for time in tabela[0:5]:
    print(time)

print('=-' * 20)

print('Os ultimos 4 colocados da tabela são: ')
for time in tabela[-4:]:
    print(time)

print('=-' * 20)

print("Os times participantes em ordem: ")
lista = []
for time in tabela:
    t = time
    lista.append(t)
s = sorted(lista)
a = '\n'.join(s)
print(a)

print('=-' * 20)

print(f"O gremio está na {tabela.index('Gremio') + 1} posição")
