n1 = float(input('Qual é a distancia da sua viagem? '))
p1 = 0.5
p2 = 0.45
if n1 <= 200:
    print(f"O preço da sua passagem ira ser R${(p1*n1)}" )
elif n1 >= 200:
    print(f"O preço da sua passagem ira ser R${(n1*p2)} ")
