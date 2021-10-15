import random
print('-==-'*50)
print('EXERCÍCIO 75 - NÚMEROS ALEATÓRIOS NA TUPLA')
print('-==-'*50)

numeros=(random.randint(3,9),random.randint(3,9),random.randint(3,9),random.randint(3,9),random.randint(3,9))

print(numeros)
if 9 in numeros:
    print(f'O número 9 apareceu: {numeros.count(9)} vezes')
else:
    print(f'O número 9 NÃO APARECEU')
#print(f'O número 3 apareceu na posição: {numeros.index(3)}ª')
if 3 in numeros:
    print(f'O número 3 apareceu na posição: {numeros.index(3)+1}ª')
else:
    print('O número 3 não foi sorteado na lista')

print('Os números Pares Sorteados foram: ',end='')
for pos,n in enumerate(numeros):
    if n%2==0:
        print(f'{n} ',end='')

print('\n')
