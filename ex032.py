import calendar
ano = int(input('Me diga um ano para saber se é Bissexto ou não: '))
if (calendar.isleap(ano)):
    print('Esse Ano de {} é Bissexto'.format(ano))
else:
    print('Esse ano de {} não é Bissexto!'.format(ano))
