ano_atual = 2024  # define o ano atual
soma_menores = 0
soma_maiores = 0

# pega os anos de nascimento
anos_nascimento = [
    int(input('Digite o ano de nascimento da primeira pessoa: ')),
    int(input('Digite o ano de nascimento da segunda pessoa: ')),
    int(input('Digite o ano de nascimento da terceira pessoa: ')),
    int(input('Digite o ano de nascimento da quarta pessoa: ')),
    int(input('Digite o ano de nascimento da quinta pessoa: ')),
    int(input('Digite o ano de nascimento da sexta pessoa: ')),
    int(input('Digite o ano de nascimento da sétima pessoa: '))
]

for ano_nascimento in anos_nascimento:
    idade = ano_atual - ano_nascimento  # calcula a idade
    if idade < 18:
        soma_menores += 1  # soma menor de idade
    else:
        soma_maiores += 1  # soma maior de idade

print(f'Ao todo tivemos {soma_maiores} maiores de idade.')
print(f'Ao todo tivemos {soma_menores} menores de idade.')