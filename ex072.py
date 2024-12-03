numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ,19 , 20)
numeroletra = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

per = int(input('Fale um numero de 0 a 20: '))

while per not in range(21):
    per = int(input('O valor inserido foi invalido!! Fale um numero de 0 a 20: '))

#puxa o numero em ralação a outra tupla
print(f'O numero falado foi {per} e se chama {numeroletra[per]}.')




