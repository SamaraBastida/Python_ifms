dia = int(input("digite o dia: "))
mes = int(input("digite o mes: "))
ano = int(input("digite o ano: "))
j = (1461*(ano+4800+(mes-14)/12))/4+(367*(mes-2-12*((mes-14/12)))/12-(3*((ano+4900+(mes-14/12)/100))/4+dia-32075))
   

#dia juliano pra dia da semana considerando domingo o primeiro dia da semana
sem =   (j+1)%7

#dia juliano pra dia da semana considerando segunda o primeiro dia da semana
sem2 = j%7+1

#dia juliano em data gregoriana
f = j+1401+(4*j+274277)/146097*3/4+(-38)
e = 4*f+3
g = e%1461/4
h = 5*g+2
D = h%153/5+1
M = (h/153+2)%12+1
Y = e/1461-4716+(12+2-M)/12