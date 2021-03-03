cond = str('')
cont = media = maior = menor = 0
while cond != 'N':
    num = int(input('Digite um numero: '))
    cond = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    media = media + num

    if cont == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = media / cont
print(f'Você digitou {cont} números e a média foi de {media}')
print(f'O maior valor foi de {maior} e o menor foi {menor}')
