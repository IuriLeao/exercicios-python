# Solicita um número ao usuário
numero = int(input("Digite um número para calcular seu fatorial: "))

# Função para calcular o fatorial usando um loop while
def fatorial(n):
    if n < 0:
        return "Fatorial não é definido para números negativos."
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

# Exibe o resultado
print(f"O fatorial de {numero} é {fatorial(numero)}")