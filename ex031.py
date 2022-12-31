print('Calculo de Viagem')
dist = float(input('Me Diga a Distância em KM da viagem: '))
print('Vamos Calcular o valor!')
if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print('O Valor da sua viagem é de {:.2f}'.format(preço))