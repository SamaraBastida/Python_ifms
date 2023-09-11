#Gerar uma senha aleatória de 8 dígitos com letras maiúsculas, minúsculas e inteiros
import random

primeiro = 65
ultimo = 90
quantidade = ultimo - primeiro + 1
maiuscula = primeiro + int(random.random() * quantidade)

p = 97
u = 122
q = u - p + 1
minuscula = p + int(random.random() * q)

pn = 48
un = 57
qn = un - pn +1
inteiro = pn + int(random.random()*qn)



#senha?????
#print("Sua senha é:",senha )