nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('\033[1mOlá! Seu primeiro nome é {}\033[m'.format(n[0]))
print('\033[7mSeu último nome é {}\033[m'.format(n[len(n)-1]))