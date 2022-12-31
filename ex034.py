print('Aumento de Salário')
sal = float(input('Me diga o seu Salário R$ '))
print('Vamos Calcular o Aumento!')
if sal <= 1250:
    aumento1 = sal + (sal * 15 / 100)
    print('O Seu salário era de R${} e teve aumento de 15% sendo agora de R${}'.format(sal, aumento1))
else:
    aumento2 = sal + (sal * 10 / 100)
    print('O Seu salário era de R${} e teve aumento de 10% sendo agora de R${}'.format(sal, aumento2))