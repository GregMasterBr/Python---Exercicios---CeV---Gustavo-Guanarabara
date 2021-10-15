print('-==-'*50)
print('EXÉRCICIO 61 - Progressão Aritmética com While')
print('-==-'*50)

a = int(input('Informe o primeiro termo da PA: '))
r = float(input('Informe a razão da PA: '))
an=a

x = 1
while x<11:
   print('Termo {}º - é {:.2f} '.format(x,an))
   an = an + r
   x+=1

