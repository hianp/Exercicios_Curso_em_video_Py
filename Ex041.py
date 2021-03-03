nasc = int(input('Digite o seu ano de nascimento: '))
data = 2021 - nasc
print(f'Sua idade é {data}')

if data <= 9:
    print('Categoria MIRIM')
elif data <= 14:
    print('Categoria INFANTIL')
elif data <= 19:
    print('Categoria JUNIOR')
elif data == 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
