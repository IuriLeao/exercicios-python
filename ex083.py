expressao = input('Digite sua expressão: ')

if expressao.count('(') == expressao.count(')'):
    saldo = 0
    for char in expressao:
        if char == '(':
            saldo += 1
        elif char == ')':
            saldo -= 1
        if saldo < 0:
            print('Sua expressão está invalida! ')
            break
        else:
            if saldo == 0:
                print('Sua expressão está valida! ')
else:
    print('Sua expressão está invalida')