times = 'botafogo', 'palmeiras', 'fortaleza', 'flamengo', 'internacional', 'sao paulo', 'cruzeiro', 'bahia', 'corinthians', 'vasco da gama', 'atletico-MG', 'EC vitoria', 'gremio', 'Atletico-PR', 'Juventude', 'Fluminense', 'Criciuma', 'bragantino', 'cuiaba', 'Atletico-Go'

print(f'Os Primeiros 5 São {times[0:5]}')

print(f'Os ultimos 4 são {times[-4:]}')

times_sorted = tuple(sorted(times)) # ordena e converte de volta para tupla

print(f'Os time em ordem alfabetica são {times_sorted}')

posição = times.index('corinthians') # pega o indice do time 'corithians'

print(f'O Corithians está na posição {posição} ')