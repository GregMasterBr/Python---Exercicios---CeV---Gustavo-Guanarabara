print('-==-'*50)
print('EXÉRCICIO 65 - SOMANDO VALORES FRENETICAMENTE COM S/N')
print('-==-'*50)
numeros = []
u=0
opc =''
while opc!='N': #while opc in 'Ss':
    u = int(input('Digite um número?: '))
    numeros.append(u)
    opc = str(input('QUER CONTINUAR? [S/N]')).strip().upper()[0]
print('Revelando os números digitados {}. Você informou {} números. A soma dele é {}. O maior numero entre eles é: {}.  O Menor número é {}'.format(numeros, len(numeros), sum(numeros),max(numeros),min(numeros)))