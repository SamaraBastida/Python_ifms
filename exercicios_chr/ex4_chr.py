#Dada uma letra, ela é maiúscula ou minúscula?

letra = input("digite uma letra")
cod = ord(letra)

if 65 <= cod <= 90:
    print("letra maiuscula")

elif 97 <= cod <=122:
    print("letra minuscula")
else:
    print("valor invalido")