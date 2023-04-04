#criando lista
moradores = []

#variáveis


#coletando e armazenado informações do usuário
while True:
    elevador = input("Qual elevador você utiliza com mais frequência? (A, B ou C): ").upper()
    periodo = input("Em qual período você costuma utilizar o elevador? (M = Matutino, V = Vespertino, N = Noturno): ").upper()

    if elevador not in ["A", "B", "C"] or periodo not in ["M", "V", "N"]:
        print("Valores inválidos. Tente novamente.")
        continue

    morador = {"elevador": elevador, "periodo": periodo}
    moradores.append(morador)

    continuar = input("Deseja continuar coletando informações? (S/N): ").upper()
    if continuar == "N":
        break
print(moradores)