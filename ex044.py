print('Gerenciador de Pagamentos')
val = float(input('Digite o Valor do Produto R$ '))
print('As Formas de Pagamento que temos são: \n 1)À vista com 10% de Desconto \n 2)À vista no cartão 5% de Desconto \n 3)Em 2x no Cartão sem Juros \n 4)Em 3x ou Mais com 20% de Juros')
sel = int(input('Selecione a forma de Pagamento: '))
n1 = val - (val * (10/100))
n2 = val - (val * (5/100))
n3 = val / 2
n4 = val + (val * (20/100))
if sel == 1:
    print('O valor do seu pagamento à vista com 10% de Desconto é R$ {:.2f}'.format(n1))
elif sel == 2:
    print('O Valor do seu pagamento com cartão a vista é de R$ {:.2f}'.format(n2))
elif sel == 3:
    print('O Valor das suas parcelas sem juros é de R$ {:.2f}'.format(n3))
elif sel == 4:
    print('O Valor em 3x ou Mais com Juros é de R$ {:.2f}'.format(n4))
else:
    print('Selecione uma operação válida!')
    