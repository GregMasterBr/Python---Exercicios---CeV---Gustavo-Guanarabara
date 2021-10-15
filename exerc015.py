print("Conversor de Temperaturas")
c = float(input("Informe a temperatura em ºC:"))

f = (c*(9/5))+32 # 9/5 = 1.8
k = (c + 273.15)

#print('A temperatura {}ºC é {}ºF Fahrenheit e {}ºK Kelvin'.format(c,f,k))

print('A temperatura {0}ºC é {1}ºF Fahrenheit e {2}ºK Kelvin'.format(c,f,k))