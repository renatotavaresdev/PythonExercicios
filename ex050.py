print('Soma de 6 numeros sendo apenas pares!')
soma = 0
for c in range(1, 7):
    n1 = int(input('Me diga um valor: '))
    if n1 % 2 == 0:
        soma += n1
print('A Soma dos números pares são iguais a {}'.format(soma))
