import random
print('-==-'*50)
print('AULA 19 - VARIÁVEIS COMPOSTAS - DICIONÁRIOS')
print('-==-'*50)

#REVISAO
#= TUPLAS ()
#= LISTA []
#= DICIONÁRIOS {}

dados = dict() # dados={}

dados={'nome':'Gregorio','idade':29,'sexo':'M','nome':'Amanda','idade':31,'sexo':'F'}
print(dados)
del dados['sexo']
dados['peso']=50
print(dados)
filmes={
        'titulo':'Star Wars' ,
         'ano':1977 ,
          'diretor':'George Lucas'

        }
print(filmes)
print(filmes.values())
print(filmes.keys())
print(filmes.items())
print()

for k,v in filmes.items():
    print(f'O {k} é {v}')
print('\n')
brasil = []
estado_1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado_2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado_1)
brasil.append(estado_2)
print(brasil[0])
print(brasil[0]['sigla'])
print(brasil)

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa: ')).upper().strip()
    estado['sigla']=str(input('Sigla do Estado: ')).upper().strip()[:2]
    estado['populacao'] = float(input('População: '))
    estado['governador'] = str(input('Governador: '))
    brasil.append(estado.copy())
print(brasil)
print('\n')
for e in brasil:
    for k,v in estado.items():
        print(f'O Campo {k} tem o valor {v}')
print('\n')
def nomeExercicio(e,titulo):
    print('-==-'*50)
    print(f'{"":^60}EXERCÍCIO {e} - {titulo}')
    print('-==-'*50)
nomeExercicio(90,'SITUAÇÃO DO ALUNO E MÉDIA')
alunos = dict()
alunos["nome"] = str(input('Nome do Aluno: '))
alunos["nota1"] = float(input('Nota 1: '))
alunos["nota2"] = float(input('Nota 2: '))
alunos["media"] = (alunos["nota1"]+alunos["nota2"])/2

if alunos["media"]<5:
    alunos["situacao"]='REPROVADO'
elif alunos["media"]<7:
    alunos["situacao"] = 'RECUPERACAO'
else:
    alunos["situacao"] = 'APROVADO'

print(alunos)
for k,v in alunos.items():
    print(f'O Campo {k} tem o valor {v}')