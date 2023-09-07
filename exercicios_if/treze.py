peso = float(input("Insira seu peso atual "))
altura = float(input("Insira sua altura "))
gen = input("Digite F para feminino e M para masculino ")

imc = peso / (altura**2)


if gen == 'f':
    imc < 19.1
    print("Você está abaixo do peso")
    
elif gen == 'm' and imc < 20.7:
    print("Você está abaixo do peso")
    
else:
    if gen == 'f' and imc <= 19.1: 
        if imc < 25.8:
            print("Você está no peso ideal")
    
    elif gen == 'm' and imc <= 20.7:
     if imc < 26.4:
         print("Você está no peso ideal")
    else:
        if gen == 'f':
         imc < 25.8
         print("Você está acima do peso")
    
        elif gen == 'm' and imc < 26.4:
          print("Você está acima do peso")
            

    
    


     
            

    
    


     