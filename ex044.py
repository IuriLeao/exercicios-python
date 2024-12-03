preco = float(input('Qual preço do produto? '))
cnd = str(input('Qual a forma de pagamento? (dinheiro/cheque/cartão a vista/cartão 2x/cartão 3x)')).strip().lower()
if cnd in ["dinheiro", "cheque"]:
    desconto = (10/100) * preco
    print(f'o desconto de 10% é de {desconto:.2f}')
elif cnd in ["cartão a vista"]:
    desconto = (5/100) * preco
    print(f'O desconto de 5% foi de `{desconto:.2f}')
elif cnd in ["cartão 2x"]:
    print('O preço continuara o mesmo')
elif cnd in ["cartão 3x"]:
    aumento = ((30/100) +1) * (preco)
    print(f'O preço com 30% a mais ficara de {aumento}')
else:
    print('Forma de pagamento invalida')




