# Cria uma lista vazia para armazenar os valores únicos
valores = list()

# Inicia um loop infinito que será interrompido apenas com a condição definida
while True:
    # Solicita ao usuário que digite um valor numérico e o converte para inteiro
    n = int(input('Digite um valor: '))

    # Verifica se o valor digitado já está na lista
    if n not in valores:
        # Se o valor não estiver na lista, adiciona-o e exibe uma mensagem de sucesso
        valores.append(n)
        print('Valor adicionado com sucesso! ')
    else:
        # Se o valor já estiver na lista, exibe uma mensagem de duplicidade
        print('Valor duplicado, Não vou adicionar')

    # Solicita ao usuário que indique se deseja continuar ou não,
    # convertendo a resposta para maiúscula e removendo espaços extras
    continuar = input('Quer continuar? [S / N]').upper().strip()

    # Verifica se a entrada é válida (apenas 'S' ou 'N')
    if continuar in ['N', 'S']:
        # Se a resposta for 'N', interrompe o loop
        if continuar == 'N':
            break
    else:
        # Caso a entrada seja inválida, exibe uma mensagem de erro
        print("Entrada inválida, Digite apenas 'S' ou 'N'.")

# Ordena a lista de valores em ordem crescente
valores.sort()

# Exibe a lista ordenada ao usuário
print(valores)