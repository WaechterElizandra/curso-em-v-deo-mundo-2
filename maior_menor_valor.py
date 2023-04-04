#escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
#O primeiro valor é maior
# O segundo valor é maior
#Não existe valor maior os dois são iguais
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro número é maior!')
elif n1 < n2:
    print('O segundo número é o maior!')
else:
    print('Não existe valor maior. Os dois são iguais!')