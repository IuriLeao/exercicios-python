import random
n1 = (input("Fale o Primeiro nome"))
n2 = (input("Fale o Segundo nome"))
n3 = (input("Fale o terceiro nome"))
n4 = (input("Fale o Quarto nome"))
lista = [n1, n2 ,n3, n4]
escolhido = random.choice(lista)
print(f"O escolhido foi {escolhido}")
