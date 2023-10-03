# Mais exemplos de usando o for - laços alinhados

# veja estruturas de seleção ou de repetição, podemos colocá-las umas dentro das outras. 
# Veja este exemplo de um for dentro de outro for. Qual a saída?

# print("Início")
# for externo in range(1, 4):  
#     print(">", end=" ")
#     for interno in range(1, 6):
#       #nesse caso só vai voltar para o for externo quando o for interno chegar no final, ou seja, no 5
#         print(externo, interno, sep="", end=" ") #sep vai imprimir a variavel interna e externa juntas
#     print()  # Adiciona uma quebra de linha após a conclusão de cada linha interna
# print("Fim")

# Veja esse exemplo de if-else dentro de for. Qual a saída?

i = 12
for j in range(1, i + 1):
    print("", j, end="")
    # 
    if j % 5 == 0 or j % 3 == 0:
        print(" A", end="")
        # 
    if i % j == 0:
        print(" B", end="")
        # 
    else:
        print(" C", end="")
        # 



