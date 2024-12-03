valores = list()
par = list()
impar = list()

while True:
    n = int(input('Digite Um valor: '))
    valores.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    continuar = input('Você deseja continuar? [Sim / Não] ').strip().capitalize()
    if continuar in ['S', 'N', 'Sim', 'Não', 'Nao']:
        if continuar in ['N', 'Não', 'Nao']:
            break
    else:
        print('Entrada invalida, Digite apenas Sim(S) ou Não(N)')
        
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
