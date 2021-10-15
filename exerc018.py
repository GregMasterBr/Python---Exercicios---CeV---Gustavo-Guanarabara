import random
import math
import emoji

print('Calcular a Hipotenusa')
co = float(input('Digite o valor do Cateto Oposto:'))
ca = float(input('Digite o valor do Cateto Adjacente'))

hip = math.sqrt(pow(co,2)+pow(ca,2))
print(emoji.emojize("A hipotenusa deste :triangular_ruler: é {:.2f}",use_aliases=True).format(hip))
print('-----'*20)
hip = math.hypot(co,ca)
print(emoji.emojize("A hipotenusa deste :triangular_ruler: é {:.2f}",use_aliases=True).format(hip))
print('-----'*20)
print('\n')
print('####'*20)

print('Calcular o Seno, Cosseno e Tangente')
ang = float(input('Informe o valor do ângulo: '))
#s = co / hip
#c = ca / hip
#t = co / ca
ang_r = math.radians(ang)
s = math.sin(ang_r)
c = math.cos(ang_r)
t = math.tan(ang_r)

print('O ângulo {0:.0f}º, tem {1:.2f} como SENO, {2:.2f} como COSSENO e {3:.2f} como TANGENTE'.format(ang,s,c,t))