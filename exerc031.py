print('-==-'*50)
print('VALOR DA PASSAGEM')
print('-==-'*50)
v = float(input('Informe a Distância da viagem em km: '))

if(v<=200):
    print('O valor da sua passagem é R${:.2f}'.format(v*0.50))
else:
    print('O valor da sua passagem é R${:.2f}'.format(v * 0.45))
print('\nIF OTIMIZADO. IF INLINE')
preco=v * 0.50 if v<=200 else v*0.45
print('O valor da sua passagem é R${:.2f}'.format(preco))

