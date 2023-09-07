#personalização da exibicao do texto no print
# sep="<" é oq vai ser usado para separar os argumentos usa isso no lugar de ficar colocando varios "," 
# end ="." finaliza a linha e imprime os outros prints

print("Uma sequência de números: ", 1, 2, 3, sep="<", end=". ")
print("Agora, de trás para frente: ", 3, 2, 1, sep=">")
print("Fim!")


print()

#formatando o texto

#placeholders tudo que estiver entre {}
# no lugar de colocar varios prints voce consegue fazer de uma vez
inteiro = 10
decimal = 12.34
letra = 'A'

print("um inteiro: ", inteiro)
print("um decimal: ", decimal)
print("uma letra: ", letra)
 
print(f"Um inteiro: {inteiro}.\nUm decimal: {decimal}.\nUma letra: {letra}")


a = 65
b = 2
 
# consegue colocar expressoes dentro do placeholder
print(f"A soma de 'a' e 'b' é {a+b}.\nO caractere correspondente a 65 + 2 é {chr(a+b)}")


