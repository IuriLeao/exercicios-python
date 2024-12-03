n1 = int(input('Digite um número para ver sua tabuada'))

print(f"\nTabuada do {n1}:\n")

for i in range(1, 11):
    resultado = n1 * i
    print(f"{n1} x {i} = {resultado}")
