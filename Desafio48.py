# faça um programa que que calcule a soma entre todos os números ímpares que são multiplos de 3 e que se necontram no intervalo de 1 a 500
soma = 0
contador = 0
for c in range(1,501):
    if c % 2 == 1:
        if c %3 == 0:
            soma += c
            contador +=  1
print('A soma dos {} números é igual a {}'.format(contador,soma))