print('Alistamento')
ano = int(input('Em que ano você nasceu? '))
at = 2022
alist = at - ano
n1 = alist - 18
n2 = 18 - alist
print('Você tem {} anos!'.format(alist))
if alist == 18:
    print('Você Precisa se Alistar!')
elif alist < 18:
    print('Faltam {} anos para você se Alistar'.format(n2))
else:
    print('Você está atrasado em {} anos'.format(n1))