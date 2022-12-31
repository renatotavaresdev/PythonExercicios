from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(0, 7):
    idade = int(input('Digite o Ano em que Nasceu? '))
    anos = atual - idade
    print('Você tem {} anos'.format(anos))
    if anos >= 21:
        totmaior += 1
        print('Você atingiu a Maioridade!')
    else:
        totmenor += 1
        print('Você não atingiu a maioridade! ')
print('Ao todo tivemos {} maior de idade e {} menor de idade'.format(totmaior, totmenor))
