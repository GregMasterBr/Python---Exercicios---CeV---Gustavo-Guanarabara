print('-==-'*50)
print('EXÉRCICIO 70 -   ANALISANDO DADOS')
print('-==-'*50)
produtos=[]
precos=[]
mais1000=0
while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o Preço do Produto: R$'))
    if preco > 999:
        mais1000+=1
    produtos.append(produto)
    precos.append(preco)

    r=str(input('\nDeseja Cadastrar mais algum produto?[S/N]'))
    if r in 'Nn':
        break

print(f'TOTAL GASTO: R${sum(precos):.2f}')
print(f'PRODUTO MAIS BARATO: {produtos[precos.index(min(precos))]} - R${min(precos):.2f}')
print(f'PRODUTOS MAIS CAROS DO QUE R$1.000,00 {mais1000}')


