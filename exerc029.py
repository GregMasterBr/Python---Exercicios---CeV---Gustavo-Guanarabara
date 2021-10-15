import random
from time import sleep
print('-==-'*50)
print('RADAR ELETRÔNICO')
print('-==-'*50)
multa = 7
v = float(input('Qual é a velocidade atual do Carro?:'))

if(v<=80):
    print('Parabéns. Dirija com segurança')
else:
    print('RADAR. Você está acima da velocidade permitida. Você está á {:.0f}km/h enquanto a velocidade permitida é 80km/h'.format(v))
    print('Você terá que pagar uma multa de R${:.2f} e 7 pontos na carteira. Na próxima vez, respeite os limites.'.format(v-80)*multa)