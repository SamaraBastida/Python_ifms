#Dado um caractere, ele é um número?

carac = input("digite um unico caracter ")
cod = ord(carac)

if 48 <= cod <= 57:
    print("é um numero")

else:
    print("o caracter digitado não é um numero")