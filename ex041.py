print('Classificando Atletas')
n1 = int(input('Em que ano você nasceu: '))
at = 2022
ano = at - n1
if ano < 9:
    print('Sua Categoria é MIRIM, pois você tem {} anos'.format(ano))
elif ano == 10 or ano == 11 or ano == 12 or ano == 13 or ano == 14:
    print('Sua Categoria é INFANTIL, pois você tem {} anos'.format(ano))
elif ano == 15 or ano == 16 or ano == 17 or ano == 18 or ano == 19:
    print('Sua Categoria é JUNIOR, pois você tem {} anos'.format(ano))
elif ano == 20:
    print('Sua Categoria é SENIOR, pois você tem {} anos'.format(ano))
else:
    print('Sua Categoria é MASTER, pois você tem {} anos'.format(ano))
