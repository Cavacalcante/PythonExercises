dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos km você andou com o carro? '))

preco_total = (dias * 60) + (km * 0.15)

print('O valor total a ser pago é R${:.2f}'.format(preco_total))