print('EXÉRCICIO 50 - LER 6 NÚERMOS E SOMAR OS PARES')
s=0
for c in range (1,7,1):
    n=int(input('Informe um número:'))
    if (n%2==0):
        s+=n
print('Pronto, a soma dos números é {}'.format(s))
print('-'*50)
