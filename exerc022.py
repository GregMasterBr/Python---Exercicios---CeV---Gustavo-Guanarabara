print('~~~'*50)
nome_completo = str(input('Digite o seu nome completo: '))
print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo.strip()))
primeiro_nome = nome_completo.split()
print(primeiro_nome)
print('SEM ESPAÇO {} tem {} letras'.format(nome_completo.replace(' ',''),len(nome_completo.replace(' ',''))))
print('O primeiro nome {} tem {} letras'.format(primeiro_nome[0].upper(), len(primeiro_nome[0])))
print('~~~'*50)
#frase = str(input('Digite uma frase: '))
frase ='Eu sou Corinthiano Mano. Aqui tem um bando de louco'
print(frase[4])
print(frase[4:11])
print(frase[4:11:2])
print(frase[:5])
print(frase[5:])
print(len(frase)) #comprimento
print(frase.count('o'))#contar quantas vezes tem a letra na analise
print(frase.find('ano'))#procurar a palavra
print('Corinthiano' in frase)

print(frase.replace('Corinthiano','Palmeiras'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())#primeiro caracatere em maiusculo
print(frase.title())#todas as palavras inciias em maiusculo
print(frase.strip())#remove espalis em brancos inuteis da direita e esquerda
print(frase.rstrip())#remove espalis em brancos inuteis da direita
print(frase.lstrip())#remove espalis em brancos inuteis da esquerda
#divisão
print(frase.split())#aproveita o espaço em branco
print('X'.join(frase))

