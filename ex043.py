print('Calculando IMC')
peso = float(input('Quantos Kg você pesa: '))
alt = float(input('Qual a sua altura: '))
imc = peso / (alt * alt)
print('o Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está Abaixo do Peso')
elif imc > 18.5 and imc <= 25:
    print('Você está no Peso Ideal')
elif imc > 25.1 and imc <= 30:
    print('Você está com Sobrepeso')
elif imc > 30.1 and imc <= 40:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade Mórbida')