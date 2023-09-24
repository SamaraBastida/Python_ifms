#Qual o intervalo de inteiros de cada item a seguir? 
# (escrever cada intervalo em uma linha)
#a [0,10], b[10,0], c[-10,10], d[100,1]

print("\nIntervalo de inteiros de [0,10]")
i = 1
while i < 9:
    print(i, end= ' ')
    i = i + 1
print(i)

print("\nIntervalo de inteiros de [10,0]")
i = 9
while i  > 0:
    print(i, end= ' ')
    i = i - 1
print(i)

print("\nIntervalo de inteiros de [-10,10]")
i = -9
while i  < 9:
    print(i, end= ' ')
    i = i + 1
print(i)

print("\nIntervalo de inteiros de [100,1]")
i = 99
while i  > 1:
    print(i, end= ' ')
    i = i - 1
print(i)