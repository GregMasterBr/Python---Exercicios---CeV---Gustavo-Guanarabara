print('Quantos Dólares vc pode comprar')
r = float(input('Informe quantos reais você tem na carteira R$:'))
d = 5.73
print('A cotação do dólar atual é R${}\n'.format(d))
print('Você pode comprar US${} doláres com esses {} reais que você tem'.format(r//d,r))
print('Você pode comprar US${:.2f} doláres com esses {} reais que você tem'.format(r/d,r))