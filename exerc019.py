import random
print('Sortear nomes aleatórios')
a1 = str(input('Digite o nome do Aluno:'))
a2 = str(input('Digite o nome do Aluno:'))
a3 = str(input('Digite o nome do Aluno:'))
a4 = str(input('Digite o nome do Aluno:'))
sorteado = random.choice([a1,a2,a3,a4])


print('Oi {}, você foi sorteado. Meus Parabéns. Pode ir apagar a lousa e trazer meu café.'.format(sorteado))

print('####'*20)
#lista= [a1,a2,a3,a4]
#print('Oi {}, você foi sorteado. Meus Parabéns. Pode ir apagar a lousa e trazer meu café.'.format(sorted(lista)))