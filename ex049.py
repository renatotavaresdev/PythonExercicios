num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('A tabuada de {} x {} = {}'.format(num, c, num*c))