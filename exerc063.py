import math
print('-==-'*50)
print('EXÉRCICIO 63 - SUQÊNCIA DE FIBONACCI ')
print('-==-'*50)

n = int(input('Informe termos quer mostrar: '))
numeros = []
fib = [0,1]
c=2
while c<n:
    fib.append(fib[c-2]+fib[c-1])
    c+=1
print('{}'.format(fib))

print('''\nNa matemática, os números de Fibonacci são uma sequência ou sucessão definida como recursiva pela
fórmula:
F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1 .
Os primeiros números de Fibonacci são:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, ...
Esta sequência foi descrita primeiramente por Leonardo de Pisa, também conhecido como Fibonacci,
para descrever o crescimento de uma população de coelhos.''')

print('\n')
print('{}'.format(math.fiv))