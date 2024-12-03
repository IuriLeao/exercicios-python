pr = str(input("Qual Seu nome")).upper().strip()
print ('A letra A aparece {} vezes na frase'.format(pr.count('A')))
print ('A primeira letra A apareceu na posição{}'.format(pr.find('A')+1))
print ('A ultima letra A apareceu na posição {}'.format(pr.rfind('A')+1))
