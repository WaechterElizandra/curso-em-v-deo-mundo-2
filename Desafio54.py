#Crie um programa que leia a data de nascimentode sete pessoas. no final mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já são maiores
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range (7):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa '.format(c+1)))
    idade = atual - nascimento
    if idade >= 18:
        maior +=1
    else:
        menor += 1
print('Tivemos {} pessoas maiores e {} pessoas menores'.format(maior,menor))
