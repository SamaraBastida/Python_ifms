#Dado um inteiro como semente, gerar três inteiros aleatórios.

import random
num = 5

random.seed(num)

sorteado = int(random.random()*num)
sorteado2 = int(random.random()*num+1)
sorteado3 = int(random.random()*num+2)

print("Primeiro inteiro aleatorio:",sorteado)
print("\nSegundo inteiro aleatorio:",sorteado2)
print("\nTerceiro inteiro aleatorio:",sorteado3)






