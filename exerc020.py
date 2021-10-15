import random
print('Sortear Ordem de Apresentação dos Alunos')
a1 = str(input('Digite o nome do Aluno:'))
a2 = str(input('Digite o nome do Aluno:'))
a3 = str(input('Digite o nome do Aluno:'))
a4 = str(input('Digite o nome do Aluno:'))

sorteado = random.sample([a1,a2,a3,a4],k=4)

print('[SIMPLE] Oi. Essa é a ordem de apresentação dos alunos: {}.'.format(sorteado))
#o legal de usar o sample ao invés do shuffle é q da pra limitar a quantidade de pessoas q vão apresentar, atribuindo a quantidade no 'k',
# então se na lista tiverem 10 alunos inscritos
# mas o k for igual a 5 então serão escolhidos só 5 dentre os 10 alunos
# sample([aluno1, aluno2, aluno3, aluno4], k=2)  -> serão escolhidos 2 dentre os 4 alunos
print('xxxxx'*20)
sorteado_shuffle = [a1,a2,a3,a4]
random.shuffle(sorteado_shuffle)
print('[SHUFFLE] Oi. Essa é a ordem de apresentação dos alunos: {}.'.format(sorteado_shuffle))