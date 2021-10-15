import random
print('-==-'*50)
print('EXERCÍCIO 74 - NÚMEROS ALEATÓRIOS NA TUPLA')
print('-==-'*50)
numeros=(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
#numeros=(random.randint(1,10),*5))


for n in numeros:
    print(f'{n} ',end='')
#print(numeros)
print(f'\nMAIOR: {max(numeros)}')
print(f'MENOR: {min(numeros)}')