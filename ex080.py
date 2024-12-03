valores = []
for c in range(0, 5):
    n = int(input('Digte um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(F'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('Os valores digitados em ordem fora {}'.format(valores))


