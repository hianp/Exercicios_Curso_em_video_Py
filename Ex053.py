"""
frase = str(input('Digite uma frase: ')).lower().replace(' ', '').strip()

f = frase[::-1].lower().replace(' ', '')

if f == frase:
    print('É um palíndromo')
else:
    print(f'{frase} não é um palíndromo')
    print('Erro')

"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')
