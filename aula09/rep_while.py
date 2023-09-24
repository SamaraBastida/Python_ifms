#while - repetiçao/ laço ou loop
#end " " vai dar um espaço entre cada print

print("\nversão 1")
i = 10
if i < 20:
    print(i, end=" ")
    i = i + 1
print(i)

print("\nversão 2")
i = 10
while i < 20:
    print(i, end=" ")
    i = i + 1
print(i)

print("\nversão 3")
i = 100
if i < 20:
    print(i, end=" ")
    i = i + 1
print(i)

print("\nversão 4")
i = 100
while i < 20:
    print(i, end=" ")
    i = i + 1
print(i)

print("\nversão 5")
i = 1
if i < 20:
    print(i, end=" ")
print(i)

print("final das versoes")

#print("\nversão 6")  
#i = 1
#while i < 20:
 #   print(i, end=" ")  infinito
#print(i)

i = 1
soma = 0
while i < 5:
    print("+", i, end=' ')
    soma = soma + i
    i = i + 1
print("=", soma)

bit = 512
p = 0
while bit > 1:
    print(bit)
    p = p + 1
    bit = bit // 2
print("=", p)

#contador sabe quntas vezes vai repetir
# Inicialize as variáveis
total = 0
contador = 1
 
# Use um loop para ler as notas dos cinco estudantes
while contador <= 5:
    nota = float(input(f"Digite a nota do {contador}º estudante (entre 0 e 10): "))
    total = total + nota
    contador = contador + 1
 
# Calcule a média
media = total / 5
# Escreve a média da classe
print("A média da classe é:", media)

#mesmo programa só q agr não tem quantidade de estudantes definidas
#sentinela tem uma condição para fazer parar o while

total = 0
contador = 0
nota = float(input("Digite a nota do estudante (ou -1 para encerrar): "))
 
while nota != -1:
    if 0 <= nota <= 10:
        total = total + nota
        contador = contador + 1
    else:
        print("A nota deve estar entre 0 e 10. Tente novamente.") #caso o usuario digite um valor invalido
 
    nota = float(input("Digite a nota do estudante (ou -1 para encerrar): "))
 
if contador > 0:
    media = total / contador
    print("A média da classe é:", media)
else:
    print("Nenhuma nota válida foi inserida.")
    
    