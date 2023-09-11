#Dados dois inteiros m e n, gerar três inteiros aleatórios múltiplos de m entre 0 e n

import random

n = int(input("insira o valor de n: "))
m = int(input("insira o valor de m: "))

primeiro = n
ultimo = m
diferenca = m
quantidade = (ultimo - primeiro) / (diferenca) + 1
sorteado = primeiro + diferenca * int(random.random() * quantidade)
sorteado2 = primeiro + diferenca * int(random.random() * quantidade)
sorteado3 = primeiro + diferenca * int(random.random() * quantidade* quantidade)

print("Primeiro numero aleatorio", sorteado)
print("\nSegundo numero aleatorio", sorteado2)
print("\nTerceiro numero aleatorio", sorteado3)
