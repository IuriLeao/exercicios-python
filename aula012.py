nome = str(input('Qual é seu nome? '))
if nome =='gustavo':
    print('que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no brasil')
elif nome in 'ana claudia jessica juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}')
