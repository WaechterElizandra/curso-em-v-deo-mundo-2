#faça um algoritmo que leia o salário de uma pessoa e mostre seu novo salário com 15% de aumento
salario = float(input('Informe o salário do servidor: '))
print('\033[1mSalário com aumento: {:.2f}'.format(salario + salario * 15/100))