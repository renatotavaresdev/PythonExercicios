import random
print('Sorteando o Aluno')
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print('A ordem de apresentação será: ')
print(alunos)