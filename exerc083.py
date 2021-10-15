print('-==-'*50)
print(' EXERCÍCIO 83 - VERIFICAR SE A EXPRESSÃO É VÁLIDA')
print('-==-'*50)

expressao = str(input('Digite uma expressão: '))
#Dessa maneira aceita uns bugs.
abriu=expressao.count('(')
fechou=expressao.count(')')


print(abriu)
print(fechou)

if(abriu==fechou):
    print(expressao.index('('), expressao.index(')'))
    if expressao.index('(') > expressao.index(')'):
        print('EXPRESSÃO NAO É VÁLIDA')
    else:
        print('EXPRESSÃO É VÁLIDA')
else:
    print('EXPRESSÃO NAO É VÁLIDA')

#GUANABARA
pilha = []

for s in expressao:
    if s =='(':
        pilha.append('(')
    elif s==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('[GUANABARA] EXPRESSÃO É VÁLIDA')
else:
    print('[GUANABARA] EXPRESSÃO NÃO É VÁLIDA')

