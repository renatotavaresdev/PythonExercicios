from random import randint
import time
print('Jokenpô')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções: 
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('Jo...')
time.sleep(2)
print('Ken...')
time.sleep(2)
print('Pô!!!')
time.sleep(2)
print('-=' * 20)
print('O Computador escolheu {}'.format(itens[computador]))
print('O Jogador escolheu {}'.format(itens[jogador]))
print('-=' * 20)
if computador == 0: #Pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('O Jogador Venceu! Parabéns')
    elif jogador == 2:
        print('O Computador Venceu! Que Pena')
    else:
        print('Jogada Inválida')
elif computador == 1: #Papel
    if jogador == 0:
        print('O Computador Venceu! Que Pena')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('O Jogador Venceu! Parabéns')
    else:
        print('Jogada Inválida')
elif computador == 2: # Tesoura
    if jogador == 0:
        print('O Jogador Venceu! Parabéns')
    elif jogador == 1:
        print('O Computador Venceu! Que Pena')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada Inválida')