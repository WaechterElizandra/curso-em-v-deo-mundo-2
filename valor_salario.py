#Faça um programa que pergunte o salário de um funcionário calcule o valor do seu aumento. Para slários acima de 1250,00 calcule um aumento de
# 10% para inferiores ou iguais o aumento é de 15%
salario = float(input('\033[4mInforme seu salário em R$: \033[m'))
if salario > 1250.0:
    print('Salário com aumento: {:.2f}'.format(salario +(salario * 10/100)))
else:
    print('O salário com aumento: {:.2f}'.format(salario + (salario * 15/100)))