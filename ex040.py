n1 = float(input('Nota da primeira prova? '))
n2 = float(input('Nota da segunda prova? '))
cal = (n1 + n2)/2
if cal < 5.0:
    print(f"Reprovado!!, Sua média foi {cal}")
elif cal >= 7.0:
    print(f"Aprovado!!, Sua média foi de {cal}")
elif cal >= 5.0 and cal < 7.0:
    print(f"Recuperação!!, Sua média foi de {cal}")

