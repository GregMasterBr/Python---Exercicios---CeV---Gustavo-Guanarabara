print('-==-'*50)
print(' EXERCÍCIO 81 - LISTAS LER VARIOS NÚMEROS NÚMEROS E QUANTOS NUMEROS, ORDEM E SE O CINCO TA LISTA')
print('-==-'*50)
numeros = []
while True:
    n = int(input(f'Digite um  número: '))
    if n < 0:
        break
    else:
        numeros.append(n)
print(f'Quantidade de números digitados: {len(numeros)}')
print(f'Ordem Original: {numeros}')
num = numeros[:]
num.sort()
print(f'Ordem decrescente: {num}')
x = int(input(f'Digite um  número para procurar na lista: '))
if x in num:
    print(f'O número {x} está na lista')
else:
    print(f'O número {x} não está na lista')

