n1 = int(input('Digite Um valor: '))
n2 = int(input('Digite Outro valor: '))
opcao = 0
while opcao != 5:
    print('''\nO que você deseja fazer com os números:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('Sua opção: '))

    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior é {n1}')
        else:
            print(f'Entre {n1} e {n2}, o maior é {n2}')
    elif opcao == 4:
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro novo valor: '))
    elif opcao == 5:
        print('Programa FINALIZADO!')
    else:
        print('Opção inválida. Tente novamente.')

    # Uma linha em branco para melhorar a visualização
    print()

print('Obrigado por usar o programa!')
