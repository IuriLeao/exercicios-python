digitados = 0
soma = 0
numero = 0
while True:
    numero = int(input('Digite Mais um numero: '))
    if numero == 999:
        break
    digitados += 1
    soma += numero

print(f'A quantidade de numeros digitados foram {digitados}, e a soma deles foram {soma}')