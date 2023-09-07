import random
 #gerar numeros aleatorios
 
# sorteia um float no intervalo [0,1)
sorteado = random.random()
print("float aleatorio gerado no intervalo de [0,1]",sorteado)
 
# transforma em um float aleatorio entre [0,10)
sorteado = sorteado * 10
print("float aleatorio entre [0,10]",sorteado)
 
# descarta a parte decimal
int_sorteado = int(sorteado)
print("tornando o numero sorteado em inteiro",int_sorteado)

print()

print("geracao de um numero aleatorio entre[0,n]")
#declarando o valor de n
n = 20  
aleat = int(random.random()*n)
print("o numero aleatorio gerado no intervalo de 0 e", n, "foi ",aleat)

print()

print("comecando de um numero especifico") 
primeiro1 = 10
ultimo1 = 20
quantidade1 = ultimo1 - primeiro1 + 1
sort = primeiro1 + int(random.random() * quantidade1)
print(sort)

print()

print("gerando numeros aleatorios QUE sejam multiplo de 5 entre[50,100]") 
primeiro2 = 50
ultimo2 = 100
diferenca = 5
quantidade = (ultimo2 - primeiro2) / diferenca + 1
s = primeiro2 + diferenca * int(random.random() * quantidade)
print(s)






