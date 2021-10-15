print('-==-'*50)
print('EXERCÍCIO 73 - CORINTHIANS CAMPEÃO DO BRASILEIRÃO DE 2017')
print('-==-'*50)

classificacao=('','Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense','Atlético-MG','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport','Vitória','Coritiba','Avaí','Ponte Preta','Atlético-GO')

print('CLASSIFICAÇÃO CAMPEONATO BRASOLEIRO - 2017')
for pos,clube in enumerate(classificacao):
    if pos>0:
        print(f'{pos}º - {clube}')


print('\nCLASSIFICADOS LIBERTADORES 2018')
print(classificacao[0:6])
for libertadores in range(1, 6):
    print(f'{libertadores}º - {classificacao[libertadores]}')

print('\nREBAIXADOS PARA O CAMPEONATO DA SÉRIE B 2018')
for pos,clube in enumerate(classificacao):
    if pos>16:
        print(f'{pos}º - {clube}')

print('\nCLUBES QUE PARTICIPARAM DO CAMPEONATO BRASILEIRO 2017 - AZ')
for cont in range(1, len(classificacao)):
    print(f'{sorted(classificacao)[cont]}')

print(f'\nA Chapecoense ficou em {classificacao.index("Chapecoense")}º no Campeonato Brasileiro de 2017')