#desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final mostre os 10 primeiros termos dessa PA
print(' '*10,'10 TERMOS DE UMA PA')
print('*' *20)
primeiro = int(input('Digite um número: '))
razao = int(input('Digite uma razão para a PA: '))
decimo = primeiro + (11 - 1) *razao
for c in range (primeiro,decimo, razao):
    print(c, end= '-> ')
print('ACABOU')