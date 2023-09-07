#Dados três números, qual o maior?

a = int(input("insira o primeiro numero "))
b = int(input("insira o segundo numero "))
c = int(input("insira o terceiro numero "))

maior = int()

if a > b:
    if a > c:
        maior = a

else:
    if b>c:
        maior = b
    else:
        maior = c
        
print(maior, "é o maior número")
