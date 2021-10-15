print('-==-'*50)
print('EXÉRCICIO 71 - BANCO GREGMASTER')
print('-==-'*50)
cedulas=[100,50,20,10,5,2,1] #Pode causar um problema, por exemplo, um random em que interrompe o fornecimento de dinheiro ou o usuario escolhe as notas que quer receber. Basta operacionalizar a lista notas.
valor=int(input('Que valor quer sacar? R$'))
sacar = valor
notas_entregue=[]
c=-1
while True:
    if sacar >0:
        c+=1
        while True:
            if sacar / cedulas[c] < 1:
              break
            else:
                sacar = sacar - cedulas[c]
                #print(f'{c} - VALOR LIBERADO: R$ {cedulas[c]} - DEVEDOR: {sacar}')
                notas_entregue.append(c)
    if sacar ==0:
        break
print('\JÁ LIBEREI SEU DINHEIRO. AGORA PAGA JUROS PRA MIM')
print('CONFIRA SUA NOTAS AÍ. TE PAGUEI ASSIM: ')

for x in range(0,len(cedulas)):
    if notas_entregue.count(x)> 0:
        print(f'{notas_entregue.count(x)} nota(s) de R${(cedulas[x])} reais')
print(f'\nTOTALIZANDO = R${valor} reais ')
