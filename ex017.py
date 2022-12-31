import math
print('Calculando a Hipotenusa')
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hyp = math.hypot(co, ca)
print('O Cateto Oposto vale {} o Adjacente {} e sua Hypotenusa vale {:.2f}'.format(co, ca, hyp))