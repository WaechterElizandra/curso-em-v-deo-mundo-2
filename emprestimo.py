#escreva um programa para aprovar o emprestimo bancário para comprar uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
valor_casa = float(input('Informe o valor da casa em R$: '))
salario =float(input('Informe a renda do comprador em R$: '))
parcelas = int(input('Informe em quantos anos a casa será paga: '))
valor_parcelas = valor_casa / (parcelas * 12)
if valor_parcelas > salario * 30 / 100:
    print('\033[1;31mEmpréstimo Negado! O valor da parcela excede 30 % do seu salário!\033[m')
else:
    print('\033[1;34mEmpréstimo concedido\033[m')

print('O valor da parcela será de {}{:.2f}{}'.format('\033[1;32m',valor_parcelas,'\033[m'))