print('-==-'*50)
print('EXÉRCICIO 53 - PALINDROMO')
print('-==-'*50)

frase=str(input('Digite uma frase: ')).upper().strip()
frase_ = list(frase)
frase_ =frase_[::-1]
frase2 = ''.join(frase_)

print(frase)
print(frase_[::-1])
print(frase2)


if(frase.replace(' ','')==frase2.replace(' ','')):
    print('PALINDROMO')
else:
    print('NÃO É PALÍNDROMO')