sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Erro! Digite novamente')
if sexo == 'M':
    print('Sexo masculino registrado com sucesso.')
else:
    print('Sexo feminino registrado com sucesso')
