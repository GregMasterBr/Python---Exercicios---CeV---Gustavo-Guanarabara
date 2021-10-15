print('-==-'*50)
print('EXÉRCICIO 67 - TABUADA COM WHILE FODA')
print('-==-'*50)

while True:
    n = int(input('\nInforme um número para realizar a tabuada:'))
    if n<0:
        break
    c=1
    for c in range(1, 11):
        print('{} X {:2} = {}'.format(n, c, n * c))
print('-'*50)

