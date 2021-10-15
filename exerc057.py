print('-==-'*50)
print('AULA 14  - WHILE - EXPLICAÇÃO DOS CONCEITOS')
print('-==-'*50)

'''for c in range(1,11):
    print(c)
print('Esturutura com o FOR')'''
c=1
'''while c<=10:
    print(c)
    c=c+1
print('Esturutura com o WHILE')'''

r='S'
'''while r=='S':
    n=int(input('Digite um número: '))
    r=str(input('Deseja Continuar? [S/N]: ')).upper().strip()
print('FIM')'''

par=0
impar=0
x=1
numeros = []
while x!=0:
    x=int(input('Digite um número: '))

    if(x%2==0):
        if(x!=0):
            par=par+1
    else:
        impar = impar+1
    numeros.append(x)
print('FIM com o X=0')
numeros.pop()#Remove o último elemento daa lista. No caso que sempre será 0
print('A sequencia de números foi {}'.format(numeros))
print('PAR {}\nIMPAR {}'.format(par,impar))
print('Você informou {} números. O maior numero foi {} e o menor foi {} e a soma da lista é:{}. A média é {}'.format(len(numeros),max(numeros),min(numeros),sum(numeros),sum(numeros)/len(numeros)))

b = 0
while b==0:
    s=str(input('Digite o seu Sexo: [M/F]: ')).upper().strip()[0]

    if s=='F' or s=='M':
        b=1
    else:
        print('DIGITE CORRETAMENTE!!!')
        b=0

#Mais ELEGANTE

sexo = str(input('Digite o seu Sexo: [M/F]: ')).strip()[0]
while  sexo not in 'MmFf':#MAIS ELEGANTE
    sexo = str(input('Digite o seu Sexo: [M/F]: ')).upper().strip()[0]
print('O sexo registrado foi: {}'.format(sexo))