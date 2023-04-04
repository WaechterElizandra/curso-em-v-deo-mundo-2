#escreva um programa que faça o computaddor pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número pensado pelo computador. o programa deverá escrever se o usuário perdeu ou ganhou.
from  random import randint
from time import sleep #biblioteca faz um delay no programa
print('\033[1;31m-\033[m'*70)
print('ESTOU PENSANDO EM UM NÚMERO DE 0 A 5. VOCÊ PODE ADIVINHAR!')
print('\033[1;31m-\033[m'*70)
num = randint(0,5) #faz o pc sortear um número
escolha = int(input('Escollha um número de 0 a 5: ')) #usuário tenta adivinhar o número
print('\033[1;32m-\033[m'*70)
print('PROCESSANDO...')
print('\033[1;32m-\033[m'*70)
sleep(2)
if num == escolha:
    print('PARABÉNS VOCÊ ACERTOU A ESCOLHA DO COMPUTADOR!!')
else:
    print('A ESCOLHA DO COMPUTUTADOR FOI {} E VOCÊ ERROU!! TENTE NOVAMENTE'.format(num))
print('OBRIGADA POR PARTICIPAR!')