def nomeExercicio(titulo):
    print('-==-'*50)
    print(f'{"":^60} {titulo}')
    print('-==-'*50)
nomeExercicio('EXERCÍCIO 93 - APROVEITAMENTO JOGADOR DE FUTEBOL')
artilheiros = []
desempenho = {}
aproveitamento =[]
gols_feito = []
while True:
    desempenho = {}
    gols_feito = []
    desempenho["nome"]= str(input('Jogador: ')).upper().strip()
    
	p = int(input('Partidas que jogou: '))
    desempenho["partidas"] = p
    aproveitamento.append(desempenho)

    for j in range(1,p+1):
        gols = int(input(f'Gols na {j}ª partida: '))
        gols_feito.append({"partida":j,"gols":gols})
    desempenho["gols"] = gols_feito

    artilheiros.append(desempenho.copy())
    print()
    r = str(input('DESEJA CONTINUAR? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
print()
# print(f"{artilheiros[0]}")
# print()
# print(f"{artilheiros[1]}")
# print()
jog = []
for j in range(0,len(artilheiros)):
    golz =artilheiros[j]['gols']
    totGols=0
    for g in range (0,len(golz)):
        totGols=totGols+golz[g]['gols']
    jog.append({"jogador":artilheiros[j]['nome'],"partidas":artilheiros[j]['partidas'],"gols": totGols,"aproveitamento":totGols/artilheiros[j]['partidas']})
    print(f'Jogador: {artilheiros[j]["nome"]} - realizou {artilheiros[j]["partidas"]} partidas e marcou: {totGols} gols. COM UM APROVEITAMENTO {totGols/artilheiros[j]["partidas"]} gols por partida.')

#print(jog)

#https://www.alura.com.br/artigos/trabalhando-com-o-dicionario-no-python