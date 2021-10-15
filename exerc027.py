print('~~~'*50)
nome_completo = str(input('Digite o seu nome completo: ')).strip().upper()

nome = nome_completo.split()
print(nome)

print('Seu primerio nome é {} e último nome é {}'.format(nome[0],nome[-1]))