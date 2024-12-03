s1 = float(input("Qual Seu salario? "))
c1 = s1 + (10/100) * s1
c2 = s1 + (15/100) * s1
if s1 >= 1250:
    print(f"Seu novo salario será de R${c1:.2f}")
else:
    print(f"Seu Novo salario será de {c2:.2f}")
