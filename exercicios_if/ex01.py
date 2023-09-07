#Dado um inteiro, ele é par ou ímpar?

x = int(input("insira um número para descobrir se é par ou ímpar "))

if x % 2 != 0:
    print("o número é ímpar")
else:
    print("o número é par")