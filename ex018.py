import math
print('Seno, Cosseno e Tanjente')
ang = float(input('Me diga o valor do Ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('o Seno vale {:.2f}, Cosseno {:.2f} e a Tanjente {:.2f}'.format(sen, cos, tan))