v = float(input('Valor original da divida: ')) 
d = float(input('Valor da taxa de desconto por pagamento antecipado: '))
m = float(input('Numero de meses de antecedencia: '))

desconto = v * (1 - d * m)

print(desconto)