#Um professor que sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e mostrando o nome escolhido
import random
aluno1 = str(input('Escreva o nome do aluno: '))
aluno2 = str(input('Escreva o nome do aluno: '))
aluno3 = str(input('Escreva o nome do aluno: '))
aluno4 = str(input('Escreva o nome do aluno: '))
alunos = [aluno4, aluno3, aluno2, aluno1]
sorteado = random.choice(alunos)
print('\033[33mO aluno que irá apagar o quadro hoje é: ',(sorteado).upper())