import math
a = float(input('Digite um angulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))

print(f'O seno de {a} é {sen:.3f}')
print(f'O cosseno de {a} é {cos:.3f}')
print(f'A tangente de {a} é {tg:.3f}')
