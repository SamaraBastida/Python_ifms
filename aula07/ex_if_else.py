salario = float(input("informe teu salario: "))
nota = float(input("informe tua nota: "))
numero = int(input("informe teu numero da sorte: "))
idade = int(input("informe tua idade: "))
 
print("\nvoce ganha", salario)
if salario > 5000:
    print("vc ta bem ein!")
else:
    print("vc ainda chega la!")
 
print("\nvoce tirou nota", nota)
if nota < 7:
    print("vc esta de recuperacao!")
else: print("vc passou de ano!")
 
print("\nteu numero da sorte eh", numero)
if numero % 2 == 0: print("numero par")
else:
    print("numero impar")
 
if numero % 5 == 0: print("numero multiplo de 5.")
else: print("numero nao multiplo de 5")
 
print("\ntua idade eh", idade)
if idade >= 18:
    print("vc eh maior de idade,")
    print("ja eh responsavel legalmente.")
else:
    print("vc ainda eh menor de idade")
    print("aguarde",18-idade,"anos")
 
print("\nfim do programa.")