n = int(input("\nInsira um numero natural: "))
i = 0
soma = 0

while i < n:
    if i % 2==1:
        i = i+1
        print(i, end=' ')
    else:
        
        num = i
        soma = soma + num
        i = i+1
print("=",soma)