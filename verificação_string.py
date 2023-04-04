# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('\033[1;31mQual é o nome da sua cidade?\033[m ')).strip()
print(cidade[:5].upper() == 'SANTO')