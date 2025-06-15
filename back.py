class Banco:
    def __init__(self, usuario):
        self.usuario = usuario
        self.extrato = ''
        self.funds = 0.00
        self.MAX_WITHDRAW = 3
        self.ACTUAL_WITHDRAW = 0

    def validar_senha(self):
        senha = input(f"Digite a senha do usuário '{self.usuario.nome}': ")
        if senha == self.usuario.senha:
            return True
        else:
            print("Senha incorreta! Operação cancelada.")
            return False

    def depositar(self, valor):
        if self.validar_senha():
            if valor > 0:
                self.funds += valor
                self.extrato += f"Depósito: R${valor:.2f}\n"
                print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            else:
                print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.validar_senha():
            if valor > self.funds:
                print("Saldo insuficiente.")
            elif self.ACTUAL_WITHDRAW >= self.MAX_WITHDRAW:
                print("Limite diário de saques atingido.")
            elif valor <= 0:
                print("Valor inválido para saque.")
            else:
                self.funds -= valor
                self.extrato += f"Saque: R${valor:.2f}\n"
                self.ACTUAL_WITHDRAW += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def ver_extrato(self):
        if self.validar_senha():
            print(f"\nExtrato de {self.usuario.nome}")
            print(self.extrato if self.extrato else "Sem movimentações.")
            print(f"Saldo atual: R${self.funds:.2f}")

    def usar_menu(self):
        while True:
            print("\n1 - Depositar")
            print("2 - Sacar")
            print("3 - Ver Extrato")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                valor = float(input("Valor do depósito: "))
                self.depositar(valor)
            elif opcao == '2':
                valor = float(input("Valor do saque: "))
                self.sacar(valor)
            elif opcao == '3':
                self.ver_extrato()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
