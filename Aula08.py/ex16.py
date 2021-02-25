#EXPLICAÇÃO
#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

#from math import sqrt
#num = int(input('Digite um número: '))
#raiz = sqrt(num)
#print('A raiz de {} é {:.2f}'.format(num,raiz))

#import random
#num = random.random
#print(num)

#EXERCISE 16
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num,trunc(num)))

