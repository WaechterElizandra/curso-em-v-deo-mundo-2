#faça um programa que faça o pc jogar jokenpô com vc
import random
from time import sleep
print('=+' * 25)
print('\033[1;35mVamos jogar JOKENPÔ?\033[m')
print('\033[1;32mSerá que você pode me vencer?\033[m')
print('=+' * 25)
#informando as opções do jogo
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
#sorteando uma das opçoes
pc = random.choice(opcoes)

#recebendo informações do usuário
escolha = str(input('Escolha: Pedra, Papel Tesoura ')).upper()
print('=+' * 25)
print('\033[1;35mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ\033[m')
print('=+' * 25)
#casos onde a pedra ganha
if escolha == 'PEDRA' and pc == 'TESOURA':
    print('Você escolheu {} e eu escolhi {}. Você Ganhou! '.format(escolha,pc))
elif escolha == 'TESOURA' and pc == 'PEDRA':
    print('Você escolheu {} e eu escolhi {}. Você Perdeu! '.format(escolha,pc))
    print('Tente novamente!')
#casos onde a tesoura ganha
elif escolha == 'TESOURA' and pc == 'PAPEL':
    print('Você escolheu {} e eu escolhi {}. Você Ganhou! '.format(escolha, pc))
elif escolha == 'PAPEL' and pc == 'TESOURA':
    print('Você escolheu {} e eu escolhi {}. Você Perdeu! '.format(escolha, pc))
    print('Tente novamente!')
#casos onde o papel ganha
elif escolha == 'PAPEL' and pc == 'PEDRA':
    print('Você escolheu {} e eu escolhi {}. Você Ganhou! '.format(escolha, pc))
elif escolha == 'PEDRA' and pc == 'PAPEL':
    print('Você escolheu {} e eu escolhi {}. Você Perdeu! '.format(escolha, pc))
    print('Tente novamente!')
#caso de empate
elif escolha == pc:
    print('Você escolheu {} e eu escolhi {}. Nós Empatamos! '.format(escolha, pc))
else:
    print('Essa opção não faz parte do jogo!')