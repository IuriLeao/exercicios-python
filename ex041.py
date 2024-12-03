ano = int(input('Em que ano você nasceu? '))
cal1 = 2024 - (ano)
if cal1 <= 9:
    print('Você é mirim')
elif cal1 > 9 and cal1 <= 14:
    print('Você é infantil')
elif cal1 > 14 and cal1 <= 19:
    print('Você é junior')
elif cal1 > 19 and cal1 < 21:
    print('Você é senior')
elif cal1 > 20:
    print('Você é master')
