preco = float(input('Digite o valor do produto: '))

desconto = preco-(preco*0.05)

print('O produto sairá R${0:.2f}'.format(desconto))