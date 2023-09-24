#Dada uma sequência de números seguida pelo número zero, 
# qual a soma dos números?

i = 0
soma = 0
n = ()
while n != 0:
     n = int(input("Digite um número e 0 para encerrar "))
     soma = soma + n
    
     if n == 0:
        print("a soma da sequencia digitada é: ",soma)
