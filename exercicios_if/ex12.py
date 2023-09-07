precoE = float (input("Insira o preço da etiqueta do produto "))
pag = int (input("insira o codigo do tipo de pagamento "))
valorF = float()

if pag == 1:
    valorF = precoE - ((10/100) * precoE) 
    print("Realizando o pagamento em dinheiro o valor vai de: ", precoE)
    print("Para: ", valorF)
    
elif pag == 2:
    valorF = precoE - ((5/100) * precoE)
    print("Realizando o pagamento no deb ou pix o valor vai de: ", precoE)
    print("Para: ", valorF)
    
elif pag == 3:
    valorF = precoE / 2
    print("Realizando o pagamento em duas vezes a compra de: ", precoE, "reais")
    print("Ficara com duas parcelas de: ",valorF,)
    
elif pag == 4:
    valorF = precoE + ((10/100)* precoE)
    print("Dividindo o pagamento em 3 vezes a compra de ", precoE)
    print("Ficará dividida em 3 parcelas de: ", valorF/3)
    
    
    