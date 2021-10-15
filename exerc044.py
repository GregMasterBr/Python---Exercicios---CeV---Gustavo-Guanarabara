print('-==-'*50)
print('EXERCICIO 44 - PAGAMENTO')
print('-==-'*50)

preco = float(input('Informe o preço do Produto:R$ '))
forma_pgto = str(input('Qual a forma de pagamento?\nA - à vista - dinheiro\nC - à vista - cartão\n2 - 2x no cartão\n3 - 3x ou mais no cartão\n Escolha a sua opção:').upper())
p = 0
if(forma_pgto=='A'):
    p=preco*0.90
elif(forma_pgto=='C'):
    p = preco * 0.95
elif(forma_pgto=='2'):
    p = preco
else:
    p = preco*1.120
print('\nVocê vai pagar R${:.2f} o seu produto'.format(p))
