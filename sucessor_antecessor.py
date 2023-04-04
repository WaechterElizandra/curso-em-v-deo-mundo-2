#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n1 = int(input('\033[7;32mDigite um número: '))
print('O antecessor de {} é {} e o sucessor de {} é {}'.format(n1, n1 - 1, n1, n1 + 1))