#faça um programa que leia o ano de nascimento de um jovem e informe conforme a sua idade:
#SE ainda vai se alistar no serviço militar
#SE é a hora de se alistar
#SE já passou a tempo de alistamento
#seu programa também deve mostrar quanto tempo falta ou que já passou do alistamento.
nascimento = int(input('Qual o ano do seu nascimento? '))
idade = 2023 - nascimento
tempo_passou = 2005 -nascimento
tempo_falta = nascimento - 2005
if idade < 18:
    print('Você ainda vai se alistar no serviço militar! Em {}{}{} anos você deve se alistar '.format('\033[1;31m',tempo_falta,'\033[m'))
elif idade == 18:
    print('\033[1;34mÉ hora de se alistar!\033[m')
else:
    print('Já passou o tempo do seu alistamento! Você devia ter se alistado {}{}{} anos atrás!'.format('\033[1;31m',tempo_passou,'\033[m'))
# pode usar a biblioteca datetime import date