import random
print('-==-'*50)
print('EXERCÍCIO 77 - TUPLA VÁRIAS PALAVRAS E PROCURAR A VOGAL ')
print('-==-'*50)

palavras = ('Gregorio','Almeida','Queiroz','Amanda','Altava','Palhares','Se','Amam')
vogais ='aeiou'

for p in range (0,len(palavras)):
    palavra = palavras[p].lower()
    print(f'\nNa Palavra {palavra.upper()} temos ', end='')
    for l in range(0,len(palavra)):
        if (palavra[l]) in vogais:
            print(f'{palavra[l]}, ', end='')
