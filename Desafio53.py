#crie um programa que leia uma frase qualquer e diga se ela é um palindromo desconsiderando os espaços
frase = str(input('Digite uma frase ')).strip()
invertida = frase[::-1]
for i in range(1):
    if invertida == frase:
        print('Você digitou a frase {}, de tras para frente ela fica {}. Portando está frase é um palindromo!'.format(frase,invertida))
    else:
        print('Você digitou a frase {}, de tras para frente ela fica {}. Portando está frase não é um palindromo!'.format(frase,invertida))



