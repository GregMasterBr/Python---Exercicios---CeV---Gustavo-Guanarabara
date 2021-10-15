print('-==-'*50)
print('EXÉRCICIO 51 - Progressão Aritmética')
print('-==-'*50)

a = int(input('Informe o primeiro termo da PA: '))
r = float(input('Informe a razão da PA: '))
an=a
print('-==-'*50)
for c in range(1,11):
   print('Termo {}º - é {:.2f} '.format(c,an))
   an = an + r

'''for c in range(a,11,int(r)):
   print('Termo {}º - é {:.2f} '.format(c,a))
   #an = an + r'''