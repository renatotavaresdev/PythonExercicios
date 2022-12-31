print('Calculo Aluguel de Carro')
dia = int(input('Diga quantos dias você ficou com o carro: '))
km = float(input('Quantos Km você percorreu? '))
d = dia * 60
dist = km * 0.15
print('O Preço pago pelos dias foi {}, o preço pago por Km foi {}, a soma dos dois é de {}'.format(d, dist, (d+dist)))