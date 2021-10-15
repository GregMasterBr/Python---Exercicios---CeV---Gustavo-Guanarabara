import random
print('-==-'*50)
print('EXERCÍCIO 76 - LISTA DE COMPRAS')
print('-==-'*50)

print("#"*40)
print(f'{"MERCADO GREGMASTER":^40}')
print("#"*40)
compras=('Pão',1,'Leite',3.50,'Maça',5.00,'Arroz',11.50,'Bife',19.85)
print(f'{"Produtos":<28}{"Preço (R$)"}')
print('-'*40)
for c in range(0,len(compras),2):
    print(f'{compras[c]:.<30}R$ {compras[c+1]:0.2f}')
print('-'*40)


print('\n\n')
nome='Gregorio'
print("Prazer em te conhecer {}!".format(nome))
print("#"*10)
print("[ESCREVE COM 20 ESPACO]Prazer em te conhecer {:20}!".format(nome))
print("#"*10)
print("[ALINHADO A DIREITA 20 ESPACO]Prazer em te conhecer {:>20}!".format(nome))
print("#"*10)
print("[ALINHADO A ESQUERDA 20 ESPACO]Prazer em te conhecer {:<20}!".format(nome))
print("#"*10)
print("[CENTRALIZADO]Prazer em te conhecer {:^20}!".format(nome))
print("#"*10)
print("[CENTRALIZADO COM UM SIMBOLO]Prazer em te conhecer {:=^20}!".format(nome))