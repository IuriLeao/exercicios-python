n1 = float(input('Quantos dias o carro foi alugado? '))
n2 = float(input('Quantos Km Rodados? '))
c1 = (n1 * 60) + (0.15 * n2)

print (f"O total a pagar é de {c1:.1f}")
