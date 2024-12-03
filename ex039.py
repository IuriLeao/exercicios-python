nasci = float(input('Qual seu ano de nascimento?'))
data = 2006
at = (nasci) - (data)
if nasci >= 2007:
    print(f'Você ainda não pode se alistar, faltam {at:.0f} anos para isso')
elif nasci == 2006:
    print(f'Você deve comparecer o mais rapido possivel a uma junta milita!!')
elif nasci <= 2006:
    print(f'Já passou o tempo de se alistar, passaram {-at:.0f} anos que você deveria ter ido')