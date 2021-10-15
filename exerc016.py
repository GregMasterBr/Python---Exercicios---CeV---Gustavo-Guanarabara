print("Aluguel de Carros")
d = int(input('Quantos dias desejar alugar o carro:'))
km = int(input('Rodar quantos Km o carro:'))
fixo = 60
diaria= 0.15
print('o Valor a pagar por {} dias é: R${}'.format(d, d*fixo +(diaria*km)))