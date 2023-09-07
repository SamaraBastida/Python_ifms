#Dada uma letra, qual a sua posição no alfabeto, 
# sendo ‘a’ a posição 1 e ‘z’ a posição 26?

letra = input("digite uma letra minuscula ")
p = ord(letra)
a = p - 97
dif = a+1

if p == 97:
    print("a letra ", letra, "esta na posicao ", a+1)
    
else:
    98 >= p <=122
    print("a letra", letra, "esta na posicao", dif)
