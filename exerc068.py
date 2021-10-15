import random
print('-==-'*50)
print('EXÉRCICIO 68 - PAR OU IMPAR RAIZ')
print('-==-'*50)
ganhou=0
jogos=0
while True:
    computador = random.randint(1,10)
    n=int(input('Escolha um número: '))
    op = str(input('Você quer Par ou Ímpar [P/I]: ')).upper().strip()[0]
    r = 'PAR' if (computador + n)%2==0 else 'IMPAR'
    if(r[0]==op):
        print(f'COMPUTADOR: {computador} - USUARIO: {n} - TOTAL DEU {computador + n} - RESULTADO: {r}')
        ganhou+=1
    else:
        print(f'COMPUTADOR: {computador} - USUARIO: {n} - TOTAL DEU {computador + n} - RESULTADO: {r}')
        break

print(f'\nVocê jogou {ganhou+1} e ganhou {ganhou}.')