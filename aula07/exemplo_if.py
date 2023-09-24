salario = float(input("informe teu salario: "))
nota = float(input("informe tua nota: "))
numero = int(input("informe teu numero da sorte: "))
idade = int(input("informe tua idade: "))
 
print("\nvoce ganha", salario)
if salario > 5000:
    print("vc ta bem ein!")
 
print("\nvoce tirou nota", nota, end=', ')
if nota < 7:
    print("vc esta de recuperacao!")
elif nota >= 7:
    print("Parabens! voce esta aprovado")
 
print("\nteu numero da sorte eh", numero, end=" ")
if numero % 2 == 0: print(",um numero par", end=" ")
if numero % 5 == 0: print("que é um numero multiplo de 5.")
 
print("\ntua idade eh", idade, end=" ")
if idade >= 18:
    # Obrigatório usar indentação para indicar o bloco
    print("vc eh maior de idade,", end=". ")
    print("ja eh responsavel legalmente.")
    
elif idade < 18:
    print("Voce ainda é menor de idade")
print("\nfim do programa.")