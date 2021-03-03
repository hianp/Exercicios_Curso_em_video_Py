l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))
area = l * a

print('Sua parede tem a dimensao de {}x{}e sua área é de  {}m²'.format(l, a, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(area / 2))
