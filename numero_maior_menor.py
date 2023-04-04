#faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
n1 = float(input('\033[1;36mInforme o 1ºnúmero:\033[m '))
n2 = float(input('\033[1;32mInforme o 2ºnúmero:\033[m '))
n3 = float(input('\033[1;33mInforme o 3ºnúmero:\033[m '))
maior = n1
#verificando o maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
#verficando o menor número
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")