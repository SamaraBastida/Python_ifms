#Dados dois números, o primeiro é o dobro do segundo?

print("descubra se o primeiro numero é o dobro do segundo")
num1 = int(input("insira o primeiro número "))
num2 = int(input("insira o segundo número "))

if num1 == num2*num2:
    print("SIM")
else:
    print("NÃO")