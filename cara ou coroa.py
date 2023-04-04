import getpass

# função para criar um novo usuário
def criar_usuario():
    nome = input("Digite seu nome: ")
    senha = getpass.getpass("Digite uma senha segura: ")
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome}:{senha}\n")
    print("Usuário criado com sucesso!")

# função para fazer o login
def fazer_login():
    nome = input("Digite seu nome de usuário: ")
    senha = getpass.getpass("Digite sua senha: ")
    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()
        for usuario in usuarios:
            nome_usuario, senha_usuario = usuario.strip().split(":")
            if nome_usuario == nome and senha_usuario == senha:
                print("Login bem-sucedido!")
                return
    print("Nome de usuário ou senha incorretos.")

# menu principal
while True:
    opcao = input("Digite 1 para criar um novo usuário, 2 para fazer login ou 3 para sair: ")
    if opcao == "1":
        criar_usuario()
    elif opcao == "2":
        fazer_login()
    elif opcao == "3":
        print("Obrigado por usar nosso app!")
        break
    else:
        print("Opção inválida. Tente novamente.")
