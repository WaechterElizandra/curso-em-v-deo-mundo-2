#faça um programa que leia o peso de 5 pesssoas. No final mostre qual foi o maior e qual foi o menor lidos
maior = 0
menor = 0
for c in range (5):
    peso = float(input('Informe o peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {} e o menor peso é {}'.format(maior, menor))