#date importa a data atual da máquina
from datetime import date
ano = int(input('Digite um ano: (Coloque 0 para analisar o ano atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4==0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é {}Bissexto{}!'.format(ano,'\033[7m','\033[m'))
else:
    print('O ano {} não é {}Bissexto{}!'.format(ano,'\033[7m','\033[m'))