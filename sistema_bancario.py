from back import Banco
from user import Usuario
def main():
    print("Cadastro de Usuário:")
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")

    usuario = Usuario(nome, senha)
    banco = Banco(usuario)

    banco.usar_menu()

if __name__ == "__main__":
    main()