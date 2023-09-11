#Gerar dois inteiros aleatórios cuja soma esteja entre [0 e 100)

import random

num = 50
sorteado = int(random.random()*num)
sorteado2 = int(random.random()*num)

soma = sorteado + sorteado2

print( sorteado, sorteado2)

print("Primeiro aleatorio", sorteado, "+ segundo aleatorio", sorteado2, "=", soma)

