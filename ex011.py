n1 = float(input('Qual é largura da tua parede'))
n2 = float(input('Qual é a altura da sua parede'))
area = float(n1 * n2)
q_tinta = area / 2

print(f"Sabendo que sua parede tem uma area total de {area:.2f}m², Você precisaria de {q_tinta:.1f} litros de tinta, para pintar tudo")

