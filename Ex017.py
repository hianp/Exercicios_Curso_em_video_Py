import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = math.sqrt((co ** 2) + (ca ** 2))
print(f'A hipotenusa vale {h:.2f}')
