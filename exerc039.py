from datetime import date
print('-==-'*50)
print('EXERCICIO 39 - EXÉRCITO - ALISTAMENTO')
print('-==-'*50)
nasc=int(input('Digite o ano de nascimento: '))

ano = date.today().year

idade = ano - nasc

print('Você nasceu em {}, nós estamos no ano {} e você tem {} anos'.format(nasc,ano,idade))

if(idade<18):
    print('Logo você vai ser alistar em campeão. Mais {} anos de farra'.format(18-idade))
elif(idade==18):
    print('Tá na sofrência aí? Bate continência malandrão.')
else:
    print('Tá na reserva né? Faz {} que você passou pelo periodo de alistamento kkk'.format(idade-18))
