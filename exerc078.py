print('-==-'*50)
print('AULA 17 - PARTE 1 LISTAS ')
print('-==-'*50)

lanches = ['hamburguer','coca-cola','pizza','sorvete']
print(f'{lanches}')
#adicionar um elemento da lista
lanches.append('pudim')
print(f'{lanches}')
lanches.insert(0,'Pão')
print(f'{lanches}')
#remover um item da lista
del lanches[0]
print(f'{lanches}')
lanches.pop() #lanches.pop(-1)
print(f'{lanches}')
lanches.remove('pizza')
print(f'{lanches}')

if 'pizza' in lanches:
    lanches.remove('pizza')

valores = list(range(4,11))
print(valores)

valores2 = list(range(1,21,2))
print(valores2)
#ordenar é o método sort() parametro reverse=True - ordem inversa
valores2.sort(reverse=True)
print(valores2)
print(len(valores2))

for c,v in enumerate(valores2):
    print(f'Na posição {c} encontrei o valor {v}')
valores3 = list()

for cont in range(0,5):
    valores3.append(int(input('Digite um valor: ')))

print(valores3)
#Propriedades
a =[2,3,4,7]
b=a
print(a)
print(b)
#-> O phyton cria uma LIGAÇÃO/VINCULO FORTE entre as listas. Se eu alterar B, vai mudar A
b[2] =8
print(a)
print(b)
#Para criar uma cópia precisa usar o  o parametro :
c = a[:] #Apenas Copia, não tem vínculo
print(c)
c[2] = 20
print(c)



print('-==-'*50)
print(' EXERCÍCIO 78 - LISTAS LER 5 NÚMEROS E MOSTRAR O MAIOR E MENOR')
print('-==-'*50)
num = list()
for x in range(0,5):
    num.append(int(input('Digite um valor: ')))
print(num)
print(f'O maior valor é {max(num)}. Ele está na posição: {num.index(max(num))}')
print(f'O menor valor é {min(num)}. Ele está na posição: {num.index(min(num))}')