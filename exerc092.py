from datetime import date
def nomeExercicio(titulo):
    print('-==-'*50)
    print(f'{"":^60} {titulo}')
    print('-==-'*50)
nomeExercicio('EXERCÍCIO 92 - Cadastro de trabalhador ')

pessoa = {}
while True:
    pessoa["nome"] = str(input('Nome: ')).upper().strip()
    pessoa["nasc"] =int(input('Ano de Nascimento: '))
    pessoa["idade"] = date.today().year -  pessoa["nasc"]
    pessoa["cpts"] = int(input('Carteira de Trabalho (0 não tem): '))
    if pessoa["cpts"]==0:
        break
    pessoa["contratacao"]  = int(input('Ano de Contratação: '))
    pessoa["salario"]  = float(input('Salário: R$'))
    pessoa["aposentadoria"] =(40 - (date.today().year - pessoa["contratacao"] )) + date.today().year
    pessoa["aposentado"] =pessoa["aposentadoria"]-pessoa["nasc"]

    break
print('-==-' * 50)
for k,v in pessoa.items():
    print(f"O campo: {k} tem o valor: {v}")
print()
print(pessoa)
