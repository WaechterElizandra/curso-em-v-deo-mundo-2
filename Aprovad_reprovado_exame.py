#faça um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final de acordo com a média atingida:]
#abaixo de 5 Reprovado, 5 e 6.9 recuperação acima de 7.0 aprovado
nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Média = {}. \033[1;31mALUNO REPROVADO!\033[m'.format(media))
elif media <= 6.9:
    print('Média = {}. \033[1;33mALUNO EM RECUPERAÇÃO!\033[m'.format(media))
elif media >= 7:
    print('Média = {}. \033[1;32mALUNO APROVADO!\033[m'.format(media))