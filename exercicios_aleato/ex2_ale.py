#Dado um inteiro n, gerar três inteiros aleatórios entre 0 e n.

import random
num = int (input("insira um num inteiro "))

sorteado = int(random.random()*num)
sorteado2 = int(random.random()*num+1)
sorteado3 = int(random.random()*num+2)

print("Primeiro inteiro aleatorio:",sorteado)
print("\nSegundo inteiro aleatorio:",sorteado2)
print("\nTerceiro inteiro aleatorio:",sorteado3)

