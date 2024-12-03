n1 = int(input('Qual o primeiro numero? '))
n2 = int(input('Qual o segundo valor?'))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O Segundo valor é maior')
elif n1 == n2:
    print('Não existe valor maior, São iguais')