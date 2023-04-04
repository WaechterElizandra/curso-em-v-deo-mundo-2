#descobrir a operadora do número de telefone
import phonenumbers
from phonenumbers import carrier

#digite seu número com código do país e ddd
phoneNumber = phonenumbers.parse(input('Informe o úmero de telefone'))

#captura operadora
operadora = carrier.name_for_number(phoneNumber, 'pt-br')

print('A operadora é: {}'.format(operadora))


