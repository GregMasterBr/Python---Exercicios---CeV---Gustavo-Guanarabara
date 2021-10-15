print('-==-'*50)
print('EXÉRCICIO 56 - PESSOAS')
print('-==-'*50)
media = 0
soma_idade=0
idade_x=0
nome_mais_velho='Não Tem'
menos_20=0
for c in range(1,5):
    nome=str(input('{}º - Nome:'.format(c)))
    idade=int(input('{}º - Idade:'.format(c)))
    sexo =str(input('{}º - Sexo [M/F]:'.format(c)).upper())
    print('--' * 50)
    soma_idade=soma_idade+idade
    if(sexo=='M' and idade_x<idade):
        idade_x=idade
        nome_mais_velho=nome
    if(sexo=='F' and idade<20):
        menos_20=menos_20+1

print('A média de idade da galera é {}. Homem mais velho = {}. E tem {} mulheres menos de 20 anos'.format(soma_idade/4,nome_mais_velho,menos_20))
