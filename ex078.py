# Cria uma lista vazia para armazenar os números digitados pelo usuário
valores = list()

# Laço que itera 5 vezes para o usuário digitar os números
for c in range(0, 5):
    valores.append(int(input('Digite um numero: ')))  # Adiciona cada número digitado à lista

# Encontra o menor valor da lista usando a função min()
menor = min(valores)
# Encontra o maior valor da lista usando a função max()
maior = max(valores)

# Cria uma lista com as posições (índices) onde o menor número aparece
posicoes_menor = [i for i, v in enumerate(valores) if v == menor]
# Cria uma lista com as posições (índices) onde o maior número aparece
posicoes_maior = [i for i, v in enumerate(valores) if v == maior]


print(f'O maior numero encontrado foi {maior} na posição {posicoes_maior}')
print(f'O menor numero encontrado foi {menor} na posição {posicoes_menor}')