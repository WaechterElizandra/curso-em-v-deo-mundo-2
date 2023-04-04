#elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e a condição de pagamento:
#'A vista dinheiro ou cheque 10% de desconto'
#A vista no cartão 5% de desconto
#em  até duas vezes no cartão preço normal
#3x ou mais 20% de juros
produto = float(input('Informe o valor das compras: '))
pagamento = int(input('''Digite o nª conforme a forma de pagamento: 
[1](1x dinheiro ou cheque) 
[2](1x no cartão) 
[3](até 2x) 
[4](3x ou mais): '''))
if pagamento == 1:
    print('Desconto de 10%')
    print('Total a pagar {}'.format(produto - (produto * (10 / 100))))
elif pagamento == 2:
    print('Desconto de 5%')
    print('Total a pagar: {}'.format(produto - (produto * (5 / 100))))
elif pagamento == 3:
    print('Parcelas de {}'.format(produto/2))
    print('Total  a pagar: {}'.format(produto))
elif pagamento == 4:
    parcelas = int(input('Quantaas vezes deseja pagar? '))
    print('Juros de 20%')
    print('A parcela será de {}'.format((produto + (produto * (20 / 100)))/parcelas))
    print('Total a pagar: {}'.format((produto + (produto * (20 / 100)))))
print('AGRADECEMOS A PREFERÊNCIA!')