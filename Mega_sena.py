#gerador de numeros da mega sena

#importando sorteador
from random import randint

#declarando variáveis
aposta = set() #lista desordenada que não permite itens duplicados
numeros = 0

#estrutura de repetição. Chamando a biblioteca random
while numeros < 7:
    aposta.add(randint(1,60))
    numeros = len(aposta)

# mostrando números sorteados
print('\033[4;35;40mOs números soretados são {}\033[m'.format(aposta))