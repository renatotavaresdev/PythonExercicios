print('Casas do Numero')
num = int(input('Escolha um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Sua Unidade vale {}'.format(u))
print('Sua Dezena vale {}'.format(d))
print('Sua Centena vale {}'.format(c))
print('Sua Milhar vale {}'.format(m))
