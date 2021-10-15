print('-==-'*50)
print(' EXERCÍCIO 89 - MEDIA ESCOLAR ALUNOS')
print('-==-'*50)
alunos=[]
while True:
    nome = str(input('NOME: ')).upper().strip()

    nota1 = float(input('NOTA 1  : '))
    nota2 = float(input('NOTA 2  : '))
    alunos.append([nome,nota1,nota2])
    r = str(input('DESEJA CONTINUAR? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
print()
print('MÉDIA APROVAÇÃO - ESCOLA GREGMASTER')
#print(alunos)
print('-'*50)
print(f'{"#":<4} {"NOME":1<0} {"MÉDIA":>8}')
print('-'*50)
for pos,c in enumerate(alunos):
    #print(c)
    print(f'{pos+1:<4} {c[0]:<10}       {sum(c[1:])/2:.02f}')
print()
while True:
    idAluno = int(input('Informe o Id do Aluno para Pesquisar  : '))

    if idAluno>len(alunos):
        print('FINALIZANDO')
    else:
        idAluno-=1
        print(f" As notas do {alunos[idAluno][0]} - foram NOTA 1: {alunos[idAluno][1]} e NOTA 2: {alunos[idAluno][2]} ")