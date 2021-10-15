print('-==-'*50)
print('EXERCICIO 42 - ANALISANDO O TRIÂNGULO e FALANDO QUE TIPO É')
print('-==-'*50)

s1=float(input('Primeiro seguimento: '))
s2=float(input('Segundo  seguimento: '))
s3=float(input('Terceiro seguimento: '))


if(s1 < s2+s3 and s2 < s1+s3 and s3 <s1+s2):
    print('Os seguimentos formam um Triângulo')
    if(s1==s2==s3):
        print("Equilátero. Todos os lados são iguais.")
    elif(s1==s2 or s2==s3 or s1==s3):
        print('Isóceles. Tem dois lados iguais.')
    else:
        print('Escaleno. Todos os lados são diferentes')
else:
    print('Os seguimentos não formam um Triângulo')

