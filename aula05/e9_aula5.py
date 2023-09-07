#Joãozinho fez sua viagem até os Estados Unidos. Porém, chegando lá, descobriu que a temperatura é medida em graus Fahrenheit, e não em Celsius.
# Dada a temperatura em graus Fahrenheit, qual a temperatura correspondente em graus Celsius? C= (f-32)*5/9

gf = float(input("insira os graus em Fahrenheit "))
gc = ((gf - 32)*5)/9
print("convertendo a temperatura de Fahrenheit ", gf,"para graus Celsius ficara: ",gc)