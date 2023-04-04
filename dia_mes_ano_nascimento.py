#crie um script que leia o dia, o mes e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada
from time import sleep
print('=+='*30)
nome = input('Digete seu nome: ').upper()
print('=+='*30)
dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')
print('\033[1;31mOlá {}! Estamos analisando os seus dados!!\033[m'.format(nome))
sleep(3)
print('\033[1;34mOlá',nome,'!Você nasceu no dia ',dia,'do mês ',mes, 'do ano de',ano,'\033[m')
print('=+='*30)