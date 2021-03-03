v = int(input('Qual foi a velocidade: '))
if v > 80:
    multa = (v - 80) * 7
    print(f'Você foi multado em R${multa}')

else:
    print('Você não foi multado')

