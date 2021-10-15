print('-==-'*50)
print(' EXERCÍCIO 79 - LISTAS LER NÚMEROS ALEATORIAMENTE E NÃO DEIXAR ENTRAR NÚMEROS DUPLICADOS. NO FINAL É COLOCADO EM ORDEM')
print('-==-'*50)
num = list()
print('Digite números aleatproriamente. o -1 para de receber')
while True:
    n = int(input('Digite um valor: '))
    if n<0:
        break
    else:
        if n not in num:
            num.append(n)
if len(num)>0:
    print('Olha os números dígitados')
    print(num)
    print('Os números ordenados')
    num.sort()
    print(num)
else:
    print('NÃO FOI DIGITADO NENHUM NÚMERO')






