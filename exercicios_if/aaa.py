gen = int(input("Digite F para feminino e M para masculino "))
peso = float(input("Insira seu peso atual "))
altura = float(input("Insira sua altura "))

imc = peso / (altura**2)

if imc <19.1:
    if gen =='f':
        print("Ela esta abaixo do peso")
     
    elif gen == 'm':
        if imc <20.7:
            print("ele esta abaixo do peso")
            
if imc == 19.1:
    if imc<25.8:
        if gen == 'f':
           print("ela esta no peso ideal")
                
        elif gen == 'm':
            if imc == 20.7:
                if imc<26.4:
                    print("ele esta no peso ideal")
                        
if imc >= 25.8:
    if gen == 'f':
        print("ela esta acima do peso")
        
    elif gen == 'm':
        if imc >= 26.4:
            print("ele esta acima do peso")
                    
                
    