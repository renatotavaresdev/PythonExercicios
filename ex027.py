n = str(input('Qual o seu Nome Completo: ')).strip()
nome = n.split()
print('Muito Prazer em te conhecer!')
print('Seu Primeiro nome é {}'.format(nome[0]))
print('Seu Ultimo nome é {}'.format(nome[len(nome)-1]))
