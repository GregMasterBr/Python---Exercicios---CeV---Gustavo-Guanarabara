from datetime import date
print('-==-'*50)
print('ANO BISSEXTO')
print('\nChama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).\n Isto é feito com o objetivo de manter o calendário anual ajustado com a translação da Terra e com os eventos sazonais relacionados às estações do ano. O ano presente (2020) é bissexto.\n O ano bissexto anterior foi 2016 e o próximo será 2024.')
print('-==-'*50)

ano = int(input('Qual ano quer analisar? Coloque 0 para o ano atual: ').upper())
if (ano==0):
    ano = date.today().year
if(ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0):
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

