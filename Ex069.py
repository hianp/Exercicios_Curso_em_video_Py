maior_idade = 0
qnt_homens = 0
qnt_mulheres = 0
while True:
    print('-=' * 15)
    print('Cadastre uma pessoa')
    print('-=' * 15)
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo [M/F]: ')).strip().lower()[0]
    while sexo != 'm' and sexo != 'f':
        sexo = str(input('Qual seu sexo [M/F]: ')).strip().lower()[0]
    print('-' * 30)
    cont = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while cont != 's' and cont != 'n':
        cont = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if idade >= 18:
        maior_idade += 1
    if sexo == 'm':
        qnt_homens += 1
    if sexo == 'f':
        if idade < 20:
            qnt_mulheres += 1
    if cont == 'n':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {qnt_homens} homens cadastrados.')
print(f' E temos {qnt_mulheres} mulheres com menos de 20 anos.')


