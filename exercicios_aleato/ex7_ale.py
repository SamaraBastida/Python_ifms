#Gerar uma letra aleatória entre 'a' e 'z'.

import random

primeiro = 97
ultimo = 122
quantidade = ultimo - primeiro + 1
sorteado = primeiro + int(random.random() * quantidade)

print("a letra sorteada foi: ", chr(sorteado))