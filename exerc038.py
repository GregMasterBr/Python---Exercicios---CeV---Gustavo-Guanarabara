import random
from time import sleep
print('-==-'*50)
print('EXERCICIO 38 - COMPARANDO NÚMEROS')
print('-==-'*50)
num1=int(input('Digite um número inteiro entre 0-100: '))

#num2=int(input('Digite um número inteiro: '))
num2=random.randint(0,100)
print('PROCESSANDO...')
sleep(2)

if(num1>num2):
    print('O número {} é MAIOR que {}'.format(num1,num2))
elif (num1<num2):
    print('O número {1} é MAIOR que {0}'.format(num1,num2))
else:
    print('Os números são IGUAIS. {} == {}'.format(num1,num2))
