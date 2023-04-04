#crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado
print('-=-'*20)
nome = input('Digite o seu nome: ').upper()
print('-=-'*20)
print('\033[1;32mOlá {}'.format(nome),'! Você acaba de fazer seu primeiro script python!\033[m')
print('-=-'*20)
print('\033[7mBem vinda ao curso de Engenharia de Computação!!\033[m')
print('-=-'*20)