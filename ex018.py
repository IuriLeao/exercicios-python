import math
angulo_graus = float(input("Digite o angulo em graus: "))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Seno de {angulo_graus}°: {seno:.2f}")
print(f"Cosseno de {angulo_graus}°; {cosseno:.2f}")
print(f"Tangente de {angulo_graus}°: {tangente:.2f}")


