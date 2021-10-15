print('-==-'*50)
print(' EXERCÍCIO 82 - LISTAS LER VARIOS NÚMEROS NÚMEROS E SEPARAAR EM PARE E IMPAR')
print('-==-'*50)
numeros = []
par = []
impar = []
while True:
    n = int(input(f'Digite um  número: '))
    if n < 0:
        break
    else:
        numeros.append(n)
        if n%2==0:
            par.append(n)
        else:
            impar.append(n)

print(f'Quantidade de números digitados: {len(numeros)}')
print(f'Ordem Original: {numeros}')
if len(par)>0:
    print(f'PARES: {par}')
else:
    print('NÃO FOI INFORMADO NÚMERO PAR')
if len(impar)>0:
    print(f'IMPARES: {impar}')
else:
    print('NÃO FOI INFORMADO NÚMERO ÍMPAR')
