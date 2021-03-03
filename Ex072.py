tupla = tuple(range(21))

lista = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input("Digite um numero entre 0 e 20: "))

# podes-se usar um while True também.
# while True:
#   num = int(input())
# if 0 <= num <= 20:
#   break
while num > 20 or num < 0:
    num = int(input("Tente novamente. Digite um numero entre 0 e 20: "))

if num < 20 or num >= 0:
    print(f"Você digitou o numero {lista[num]}")

