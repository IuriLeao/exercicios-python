casa = float(input('Qual Valor da casa? '))
salario = float(input('Qual o valor do seu salario? '))
anos = float(input('Em quantos anos você quer pagar? '))
c_anos = (anos)*12
c_casa = casa/(c_anos)
if c_casa >  30 / 100 * salario:
    print('Seu emprestimo foi negado, Tente um valor mais baixo')
    print(f'Você iria pagar {c_casa:.0f} em {c_anos:.0f} meses, Iria ultrapassar 30% do seu salario!!')
else:
    print('Seu Emprestimo foi aprovado, Parabens!')
    print(f'O valor da sua mensalidade será de {c_casa:.0f} e será paga em {c_anos:.0f} meses')



