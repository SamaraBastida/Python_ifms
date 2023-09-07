#Dada uma letra e um inteiro N, qual a letra correspondente
# ao andar N casas à frente da letra lida (ou atrás, 
# se o N for negativo).

letra1 = input("digite uma letra ")
num = int(input("digite um numero "))

resp = chr(num + ord(letra1))
print(num, "letras depois de", letra1, "é", resp)