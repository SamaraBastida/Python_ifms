#Dado um inteiro como semente, gerar três inteiros aleatórios.

import random
num = int(input("digite um numero "))

random.seed(num)
print(random.random())
print(random.random())
print(random.random())


