print('Loja com Descontaço - Black Friday')

p = float(input('Informe o preço do Produto: '))
d = float(input('Informe quanto vai dar de desconto em %: '))

print('Caro cliente, o preço deste produto é R${} mas eu conversei com o gerente e consegui {}% de desconto. Então o produto vai ficar R${}. Parabéns'.format(p,d,p*((100-d)/100)))
print('Você economizou {}'.format(p*(d/100)))