import random

vitorias = 0

while True:
    escolha  = input("Você quer impar ou par [i/p]")
    if escolha not in ['i', 'p']:
        print('Escolha invalida, Tente novamente!')
        continue

    numero_meu = int(input('Digite um numero de 1 a 10: '))
    numero_computador = random.randint(1, 10)

    soma = numero_meu + numero_computador
    resultado = "par" if soma % 2 == 0 else "impar"

    print(f"Você escolheu {numero_meu} e o computador escolhou {numero_computador} ")
    print(f"A soma é {soma}, que é {resultado}")

    if(resultado == "par" and escolha == 'p') or (resultado == "impar" and escolha == 'i'):
        print('Você venceu!!')
        vitorias += 1
    else:
        print('O computador venceu!')
        break
print(f'Fim do jogo! Você teve um total de {vitorias} vitoria(s)')