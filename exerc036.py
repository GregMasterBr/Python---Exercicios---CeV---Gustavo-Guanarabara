print('-==-'*50)
print('AULA 12 - EXPLICAÇÃO')
print('-==-'*50)
nome=str(input('Qual é o seu nome: ')).capitalize().strip()

if(nome=='Gregorio'):
    print('Nome de Gênio')
elif(nome=='Maria' or nome=='Pedro' or nome=='Paulo'):
    print('Nome popular no BRASIL')
elif(nome in 'Ana Macarrão Jéssica Cláudia Mercedez'):
    print('Desculpa, mas seu nome é dahora. Enganei você!')
else:
    print('Que legal, é o nome do meu cachorro.')

#print('Tenha um bom dia, \033[1;31;40m{}'.format(nome))
print('Tenha um bom dia, {}'.format(nome))

print('-==-'*50)
print('EXERCICIO 36 - EMPRÉSTIMO BANCÁRIO')
print('-==-'*50)

casa = float(input('{}, seja Bem-vindo ao Banco Explorando Você. Por favor, informe o valor da casa que quer simular financiamento: R$'.format(nome)))

salario = float(input('{}, Quanto você ganha: R$'.format(nome)))

tempo = int(input('Qual o período de financiamento em meses?'))

val_max_parcela=salario*0.3

mensalidade = casa/tempo

if(mensalidade<=val_max_parcela):
    print('{}, PARABENS. O Seu emprestimo foi APROVADO!'.format(nome))
elif(val_max_parcela-mensalidade<=150):
    print('{}, Não Aprovado. O Seu emprestimo não foi APROVADO mas VOU FAZER UM ESQUEMA!'.format(nome))
else:
    print('{}, LAMENTO. O Seu emprestimo NÃO FOI APROVADO!'.format(nome))

print('Sua Mensalidade foi de R${:.2f}'.format(mensalidade))