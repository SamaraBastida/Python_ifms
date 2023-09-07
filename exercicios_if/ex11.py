#Dado o código de determinado produto, qual a sua classificação?
# Utilize a seguinte tabela de referência:

cod = int(input("Insira o codigo do produto "))

if cod == 1: 
    print("Alimento não perecivel")

elif cod >= 2: 
    if cod <=4:
        print("Alimento perecivel")
        
    elif cod >= 5:
        if cod <= 6:
            print("Vestuario")
        
        elif cod == 7: 
            print("Higiene pessoal")

        elif cod >=8:
            if cod <= 15:
             print ("Limpeza e utensilios domesticos")
     
            else: print("Código inválido")
