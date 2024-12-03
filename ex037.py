n1 = int(input('Me diga um numero'))
print('''Escolha umas das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção:  '))
if opção == 1:
    print(f'{n1} convertido para binario é igual a {bin(n1)[2:]}')
elif opção == 2:
    print(f'{n1} convertido para OCTAL é igual a {oct(n1)[2:]}')
elif opção == 3:
    print(f'{n1} convertido para HEXADECIMAL é igual a {hex(n1)[2:]}')
else:
    print('Opção invalida. Tente novamente!')
