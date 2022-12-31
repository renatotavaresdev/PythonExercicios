print('Menor e Maior Numero')
n1 = int(input('Me diga o Primeiro Número: '))
n2 = int(input('Me dia o Segundo Número: '))
n3 = int(input('Me Diga o Terceiro Número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O Menor Valor Digitado foi {} e o Maior {}'.format(menor, maior))