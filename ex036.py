print('Calculando Empréstimo')
casa = float(input('Qual é o Valor do Imóvel R$ '))
sal = float(input('Quanto você ganha por mês R$ '))
anos = int(input('Em quantos anos quer financiar: '))
parcela = casa / (anos * 12)
minimo = sal * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa, anos, parcela))
if parcela <= minimo:
    print('O Valor do Empréstimo foi Aprovado!')
else:
    print('O Valor excede o seu salário, assim foi Negado o Empréstimo')