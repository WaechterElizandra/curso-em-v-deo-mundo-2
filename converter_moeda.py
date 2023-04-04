#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar
real = float(input('\033[1;35mQuantos reais você tem na sua carteira?R$: \033[m'))
print('Com esse valor você pode comprar {}{:.2f}{} dólares'.format('\033[1;34m',real/5.27,'\033[m'))