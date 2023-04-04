#desenvola um programa que leia o nome a idade e o sexo de 4 pessoas. no final o programa mostre
#a média de idade do grupo
#o nome do homem mais velho
#quantas mulheres tem menos de 21 anos
somaidade = 0
mediaidade = 0
maioridadehome = 0
nomevelho = ''
totmulher20 = 0
for p in range(4):
    print('-------{} pessoa------'.format(p+1))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = int(input('Infrome o sexo: 1[feminino] ou 2[masculino]'))
    somaidade += idade
    if p == 1 and sexo == 2:
        maioridadehome = idade
        nomevelho = nome
    if sexo == 2 and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo == 1 and idade > 20:
        totmulher20 += 1

mediaidade = somaidade/4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} ano e se chama {}'.format(maioridadehome, nomevelho))
print('{} mulheres são maiores de 20 anos'.format(totmulher20))