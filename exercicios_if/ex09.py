#Em certa região, o preço pelo fornecimento de energia elétrica 
# depende do consumo em kWh, conforme a seguinte tabela:
#até 500 - preco 0,40 ----- acima de 500 - preco 0,65

consumo = int(input("Insira seu consumo de energia "))
pagamento = int()

if consumo <= 500:
    pagamento = consumo * 0.40
    print("O preço pago pela energia é", pagamento)
    
elif consumo > 500:
    pagamento = consumo * 0.65
    print("O preço pago pela energia é", pagamento)
    
