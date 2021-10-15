print('-==-'*50)
print(' EXERCÍCIO 84 - ANÁLISE DE DADOS')
print('-==-'*50)
pessoas = []
while True:
    n = str(input('Nome: ')).upper().strip()
    p = float(input('Peso (kg): '))
    pessoas.append([n,p])
    r = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'Ordem das pessoas LEVEs ')
pessoas.sort(key=lambda x:x[1])
for pes in pessoas:
    print(pes)
print(f'Ordem das pessoas PESADAS')
pessoas.sort(key=lambda x:x[1], reverse=True)
for pes in pessoas:
    print(pes)