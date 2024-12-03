from random import randint

# Gerando números aleatórios
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# Imprimindo os números sorteados com espaço entre eles
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')  # Adiciona um espaço após cada número
print()  # Para garantir que a próxima impressão fique em uma nova linha

# Imprimindo o maior e o menor valor sorteado
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')