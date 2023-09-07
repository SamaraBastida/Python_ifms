#Dado um caractere, ele é uma letra?

carac = input("digite uma letra ")
letra = ord(carac)

if 65 <= letra <= 90:
    print("é uma letra")
    
if 97 <= letra <=122:
 print("é uma letra")
 
else:
    print("o caracter digitado não é uma letra")