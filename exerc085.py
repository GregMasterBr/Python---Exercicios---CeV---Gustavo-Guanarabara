print('-==-'*50)
print(' EXERCÍCIO 85 - RECEBENDO OS VALORES')
print('-==-'*50)
num = [[],[],[]]
n = -1
for i in range(0,7):
    n=int(input(f'Digite o {i+1}º valor: '))
    num[0].append(n)
    if n % 2 == 0:
        num[2].append(n) #PAR
    else:
        num[1].append(n) #IMPAR

print(num)
print(f'Os PARES são: {sorted(num[2])}')
print(f'Os ÍMPARES  são: {sorted(num[1])}')
