# Solicita um número ao usuário
n = int(input("Digite um número para calcular a sequência de Fibonacci: "))

# Inicializa os dois primeiros números da sequência
a, b = 0, 1
contador = 0

# Exibe a sequência de Fibonacci até o número 'n'
print("Sequência de Fibonacci até o número", n, ":")

while contador < n:
    print(a, end=" ")
    a, b = b, a + b  # Atualiza os valores de a e b
    contador += 1  # Incrementa o contador