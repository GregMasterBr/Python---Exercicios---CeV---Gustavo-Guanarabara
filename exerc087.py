print('-==-'*50)
print(' EXERCÍCIO 87 - MELHORAR MATRIZ 3X3 - DIMENSIONAL')
print('-==-'*50)
soma_3col = pares = 0

matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        n = int(input(f"Digie o valor [{l+1}]x[{c+1}]: "))
        matriz[l].append(n)
        pares = pares + n if n % 2 == 0 else pares
        if c==2:
            soma_3col+= n
print('-='*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f"Soma dos valores Pares é: {pares}: ")


print(f'[MAP] A SOMA DA MATRIZ É: {sum(map(sum, matriz))}')
print(f'[FOR] A SOMA DA MATRIZ É: {sum(sum(x) for x in matriz)}')
print(f'A SOMA DA 3 COLUNA É: {soma_3col}')
print(f'A SOMA DA DOS PARES É: {pares}')
print(f'DA ERRADO   - O MAIOR VALOR É: {max(max(matriz[:][:]))}')
print(max(matriz[:][:]))
maior = 0

for z in range(0,3):
    if z==0:
        maior=matriz[1][c]
    elif matriz[1][c]> maior:
        mai = matriz[1][c]

print(f'O MAIOR VALOR DA SEGUNDA LINHA É? {maior}')


#NAO FUNCIONOUprint(f'[FOR] A SOMA DOS PARES É: {sum(sum(x if x % 2 == 0 else 0) for x in matriz)}')



