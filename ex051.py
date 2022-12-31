print('=-'*12)
print('Progressão Aritmética!!!')
print('=-'*12)
primeiro = int(input('Me diga o primeiro termo: '))
razão = int(input('Me Diga da Razão: '))
decimo = primeiro + (10-1) * razão
for c in range(primeiro, decimo, razão):
    print('{}'.format(c), end= ' -> ')
print('Fim!!!')