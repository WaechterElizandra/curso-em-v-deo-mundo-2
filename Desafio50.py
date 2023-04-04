#desenvolva um programa que leia 6 números inteiros e mostre a soma somente daqueles que forem par, se o valor digitado for
# ímpar apenas o desconsidere
soma = 0
cont = 0
for c in range (6):
    n = int(input('Digite o {}º número: '.format(c+1)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números pares e a soma deles é igual a {}'.format(cont,soma))
