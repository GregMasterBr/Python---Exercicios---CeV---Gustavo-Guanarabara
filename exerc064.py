print('-==-'*50)
print('EXÉRCICIO 64 - SOMANDO VALORES FRENETICAMENTE')
print('-==-'*50)

numeros = []
u=0
while u!=999:
    u = int(input('Digite um número?: '))
    if u!=999:
        numeros.append(u)

print('Revelando os números digitados {}. Você informou {} números. A soma dele é {}. O maior numero entre eles é: {}.  O Menor número é {}'.format(numeros, len(numeros), sum(numeros),max(numeros),min(numeros)))