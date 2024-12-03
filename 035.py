n1 = float(input('Primeiro segmento '))
n2 = float(input('Segundo segmento'))
n3 = float(input('Terceiro segmento'))
if (n1+n2 > n3) and (n1+n3 > n2) and (n2 + n3 > n1):
    print ('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os valores assim NÃO PODEM formar triângulo!')
