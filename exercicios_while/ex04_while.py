#Dada a quantidade de estudantes da turma de Algoritmos,
# seguida pelas notas das provas de cada estudante, 
# qual a maior nota e a média das notas dessa turma?

estudante = int(input("Insira a quantidade de estudantes na turma de algoritmos "))
total = 0
contador = 1
maior = 0

while contador <= estudante:
    nota = float(input(f"Digite a nota do {contador}º estudante (entre 0 e 10): "))
    if nota > total:
        maior = nota
     
    total = total + nota
    contador = contador + 1

media = total / estudante

print("A média da classe é:", media, "e a maior nota foi:", maior)

