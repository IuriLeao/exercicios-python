ano = int(input('Me diga um ano'))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 ==0 ):
    print('Seu Ano é bissexto')
else:
    print('Seu ano não é bissexto')