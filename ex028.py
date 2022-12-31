import random
import time
print('Jogo da Advinhação')
print('Irei pensar em um número entre 0 e 5')
print('Estou Pensando...')
time.sleep(3)
print('Já tenho o meu número!')
time.sleep(2)
n = random.randint(1, 5)
print('Agora é sua Vez....')
time.sleep(2)
num = int(input('Me Diga um numero entre 0 e 5 para saber se combinamos! '))
if n == num:
    print('PARABÉNS!!! Você Acertou!!')
else:
    print('Infelizmente o Computador Ganhou!!!')
print('--Fim do Jogo--')
