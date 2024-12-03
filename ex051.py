pt = int(input('Primeiro termo'))
rz = int(input('Me fale a razao'))
decimo = pt + (10-1) * rz
for c in range ((pt), (decimo) + (rz) ,(rz)):
    print('{}'.format(c), end='-> ')
print('ACABOU')


