from datetime import date
print('-==-'*50)
print('EXÉRCICIO 55 - VERIFICAR SE PESO')
print('-==-'*50)
maior=0
menor=999
for c in range(1,6):
    peso=float(input('{}º - Qual é o seu peso:'.format(c)))
    if(peso>maior):
        maior=peso
    if(peso<menor):
        menor=peso
print('O louco meu! O mais pesado é {}kg e o mais leve é {}kg '.format(maior,menor))