maior = 0
menor = 0
for p in range(1, 6):
    peso =  float(input('Qual o peso da pessoa? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(F"O maior peso lido foi de {maior}Kg")
print(f"O menor peso lido foi de {menor}Kg")
