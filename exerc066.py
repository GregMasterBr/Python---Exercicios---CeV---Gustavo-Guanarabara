print('-==-'*50)
print('AULA 15 - WHILE + TRUE + BREAK')
print('-==-'*50)
print('EXÉRCICIO 66 - SOMANDO VALORES FRENETICAMENTE COM S/N')
print('-==-'*50)
numeros=[]
while True:
    n = int(input('Digite um número: '))
    if n==999:
        break
    numeros.append(n)

print('F strings')
print(f'Foram digitados {len(numeros)} e a soma entre eles é {sum(numeros)}')

print('-==-'*50)

