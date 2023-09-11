#Ler um número inteiro e escrever um valor aleatório com base nesse número:
# uma letra maiúscula se o usuário inseriu 1, uma letra minúscula 
# se o usuário inseriu 2 e um dígito se o usuário inseriu qualquer valor
# que não seja 1 ou 2.

import random
n = int(input("Digite 1 para MAIUSCULA. ou 2 minuscula: "))

if (n == 1):
    
    primeiro = 65
    ultimo = 90
    quantidade = ultimo - primeiro + 1
    maiuscula = primeiro + int(random.random() * quantidade)
    print(chr(maiuscula))
    
elif(n == 2):
    p = 97
    u = 122
    q = u - p + 1
    minuscula = p + int(random.random() * q)
    print(chr(minuscula))
else:
    pn = 48
    un = 57
    qn = un - pn +1
    inteiro = pn + int(random.random()*qn)
    print(inteiro)