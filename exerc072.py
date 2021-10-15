print('-==-'*50)
print('AULA 16# TUPLAS - EXERCÍCIO 72')
print('-==-'*50)
print('AS TUPLAS SÃO IMUTÁVEIS!!!')
lanche=('A',1,5.5,'B')
lanche is tuple
for c in lanche:
    print(c)

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} -- {cont}')

for pos, c in enumerate(lanche):
    print(c,pos)
print('-==-'*50)
print('EXERCÍCIO 72 - TUPLA PREENCHIDA')
print('-==-'*50)

numeros=('zero','um', 'dois', 'tres', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

while True:
    n=int(input('Digite um número: '))
    if n<0 or n > 20:
        print('Número Inválido. Digite entre 0 e 20')
    else:
        print(f'{n} =>  {numeros[n].upper()}')
