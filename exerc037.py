import math
print('-==-'*50)
print('EXERCICIO 37 - CONVERSÃO DE BASES')
print('-==-'*50)
num=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] - CONVERTER PARA BINÁRIO
[ 2 ] - CONVERTER PARA OCTAL
[ 3 ] - CONVERTER PARA HEXADECIMAL
''')
opc = int(input('Sua Opção: '))

if(opc==1):
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif(opc==2):
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
else:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
print('-==-'*50)
print('''\n{}
BINARIO={}
OCTAL={}
HEXADECIMAL={}'''.format(num,bin(num)[2:],oct(num)[2:],hex(num)[2:]))