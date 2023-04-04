#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas. -
# Quantas letras ao todo (sem considerar espaços).
#  - Quantas letras tem o primeiro nome.
from time import sleep
nome = str(input('Qualé o seu nome? '))
print('PROCESSANDO INFORMAÇÕES...')
sleep(3)
print('_+_'*20)
print('\033[1;34mO seu nome em MAIÚSCULAS é',nome.upper(),'\033[m')
print('\033[1;35mO seu nome em minúsculas é',nome.lower(),'\033[m')
print('\033[1;36mO seu nome sem espaços tem ',len(nome) - nome.count(' '),'letras\033[m')
print('\033[1;37mO seu primeiro nome tem ',nome.find(' '),'letras\033[m')
print('_+_'*20)
