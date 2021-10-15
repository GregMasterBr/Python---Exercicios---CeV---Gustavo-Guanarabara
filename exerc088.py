from random import randint
from time import sleep
print('-==-'*50)
print(' EXERCÍCIO 88 - JOGANDO MEGASENA')
print('-==-'*50)
jogos = []
jogo = []
n=0
j=0
print('JOGO DA MEGA SENA')
j = int(input('Quantos JOGOS quer que eu sorteie? '))
preço = 4.5*j

while j>0:
    while True:
        n = randint(1, 60)
        #print(n)
        if n not in jogo:
            jogo.append(n)

        if len(jogo) == 6:
            print(f'{len(jogos)+1}º JOGO - Olha o jogo feito: {jogo}')
            sleep(0.5)
            jogos.append(jogo)
            #jogo.clear()
            jogo = []
            break
    j-=1
    if j<1:
        break
print()
print(f'VOCÊ PRECISA PAGAR R${preço:.02f}.\nOlha os Jogos realizados: \n{jogos}')
print()
print('FOR')
for jg in  jogos.sort():
    print(jg)

