print('Aumento de Salário')
p = float(input('Informe o salário do Funcionário: '))
d = float(input('Informe quanto vai dar de aumento em %: '))

print('Parabéns funcionário. Você conseguiu {}% de aumento de salário. Seu salário era R${} agora será de R${}. Você ganhou R${} a mais.'.format(d,p,p*((d+100)/100),p*(d/100)))