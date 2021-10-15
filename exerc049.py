print('Tabuada com FOR')
n1=int(input('Informe um número:'))
print('¨¨¨'*20)
for c in range (1,11,1):
    print('{} X {:2} = {}'.format(n1,c,n1*c))
print('Pronto, Tabuada do {} na tela'.format(n1))
print('-'*50)
