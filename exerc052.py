print('-==-'*50)
print('EXÉRCICIO 52 - NÚMERO PRIMO')
print('-==-'*50)

#n = int(input('Informe um número: '))
#print('{}'.format(n//n))
#if(n%n==0):
#    print('{} é número primo'.format(n))
#else:
#    print('{} NÃO é número primo'.format(n))


for c in range(2,101):
    if(c%2!=0 or c==2):
        #print('Pegando os Impares, exceto o 2')

        #m = n ∙ k
        if (c % c == 1):
            # print('{} é número primo'.format(c))
            print('{}'.format(c),end=' ')

   # if (c % c == 0):
   #     print('{} é número primo'.format(c))
    #else:
     #    print('{} NÃO é número primo'.format(c))

'''
for c in range(2,101):
    if(c%2!=0 or c==2):
        #print('Pegando os Impares')
        if(c%3!=0 and c!=3):

            print('{}'.format(c),end=' ')
'''


num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print("O número {} foi divisível {} vezes!".format(num, contador))

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")