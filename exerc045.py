import emoji
import random
import time
print('-==-'*50)
print('EXERCICIO 45 - JOKEMPÔ')
print('-==-'*50)
print(emoji.emojize('1 - :fist: - PEDRA',use_aliases=True))
print(emoji.emojize('2 - :hand: - PAPEL',use_aliases=True))
print(emoji.emojize('3-  :v:    - TESOURA',use_aliases=True))

opc = int(input('Digite qual o seu objeto: '))

jokenpo=[1,2,3]

random.shuffle(jokenpo)
#print(jokenpo)
computador = random.choice(jokenpo)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO...')
time.sleep(1)
print('ESCOLHA DO COMPUTADOR {}\n'.format(computador))
jogo=['PEDRA','PAPEL','TESOURA']
resultado =''
if(opc==computador):
    resultado='EMPATE'
else:
    if(opc==1):#PEDRA
        if(computador==2):
            resultado='COMPUTADOR GANHOU. PEDRA PERDE PARA PAPEL'
        else:
            resultado='VOCÊ GANHOU. PEDRA GANHA DE TESOURA'
    elif(opc==2):#PAPEL
        if(computador==1):
            resultado='VOCÊ GANHOU. PAPEL GANHA DE PEDRA'
        else:
            resultado='VOCÊ PERDEU. PAPEL PERDE DE TESOURA'
    elif(opc==3):#TESOURA
        if(computador==1):
            resultado='COMPUTADOR GANHOU. PEDRA GANHA DE TESOURA'
        else:
            resultado='VOCÊ GANHOU. TESOURA GANHA DE PAPEL'

print('{}. O Duelo foi foi:{}x{} '.format(resultado,jogo[opc-1],jogo[computador-1]))


