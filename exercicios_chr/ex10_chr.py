#Dadas duas letras, quantas letras há entre as duas?

letra1 = input("digite a primeira letra ")
letra2 = input("digite a segunda letra ")

n1 = ord(letra1) 
n2 = ord(letra2) 

if n2 < n1:
   a = n1 - n2 - 1
   print("tem", a, "letras entre ", letra2, "e",letra1)
    
elif n2 >n1:
    b =  n2 - n1 - 1
    print("tem", b, "letras entre", letra1,"e", letra2)
    

