alt = float(input('Digita a altura da parede: '))
lg = float(input('Digite a largura da parede: '))

area = alt*lg
tinta = area/2

print('A área da parede é de {0:.2f}m²'.format(area))
print('Você precisará de {0:.2f} litros de tinta'.format(tinta))