print('Olha o Radar!')
vel = int(input('Qual a velocidade o veículo passou? '))
if vel > 80:
    print('Você Ultrapassou a velocidade e foi multado!!')
    multa = (vel - 80) * 7
    print('O Valor da Multa foi de R$ {}'.format(multa))
else:
    print('Sua Velocidade está normal!')