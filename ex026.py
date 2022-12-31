frase = str(input('Digite uma frase: ')).lower().strip()
print('Contêm {} letras a na sua frase'.format(frase.count('a')))
print('Sua primeira letra a aparece na posição {}'.format(frase.find('a') + 1))
print('Sua primeira letra a aparece na posição {}'.format(frase.rfind('a') + 1))
