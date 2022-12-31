print('Igualando Numeros')
n1 = int(input('Me Diga um Número: '))
n2 = int(input('Me Diga outro Número: '))
if n1 > n2:
    print('O Primeiro numero {} é maior que o segundo {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número {} é maior que o primeiro número {}'.format(n2, n1))
else:
    print('Os números {} e {} são iguais!'.format(n1, n2))