print('Numeros Primos!')
primo = int(input('Digite um número inteiro: '))
tot = 0
for c in range (1, primo + 1):
    if primo % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(primo, tot))
if tot == 2:
    print('Esse Número é PRIMO!!!')
else:
    print('Esse número não é PRIMO!!!')