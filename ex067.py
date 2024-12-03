while True:
    n = int(input('Qual Numero Você quer ver a tabuada? '))
    if n < 0:
        print('Programa encerrado!!')
        break
    for i in range(1, 11):
        resultado = n * i
        print(f'{n} x {i} = {resultado}')