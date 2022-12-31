print('Palindromos')
frase = str(input('Escreva uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if inverso == junto:
    print('Sua Frase é um Palindromo!')
else:
    print('Sua Frase não é um Palindromo!')