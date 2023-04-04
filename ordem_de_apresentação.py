#O mesmo professor quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro e mostre a ordem sorteada
from random import shuffle

aluno1 = str(input('Escreva o nome do aluno: '))
aluno2 = str(input('Escreva o nome do aluno: '))
aluno3 = str(input('Escreva o nome do aluno: '))
aluno4 = str(input('Escreva o nome do aluno: '))
ordem = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem)# shuffle embarralha a ordem
print('\033[1mA ordem de apresentação será:',ordem)
