print('-==-'*50)
print('ANALISANDO O TRIÂNGULO')
print('-==-'*50)

print('Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.')

s1=float(input('Primeiro seguimento: '))
s2=float(input('Segundo  seguimento: '))
s3=float(input('Terceiro seguimento: '))


if(s1 < s2+s3 and s2 < s1+s3 and s3 <s1+s2):
    print('Os seguimentos formam um Triângulo')
else:
    print('Os seguimentos não formam um Triângulo')

print('\n APRENDENDO A POR CORES\ CÓDIGO ANSI - ESCAPE SEQUENCE')

print('\033[1:33:44m TEXTO')

#STYLE 0=NONE;1=BOLD;4=UNDERLINE;7=INVERTER
#TEXT 30 até 37
#BACK 40 até 47 cores de fundo