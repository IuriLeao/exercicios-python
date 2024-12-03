soma_idade = 0
maior_idade = 0
homens = 0
mulheres = 0
menor20 = 0

while True:
    idade = int(input('Fale uma idade: '))
    if idade < 0:
        print('Idade inválida. Tente novamente.')
        continue
    if idade > 18:
        maior_idade += 1

    sexo = input('Fale um sexo: [F / M] ').upper().strip()
    if sexo not in ('F', 'M'):
        print('Sexo inválido. Tente novamente.')
        continue

    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        mulheres += 1
        if idade < 20:
            menor20 += 1

    continuar = input('Quer continuar? [S / N] ').upper().strip()
    if continuar == 'N':
        break

print(f'Total de maiores de 18 anos: {maior_idade}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres cadastradas: {mulheres}')
print(f'Total de mulheres com menos de 20 anos: {menor20}')