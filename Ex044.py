p = float(input('Preço do produto: '))
print('''Agora escolha a forma de pagamento:
 [ 1 ] à vista dinheiro/cheque
 [ 2 ] à vista cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão
 Dinheiro e cheque você ganha 10% de desconto, já à vista no cartão, ganha-se 5%
 3x ou mais no cartão tem o aumento de 20% de juros.''')

c = int(input('Condição de pagamento: '))
if c == 1:
    des = (p * 10) / 100
    print(f'Sua compra de R${p:.2f} vai custar R${p - des:.2f} no final')
elif c == 2:
    des = (p*5)/100
    print(f'Sua compra de R${p:.2f} vai custar R${p - des:.2f} no final')
elif c == 3:
    print(f'Sua compra vai custar R${p:.2f}')
elif c == 4:
    juros = (p*20)/100
    print(f'O total a se pagar com 20% de juros: R${p + juros:.2f}')
