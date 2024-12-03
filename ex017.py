import math
caceto_oposto = float(input("Digite o comprimento do caceto oposto: "))
caceto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calculo
hipotenusa = math.sqrt(caceto_oposto**2 + caceto_adjacente**2)

# exibição

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")

