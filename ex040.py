print('Média Final')
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
med = (n1 + n2) / 2
if med < 5.1:
    print('Sua média foi {} e você está REPROVADO!'.format(med))
elif med > 7.0:
    print('Sua média foi {} e você está APROVADO!'.format(med))
else:
    print('Sua média foi {} e você está de RECUPERAÇÃO!'.format(med))