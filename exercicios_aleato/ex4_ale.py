#Dados dois inteiros m e n gerar três inteiros aleatórios entre m e n.
import random

n = int(input("insira o valor de n: "))
m = int(input("insira o valor de m: "))

primeiro = n
ultimo = m
quantidade = ultimo - primeiro + 1
sorteado = primeiro + int(random.random() * quantidade)
sorteado2 = primeiro + int(random.random() * quantidade)+1
sorteado3 = primeiro + int(random.random() * quantidade)

print("Primeiro numero aleatorio", sorteado)
print("\nSegundo numero aleatorio", sorteado2)
print("\nTerceiro numero aleatorio", sorteado3)
