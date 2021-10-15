print('-==-'*50)
print('EXÉRCICIO 69 -   ANALISANDO DADOS')
print('-==-'*50)
homens = mulheres_20 = maiores18=0

while True:
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual a seu sexo: [M/F]')).upper().strip()[0]

    if idade >=18:
        maiores18+=1
    if sexo in 'Mm':
        homens+=1
    else:
        if idade < 20:
            mulheres_20+=1
    r=str(input('\nDeseja Cadastrar mais alguma pessoa?[S/N]'))
    if r in 'Nn':
        break


print(f'\nQuantidade de Homens {homens}\nMaiores de 18 anos {maiores18}\nMulheres com menos de 20 anos {mulheres_20}')
