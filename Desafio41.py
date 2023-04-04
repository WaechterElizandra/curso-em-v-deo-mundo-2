#a confederação internacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria de acordo co a idede
#Até 9 anos= mirim até 14anos= infantil Até 19 anos= junior Até 20= sênior acima de 20=master
from datetime import date
nascimento = int(input('Informe o ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print('O atleta tem {} anos. '.format(idade))
    print('Categoria mirim')
elif idade <= 14:
    print('O atleta tem {} anos. '.format(idade))
    print('Categoria infantil!')
elif idade <= 19:
    print('O atleta tem {} anos. '.format(idade))
    print('Caregoria júnior')
elif idade < 25:
    print('O atleta tem {} anos. '.format(idade))
    print('Categoria sênior!')
else:
    print('O atleta tem {} anos. '.format(idade))
    print('Categoria master!')
# pode usar a biblioteca datetime import date para calcular o ano atual