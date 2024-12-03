import random
soma = 1
n1 = random.randint(0, 10)
pr = int(input('Qual numero o computador está pensando? '))

while pr != (n1):
    pr = int(input('Digite Outro valor '))
    soma += (1)

print(f"Você Acertou, Você precisou de {soma} vezes para acertar!")


