print('-==-'*50)
print('EXERCICIO 59  - CALCULADORA')
print('-==-'*50)
op=''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
print('''
MENU DE OPÇÕES
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
''')

while op!=5:
    op = int(input('Digite a sua opção '))
    if (op==1):
        print('OPÇÃO ESCOLHIDA FOI SOMAR')
        print('A SOMA ENTRE {} + NUMERO {} = {}'.format(n1,n2,n1+n2))
    elif(op==2):
        print('OPÇÃO ESCOLHIDA FOI MULTIPLICAR')
        print('O PRODUTO ENTRE {} * {} = {}'.format(n1, n2, n1 * n2))
    elif(op==3):
        print('OPÇÃO ESCOLHIDA FOI ENCONTRAR O MAIOR')
        print('O MAIOR ENTRE {} E {} = {}'.format(n1, n2, max(n1, n2)))

    elif(op==4):
        print('OPÇÃO ESCOLHIDA FOI ESCOLHER OUTROS NÚMEROS')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
    elif (op == 5):
        print('OPÇÃO ESCOLHIDA FOI ENCERRAR O PROGRAMA')
        op=5
    else:
        print('OPÇÃO INVÁLIDA')

print('SAIU DO SISTEMA')