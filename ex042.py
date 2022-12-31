print('Analisando Triangulo 2.0')
print('-=' * 20)
n1 = float(input('Me Diga o primeiro lado: '))
n2 = float(input('Me Diga o segundo lado: '))
n3 = float(input('Me Diga o terceiro lado: '))
print('-=' * 20)
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os Segumentos acima  Podem Formar um Triangulo!' end='')
    if n1 == n2 == n3:
        print('Equilatero!')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os Segmentos Não Podem formar um Triangulo!')