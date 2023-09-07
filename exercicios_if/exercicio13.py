gen = int(input("Digite 1 para mulher ou 2 para homem: "))

if (gen == 1):
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura ** 2)
    
    if(imc < 19.1):
        print("Abaixo do peso")
    elif(19.1 <= imc < 25.8):
        print("No peso ideal")
    elif(25.8 <= imc):
        print("Acima do peso")


elif(gen == 2):
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura ** 2)

    if(imc < 20.7):
        print("Abaixo do peso")
    elif(20.7 <= imc < 26.4):
        print("No peso ideal")
    elif(26.4 <= imc):
        print("Acima do peso")

else:
    print("Insira um número válido")