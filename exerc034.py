print('-==-'*50)
print('AUMENTO MÚLTIPLO DO SALÁRIO DO MAN')
print('-==-'*50)
func=float(input('Qual é o salário do funcionário? R$'))

aumento_salario=func * 1.15 if func<=1250 else func*1.10

print('Funcionário, parabéns o seu salário de R${:.2f} agora é R${:.2f}. O seu aumento foi de R${:.2f}'.format(func,aumento_salario,aumento_salario-func))