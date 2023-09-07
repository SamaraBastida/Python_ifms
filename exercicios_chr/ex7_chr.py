#Dada uma letra maiúscula, 
# qual sua correspondente em minúsculo?

letra = input("digite uma letra maiuscula ")
cod = ord(letra)
corresp = cod +32

if 65 <= cod <= 90:
    print("Letra digitada", letra, "minuscula vai ficar", chr(corresp))
