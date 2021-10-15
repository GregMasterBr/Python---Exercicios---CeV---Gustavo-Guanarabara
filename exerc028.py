import random
from time import sleep
print('-==-'*50)
print('vou pensar em um número entre 0 e 5. Tente advinhar bruxo...')
print('-==-'*50)
n = int(random.randint(0,5))
u = int(input('Em que número eu pensei?: '))
print('PROCESSANDO')
sleep(3)
if(n==u):
    print('Revelando o meu número {}. Você acertou.'.format(n))
else:
    print('Revelando o meu número {}. Você errou.'.format(n))

