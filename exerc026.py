print('~~~'*50)
frase = str(input('Digite uma frase: ')).upper().strip()

print(frase.count('A',0,len(frase)))
print(frase.count('A'))

print('Primeira vez que aparece a letra A é na posição {}'.format(frase.find('A',0)+1))
print('Última vez que aparece a letra A é na posição {}'.format(frase.rfind('A',0)+1))