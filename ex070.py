maior = 0
total = 0
menor = float("inf")
nome_barato = ""
while True:
    nome = str(input('Qual nome do produto? '))
    preco = float(input('Qual preço? '))
    total += preco

    if preco > 1000:
        maior += 1

    if preco < menor:
        menor = preco
        nome_barato = nome
    barato = menor < preco
    continuar = input('Você quer continuar? [S / N]').upper().strip()
    if continuar == 'N':
        break

print(f'Total gasto foi R$ {total:.2f}')
print(f'Total de produtos com valor maior que mil foram {maior}')
print(f'O produto mais barato foi "{nome_barato}" com o preço de R$ {menor:.2f}')


