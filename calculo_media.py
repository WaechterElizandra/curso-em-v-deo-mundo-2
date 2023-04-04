#Desenvolva um program que leia as duas médias de um aluno, calcule e mostre a sua média
nota1 = float(input('{}Informe a 1ª nota: {}'.format('\033[31m','\033[m')))
nota2 = float(input('{}Informe a segunda nota: {}'.format('\033[33m','\033[m')))
print('A média do aluno é {}{}{}'.format('\033[1;30m',(nota1+nota2)/2,'\033[m'))
