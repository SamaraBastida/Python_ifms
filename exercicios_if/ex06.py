#Dados dois números, qual o maior deles e a diferença 
# absoluta entre eles? (a diferença absoluta é o maior menos o menor).

a = int(input("insira o primeiro numero "))
b = int(input("insira o segundo numero "))
c = int()
d = int()

if (a > b): 
    c = a
    d = b
    dif = c - d
    print("o maior é o primeiro numero")
    print("A diferença é de", dif)

elif (b > a): 
    c = b
    d = a
    dif = c - d
    print("o maior é o segundo numero")
    print("A diferença é de", dif)

