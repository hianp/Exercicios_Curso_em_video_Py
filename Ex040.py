n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print(f'Media {media}')
if media < 5:
    print('Reprovado')
elif 5 <= media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')
