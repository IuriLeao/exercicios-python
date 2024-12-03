x = 5  # Define o valor a ser verificado na lista mais tarde
valores = list()  # Cria uma lista vazia para armazenar os valores digitados pelo usuário

# Início do loop infinito para coletar valores
while True:
    # Solicita ao usuário um valor inteiro e adiciona à lista
    valores.append(int(input('Digite um valor: ')))

    # Pergunta ao usuário se deseja continuar
    continuar = str(input('Você deseja continuar? [S / N] ')).upper().strip()
    # Transforma a entrada em maiúscula e remove espaços ao redor

    # Verifica se a entrada está entre as opções válidas ('S' ou 'N')
    if continuar in ['S', 'N']:
        # Se o usuário escolheu 'N', interrompe o loop
        if continuar == 'N':
            break
    else:
        # Caso a entrada seja inválida, exibe uma mensagem de erro
        print('Entrada inválida, digite apenas Sim (S) ou Não (N)')

# Após o loop, exibe o total de números digitados
print(f'O total de números digitados foi {len(valores)}')

# Ordena a lista em ordem decrescente
valores.sort(reverse=True)
print(f'A lista em ordem decrescente é: {valores}')

# Verifica se o valor de x está presente na lista
if x in valores:
    print(f'O valor {x} está na lista')
else:
    print(f'O valor {x} não está na lista')