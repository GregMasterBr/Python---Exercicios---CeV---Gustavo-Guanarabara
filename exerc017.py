import emoji
import math
import random
num = random.randint(1,10)

print(math.sqrt(num))
print(num)

print(emoji.emojize("Aqui é treta :earth_americas:",use_aliases=True))

print('*'*20)
print('Programa para exibir o número real')
n = float(input('Digite um número: '))
aleatorio = n * random.random()

print('[CEIL] O número {} tem a parte inteira {}'.format(n,math.ceil(n)))
print('[TRUNC] O número {} tem a parte inteira {}'.format(n,math.trunc(n)))
print('[COM FORMATACAO] O número {} tem a parte inteira {:.0f}'.format(n,n))
print('[COM INT] O número {} tem a parte inteira {}'.format(n,int(n)))


print('Olha um aleatório doidão:',aleatorio)