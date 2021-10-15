print('-==-'*50)
print('EXERCÍCIO 94 - UNINDO DICIONÁRIOS E LISTAS')
print('-==-'*50)

pessoas=[]
pessoa={}
soma_idade=0
mulheres = []
pessoas_velhas = []
while True:
    pessoa["nome"] = str(input('Nome: ')).upper().strip()
    pessoa["idade"] = int(input('Idade: '))
    pessoa["sexo"]= str(input('sexo: ')).upper().strip()[0]
    pessoas.append(pessoa)
    if pessoa["sexo"] in 'Ff':
        mulheres.append(pessoa)
    soma_idade = soma_idade + pessoa["idade"]
    r = str(input('DESEJA CONTINUAR? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
    pessoa={}
media_idade = soma_idade/len(pessoas)
print(f"Foram cadastradas {len(pessoas)} pessoas no sistema")
print(f"A média de idade é: {media_idade} anos entre as pessoas no sistema")
#print(pessoas)
if len(mulheres)>0:
    print("As mulheres cadastradas no sistema são: ")
    for key, m in enumerate(mulheres):
        print(f"{m['nome']}",end=' ')
else:
    print("Não foi cadastrado MULHERES no sistema")

for k,p in enumerate(pessoas):
    #print(k,p)
    if(p['idade']> media_idade):
        pessoas_velhas.append(p)
print()
if len(pessoas_velhas)>0:
    print(pessoas_velhas)
else:
    print("Não Tem Pessoas Com mais Idade que a média")

