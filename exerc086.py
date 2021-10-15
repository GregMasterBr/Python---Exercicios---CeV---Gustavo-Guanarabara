print('-==-'*50)
print(' EXERCÍCIO 86 - MATRIZ 3X3 - DIMENSIONAL')
print('-==-'*50)
matriz = []
x=y=3
for i in range(x):
    matriz.append([0]*y)
    for j in range(y):
         matriz[i][j] = int(input(f'Digie o valor [{i+1}]x[{j+1}]: '))
print(matriz)
print('\n')
for lin in range(0,x):
    for col in range(0,y):
        print(f'[{matriz[lin][col]:^5}]',end='')
    print()

print('\n')
matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()