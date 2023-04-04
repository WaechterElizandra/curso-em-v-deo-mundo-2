#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Valor do produto:R$ {}'.format('\033[1m')))
npreco = preco - preco * 5/100
print('Preço do produto {}'.format(preco))
print('Valor do desconto {:.2f}'.format(preco * 5 / 100))
print('Total a pagar {:.2f}'.format(npreco))