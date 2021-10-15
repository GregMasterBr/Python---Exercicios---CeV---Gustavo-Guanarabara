from datetime import date
print('-==-'*50)
print('EXÉRCICIO 54 - VERIFICAR SE É MAIOR DE IDADE')
print('-==-'*50)
maior=0
menor=0
for c in range(1,8):
    nasc=int(input('{}º - Qual é o ano de nascimento:'.format(c)))
    idade = date.today().year-nasc
   # print('{} idade'.format(idade))
    if(idade<18):
        menor=menor+1
    else:
        maior=menor+1
print('{} menores de idade\n {} maiores de idade'.format(menor,maior))