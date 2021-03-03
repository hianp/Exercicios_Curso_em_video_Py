n1 = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] - converter para BINÁRIO
[ 2 ] - converter para OCTAL
[ 3 ] - converter para HEXADECIMAL''')

opc = int(input('Sua opção:'))
if opc == 1:
    print(f'{n1} convertido para BINÁRIO é igual a {bin(n1)[2:]}')
elif opc == 2:
    print(f'{n1} convertido para OCTAL é igual a {oct(n1)[2:]}')
elif opc == 3:
    print(f'{n1} convertido para HEXADECIMAL é igual a {hex(n1)[2:]}')
else:
    print('''Erro!
    Selecione somente entre as 3 opções.''')
