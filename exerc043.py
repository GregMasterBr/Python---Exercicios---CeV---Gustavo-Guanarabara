print('-==-'*50)
print('EXERCICIO 43 - IMC')
print('-==-'*50)

peso = float(input('Qual é o seu peso?: '))
altura = float(input('Qual é a sua altura?: '))

imc = peso/(altura**2)

print('O IMC é: {:.2f}'.format(imc))

if(imc<18.5):
    print('ABAIXO DO PESO')
elif(imc<25):
    print('PESO NORMAL')
elif(imc<30):
    print('SOBREPESO')
elif(imc<35):
    print('OBESIDADE GRAU 1º')
elif(imc<40):
    print('OBESIDADE GRAU 2º')
else:
    print('OBESIDADE GRAU 3º')
