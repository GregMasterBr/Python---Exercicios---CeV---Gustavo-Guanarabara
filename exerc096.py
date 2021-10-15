def nomeExercicio(titulo):
    print('-==-'*50)
    print(f'{"":^60} {titulo}')
    print('-==-'*50)
nomeExercicio('EXERCÍCIO 95 - ')

def breakLoop():
    r = str(input('DESEJA CONTINUAR? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break