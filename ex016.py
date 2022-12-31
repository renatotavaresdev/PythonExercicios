import math
print('Numero real para inteiro')
num = float(input('Me diga um numero real para saber o seu numero inteiro: '))
interito = math.trunc(num)
print('O número escolhido foi {:.3f} e sua parte inteira é {}'.format(num, interito))
