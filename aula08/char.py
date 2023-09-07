#chr é usado em funçoes, converte numero para caracter usando a tabela asc
# ord vai converter o caracter para numero

a = 97
U = 85
cifrao = 36
maior = ">"
arroba = "@"
dois = "2"
 
print("na tabela asc o numero",a,"é referente ao caracter", chr(a))
print("na tabela asc o numero",U,"é referente ao caracter", chr(U))
print("na tabela asc o numero",cifrao,"é referente ao  caracter", chr(cifrao))
print("na tabela asc o caracter",maior,"é referente ao numero", ord(maior))
print("na tabela asc o caracter", arroba, "é referente ao numero",ord(arroba))
print("na tabela asc o caracter", dois,"é referente ao numero", ord(dois))

print()
print()

c1 = "d"
c2 = "h"
n1 = 7
 
c3 = chr(n1 + ord(c1))
print(n1, "letras depois de", c1, "é", c3)
 
n2 = ord(c2) - ord(c1) - 1
print("há", n2, "letras entre", c1, "e", c2)
 
c4 = ord(c1) * ord(c2)
print(c1, "*", c2, "=", c4)
 
n3 = ord(c1) + ord(c2)
print(c1, "+", c2, "=", n3)