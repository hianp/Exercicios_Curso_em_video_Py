print('-=' * 15)
print('LOJA SUPER BARATÃO')
print('-=' * 15)
soma = contador = mais = menor = 0
barato = ''
while True:

    nome = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: '))
    if preco > 1000:
        mais += 1
    soma += preco
    cont = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    contador += 1
    mais_de_mil = 1000
    while cont != 's' and cont != 'n':
        cont = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if cont == 'n':
        break
    if contador == 1:
        menor = preco
        barato = nome
    if contador > 1:
        if preco < menor:
            menor = preco
            barato = nome

print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra foi: R${soma:.2f}')
print(f'Temos {mais} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
