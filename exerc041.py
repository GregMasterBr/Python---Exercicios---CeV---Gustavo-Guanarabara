from datetime import date
print('-==-'*50)
print('EXERCICIO 41 - NATAÇÃO')
print('-==-'*50)
nasc=int(input('Digite o ano de nascimento: '))

ano = date.today().year

idade = ano - nasc
print('Você tem {} anos. Sua Categoria é: '.format(idade),end='')
if(idade<10):
    print('MIRIM')
elif(idade<15):
    print('INFANTIL')
elif(idade<20):
    print('JUNIOR')
elif(idade<21):
    print('SÊNIOR')
else:
    print('MASTER')