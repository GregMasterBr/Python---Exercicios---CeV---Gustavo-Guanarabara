from random import randint


def nomeExercicio(e,titulo):
    print('-==-'*50)
    print(f'{"":^60}EXERCÍCIO {e} - {titulo}')
    print('-==-'*50)
nomeExercicio(91,'Jogando Dados - 4 jogadores')
j=1
sorteioDados = []
jogador={}

while j<5:
    num = randint(1, 6)
    jogador={'jogador':j,'dado':num}
    #sorteioDados.append(jogador)
    sorteioDados.append(jogador.copy())
    print(f'O jogador {j}º tirou {num}')
    j+=1
print("RANKING DOS CLASSIFICAÇÃO")

#for k,v in enumerate(sorteioDados):
#    print(f'O {k} é {v}')
#print('\n')

OrdenandoListaPeloDadosMaior = sorted(sorteioDados, key=lambda k: k['dado'],reverse=True)
print(OrdenandoListaPeloDadosMaior)
print(sorteioDados)
j=1
print("RANKING DOS CLASSIFICAÇÃO")
for v in (OrdenandoListaPeloDadosMaior):
   print(f'{j}º lugar - O jogador {v["jogador"]}º - tirou no dado {v["dado"]}')
   j+=1
print('\n')



#print(sorted(sorteioDados))
#for i in sorted (sorteioDados) :
#    print ((i, sorteioDados[i]), end =" ")

#alternativa - importar o método itemgetter da lib operator
#OrdenandoListaPeloDadosMaior = sorted(sorteioDados, key=itemgetter(1), reverse=True)