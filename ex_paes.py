vestoque = int(input('Informe itens em estoque: '))
i = 1
x = int(input('Quantos pães  você deseja? '))
for i in range(1, x + 1):
    if i > vestoque:
        print('Só temos {} unidades de pães disponíveis '.format(vestoque))
        break

    if i == x:
        print('Compra efetuada. Obrigado!')