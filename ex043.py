peso = float(input('Qual Seu peso? '))
altura = float(input('Qual é sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Abaixo do peso, Seu imc é {imc:.1f}')
elif imc >= 18.5 and imc <= 25.0:
    print(f'Peso ideal, Seu imc é de {imc:.1f}')
elif imc > 25.0 and imc <= 30.0:
    print(f'Você está sobrepeso, Seu imc é de {imc:.1f}')
elif imc > 30 and imc <= 40:
    print(f'Você tem obesidade, Seu imc é de {imc:.1f}')
elif imc > 40:
    print(f'Você tem obesidade morbida, Seu imc é de {imc:.1f}')

