print('-==-'*50)
print('AULA 48 - Múltiplos de 3  - até 500')
print('-==-'*50)
s=0
soma=0
for c in range (1,501,1):
    if(c%3==0):
        s=s+1
        soma=soma+c
        print(c)
print('Na sequência entre 1-500 a soma de múltiplos de 3 é {} e tem {} numeros'.format(soma,s))