import math
print(('=' * 20) + ' SEJA BEM VINDO AO EXERCICIO 60 ' + ('=' * 20))

n = int(input('Digite um número: '))

print('[MATH] -  O Fatorial de {}! é {}'.format(n,math.factorial(n)))

fat = 1
c=1
conjunto=''
while c<=n:
    fat = fat * c
    #conjunto +=' '.join(str(c))
    c+=1
    #print('FAT {} - N={} e N={}'.format(fat,c,c-1))

print('O fatorial de {}! é {}'.format(n,fat))
z = n
fat = 1
while z>0:
    fat = fat * z
    conjunto +=''.join(str(z))+(' x ' if z>1 else ' = {}'.format(fat))

    #print('{} X '.format(z),end='')
    z-=1

print('O fatorial de {}! é {}'.format(n,fat))
print('A sequência é:{0}'.format(conjunto))