p = float(input("digite o valor principal do emprestimo"))
r = float(input("digite a taxa de juros anual"))
t = float(input("digite o tempo em anos"))

valor_total = p*(1 + r*t)

print(valor_total)