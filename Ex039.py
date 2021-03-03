ano = int(input('Informe seu ano de nascimento: '))
data = 2021 - ano
dez = 18 * 12
print(f'Quem nasceu em {ano} tem {data} anos em 2021')
meses = dez - (data * 12)
if data <= 17:
    f = 18 - data
    print(f'Ainda falta {f} ano(s) para se alistar')
    print(f'Seu alistamento será em {2021 + f}.')
elif data == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE')
else:
    d = int(data - 18)
    print(f'Já passou {d} ano(s) do alistamento')
    print(f'Seu alistamento foi em {2021 - d}')
