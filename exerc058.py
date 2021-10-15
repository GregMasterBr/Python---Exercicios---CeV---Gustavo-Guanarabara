print('-==-'*50)
print('EXERCICIO 58  - JOGO ADVINHAÇÃO - MELHORADO EXERC 28')
print('-==-'*50)
import random
u=-1
n = int(random.randint(0,10))
chances = 0

while u!=n:
    u = int(input('Em que número eu pensei?: '))
    chances+=1

print('Revelando o meu número {}. Você acertou mas precisou de {} chances'.format(n,chances))