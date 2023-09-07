#Dada uma letra minúscula, 
# qual sua correspondente em maiúsculo?

letra = input("digite uma letra minuscula ")
cod = ord(letra)
corresp = cod - 32

if 97 <= cod <= 122:
    print("Letra digitada", letra, "minuscula vai ficar", chr(corresp))
