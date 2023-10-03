# COMPARAÇÕES ENTRE WHILE E FOR..

inicio = 1
fim = 11
print("Contando até 10...")
 
cont = inicio
while cont < fim:
    print(cont)
    cont += 1
 
print("Fim!")
print("Valor final de cont:", cont)
# aqui o resultado do contador é 11

print("\nagr com for.....")

inicio = 1
fim = 11
# no for vai terminar em um numero antes
print("\nContando até 10...")
 
 
for cont in range(inicio, fim):
    print(cont)
 
 
print("Fim!")
print("Valor final de cont:", cont)
# aqui o contador vai parar em 10

i = 1
soma = 0
while i < 5:
    print("+", i, end=" ")
    soma += i
    i += 1
print("= ", soma)

# mesmo programa usando for.. com for fica mais simples
soma = 0
for i in range(1, 5):
    print("+", i, end=" ")
    soma += i
 
print("= ", soma)

# QUANDO VC NAO DEFINIR O VALOR INICIAL VAI COMECAR SEMPRE NO ZERO
print("Contando do 0 até o 9...")
for cont in range(10):
    print(cont)

# PASSO -  DEFINIR UM PADRÃO NO CONTADOR. NESSE CASO DE 5 EM 5
print("Contagem de 5 em 5...")
inicio = 0
fim = 50
passo = 5
for cont in range(inicio, fim, passo):
    print(cont)
    
# se vc der um passo negativo vai fazer uma contagem decrescente/regressiva
print("Contagem regressiva...")
for cont in range(10, 0, -1):
    print(cont)

# nao vai executar pq o inicio é menor do q o final e o passo é negativo
print("Valendo!")
for cont in range(0, 10, -1):
    print(cont)
print("Fim!")

# incrementos - aumentando / decremento - diminuindo



