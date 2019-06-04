valor = float(input('Digite um valor em metros: '))
centimetros = valor*100
milimetros = centimetros*10

print('{} metro(s) tem {:.0f} centímetros e {:.0f} milimetros'.format(valor, centimetros, milimetros))
