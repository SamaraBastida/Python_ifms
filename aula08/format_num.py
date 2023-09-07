#formatando numeros usando 1234.567

num = 1234.567

print(f'|{num:.2f}|') #arredonda para duas casas decimais
print(f'|{num:,.2f}|') #arredonda para duas casas decimais e separa os milhares com virgula
print(f'|{num:010.2f}|')#Arredonda para duas casas decimais, preenchendo com zeros até ocupar dez espaços.
print(f'|{num: 10.2f}|')#Arredonda para duas casas decimais e ocupa dez espaços.
print(f'|{num:<10}|')#Ocupa dez espaços alinhando à esquerda.
print(f'|{num:^10}|')#Ocupa dez espaços com alinhamento centralizado.
print(f'|{num:.2g}|')#Usa notação científica se ocupar mais de dois espaços.
print(f'|{num:.10g}|')#Usa notação científica se ocupar mais de dez espaços