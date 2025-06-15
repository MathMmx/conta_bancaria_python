class Banco:
    def __init__(self):    
        self.extrato = ''
        self.funds = 0.00
        self.MAX_WITHDRAW = 3
        self.ACTUAL_WITHDRAW = 0
        self.MAX_WITHDRAW_VALUES = 500
        self.menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        """

    def depositar(self):
        try: 
            valor = float(input("Digite quanto gostaria de depositar: "))
            if valor <= 0:
                print("O valor precisa ser positivo.")
                return
            self.funds += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n" 
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        except ValueError:
            print("Por favor, insira um valor numérico válido!")

    def sacar(self):
        try:
            if self.ACTUAL_WITHDRAW >= self.MAX_WITHDRAW:
                print("Limite diário de saques atingido!")
                return

            valor = float(input(f'Digite quanto gostaria de sacar (Máximo por saque: R${self.MAX_WITHDRAW_VALUES:.2f}, você ainda tem {self.MAX_WITHDRAW - self.ACTUAL_WITHDRAW} saques restantes): '))
            
            if valor <= 0:
                print("O valor precisa ser positivo.")
                return
            if valor > self.MAX_WITHDRAW_VALUES:
                print(f'Valor maior que o permitido por saque (R${self.MAX_WITHDRAW_VALUES:.2f}).')
                return
            if valor > self.funds:
                print("Saldo insuficiente.")
                return

            self.funds -= valor
            self.extrato += f'Saque: R${valor:.2f}\n'
            self.ACTUAL_WITHDRAW += 1
            print(f'Saque de R${valor:.2f} realizado com sucesso!')
        except ValueError:
            print("Por favor, insira um valor numérico válido!")

    def ver_extrato(self):
        print("\n======= EXTRATO =======")
        print(self.extrato if self.extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo atual: R${self.funds:.2f}")
        print("=======================\n")

    def usar_menu(self):
        while True:
            opcao = input(self.menu).lower()

            if opcao == 'd':
                self.depositar()
            elif opcao == 's':
                self.sacar()
            elif opcao == 'e':
                self.ver_extrato()
            elif opcao == 'q':
                print("Saindo... Obrigado por usar nosso banco!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma das opções do menu.")
