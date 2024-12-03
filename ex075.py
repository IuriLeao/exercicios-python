soma = 0

n1 = int(input('Digete o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
tupla = (n1, n2, n3, n4)

print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    posiçao = tupla.index(3)+1
    print(f'O valor 3 apareceu na posição {posiçao}')
else:
    print('0 numero 3 não foi digitado')

pares = [num for num in tupla if num % 2 == 0]
print(F'Os numeros pares foram {pares}')