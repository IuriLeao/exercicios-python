s = input("Digite um gênero (F ou M): ").upper()
while s not in ('F', 'M'):
    s = input("Digite outro gênero! ").upper()
print('Acabou')