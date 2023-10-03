# Programa de cálculo de juros compostos. 
# FORMULA -- M=C(1+I)^T
# C = VALOR INICIAL -> CAPITAL  I= TAXA DE JUROS 0.5  T= TEMPO INVESTIDO


C = float(input("Informe o capital inicial: $"))
i = float(input("Informe a taxa de juros anual (por exemplo, 5% como 0.05): "))
t = int(input("Informe a quantidade de anos de investimento: "))
 
for ano in range(1, t + 1):
    M = C * (1 + i) ** ano
    print(f"Ao final do ano {ano}, o montante será de ${M:.2f}")