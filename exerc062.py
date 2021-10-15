print('-==-'*50)
print('EXÉRCICIO 62 - Progressão Arimética FODONA ')
print('-==-'*50)

a = int(input('Informe o primeiro termo da PA: '))
r = float(input('Informe a razão da PA: '))
an=a
ate=10
x = 1
acumulador=0
numeros=[]

while x<=ate or ate==0:
   acumulador+=1
   numeros.append(an)
   print("{} → ".format(an), end='')
   an = an + r
   x+=1
   if(x==ate):
       mais_termos = int(input('\nQuantos termos a mais quer visualizar?: '))
       ate+=mais_termos

print('\nVocê viu {} termos.'.format(acumulador))
print('NUMEROS: {}'.format(numeros))
print('SOMA: {}'.format(sum(numeros)))
print('MAIOR: {}'.format(max(numeros)))
print('MENOR: {}'.format(min(numeros)))
print('MEDIA: {}'.format(sum(numeros)/len(numeros)))
