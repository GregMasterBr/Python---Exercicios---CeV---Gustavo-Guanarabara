print('-==-'*50)
print(' EXERCÍCIO 80 - LISTAS LER 5 NÚMEROS E MOSTRAR O MAIOR E MENOR')
print('-==-'*50)
num = list()
print('Digite números aleatoriamente e organizar os numeros sem o SORT')

for i in range(0,5):
    n=int(input(f'Digite o {i+1}º número: '))
    if i==0 or n > num[-1]:
        num.append(n)
    else:
        p=0
        while p < len(num):
            if n <= num[p]:
                num.insert(p, n)
                break
            p += 1
print(num)
