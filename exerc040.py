print('-==-'*50)
print('EXERCICIO 40 - MÉDIA ESCOLAR')
print('-==-'*50)
nota1=float(input('Digite a sua nota: '))
nota2=float(input('Digite a sua nota: '))

media = (nota1+nota2)/2

if (media<5):
    print('REPROVADO')
elif (media<7):
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
print('Caro aluno sua nota final foi {:.1f}'.format(media))
