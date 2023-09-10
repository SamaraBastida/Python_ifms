#Dado um inteiro n, gerar três inteiros aleatórios entre −n e n

import random
num = int (input("insira um num inteiro "))

primeiro = num * (-1) 
ultimo = num
quantidade = ultimo - primeiro + 1
sorteado = primeiro + int(random.random() * quantidade ) 
sorteado2 = primeiro + int(random.random() * quantidade ) 
sorteado3 = primeiro + int(random.random() * quantidade ) 


print("Primeiro inteiro aleatorio:",sorteado)
print("\nSegundo inteiro aleatorio:",sorteado2)
print("\nTerceiro inteiro aleatorio:",sorteado3)