from abc import ABC, abstractmethod

class Conta(ABC):
    """
    Classe abstrata que representa uma conta bancária.
    
    Parâmetros:
        numero: Número da conta.
        titular: Nome do titular da conta.
        saldo: Saldo inicial da conta.
    """
    def __init__(self, numero, titular, saldo=0):
        """
        Inicializa uma conta bancária.
        
        Parâmetros:
            numero: Número da conta.
            titular: Nome do titular da conta.
            saldo: Saldo inicial da conta.
        """
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        """
        Realiza um saque na conta bancária.
        
        Parâmetros:
            valor: Valor a ser sacado.
        """
        pass

    @abstractmethod
    def depositar(self, valor):
        """
        Realiza um depósito na conta bancária.
        
        Parâmetros:
            valor: Valor a ser depositado.
        """
        pass

class ContaCorrente(Conta):
    """
    Classe que representa uma conta corrente.
    
    Parâmetros:
        numero: Número da conta.
        titular: Nome do titular da conta.
        saldo: Saldo inicial da conta.
    """
    def __init__(self, numero, titular, saldo=0):
        """
        Inicializa uma conta corrente.
        
        Parâmetros:
            numero: Número da conta.
            titular: Nome do titular da conta.
            saldo: Saldo inicial da conta.
        """
        super().__init__(numero, titular, saldo)
        self.limite = 1000  # Limite de crédito para conta corrente

    def sacar(self, valor):
        """
        Realiza um saque na conta corrente, considerando o limite de crédito.
        
        Parâmetros:
            valor: Valor a ser sacado.
        """
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"{self.titular} realizou um saque de R${valor} com sucesso. Saldo atual: R${self.saldo}")
        else:
            print(f"{self.titular} tem saldo insuficiente para realizar o saque.")

    def depositar(self, valor):
        """
        Realiza um depósito na conta corrente.
        
        Parâmetros:
            valor: Valor a ser depositado.
        """
        self.saldo += valor
        print(f"{self.titular} realizou um depósito de R${valor} com sucesso. Saldo atual: R${self.saldo}")

class ContaPoupanca(Conta):
    """
    Classe que representa uma conta poupança.
    
    Parâmetros:
        numero: Número da conta.
        titular: Nome do titular da conta.
        saldo: Saldo inicial da conta.
    """
    def __init__(self, numero, titular, saldo=0):
        """
        Inicializa uma conta poupança.
        
        Parâmetros:
            numero: Número da conta.
            titular: Nome do titular da conta.
            saldo: Saldo inicial da conta.
        """
        super().__init__(numero, titular, saldo)

    def sacar(self, valor):
        """
        Realiza um saque na conta poupança.
        
        Parâmetros:
            valor: Valor a ser sacado.
        """
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"{self.titular} realizou um saque de R${valor} com sucesso. Saldo atual: R${self.saldo}")
        else:
            print(f"{self.titular} tem saldo insuficiente para realizar o saque.")

    def depositar(self, valor):
        """
        Realiza um depósito na conta poupança.
        
        Parâmetros:
            valor: Valor a ser depositado.
        """
        self.saldo += valor
        print(f"{self.titular} realizou um depósito de R${valor} com sucesso. Saldo atual: R${self.saldo}")

class Pessoa(ABC):
    """
    Classe abstrata que representa uma pessoa.
    
    Parâmetros:
        nome: Nome da pessoa.
        idade: Idade da pessoa.
    """
    def __init__(self, nome, idade):
        """
        Inicializa uma pessoa.

        Parâmetros:
            nome: Nome da pessoa.
            idade: Idade da pessoa.
        """
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def apresentar(self):
        """
        Método abstrato para apresentar informações da pessoa.
        """
        pass

class Cliente(Pessoa):
    """
    Classe que representa um cliente do banco.
    
    Parâmetros:
        nome: Nome do cliente.
        idade: Idade do cliente.
        conta: Conta bancária do cliente.
    """
    def __init__(self, nome, idade, conta):
        """
        Inicializa um cliente do banco.

        Parâmetros:
            nome: Nome do cliente.
            idade: Idade do cliente.
            conta: Conta bancária do cliente.
        """
        super().__init__(nome, idade)
        self.conta = conta

    def apresentar(self):
        """
        Apresenta informações do cliente, incluindo nome, idade, número da conta e saldo.
        """
        print(f"Cliente: {self.nome}, Idade: {self.idade}, Conta: {self.conta.numero}, Saldo: R${self.conta.saldo}")

class Banco:
    """
    Classe que representa um banco.
    
    Parâmetros:
        nome: Nome do banco.
    """
    def __init__(self, nome):
        """
        Inicializa um banco.

        Parâmetros:
            nome: Nome do banco.
        """
        self.nome = nome
        self.clientes = []

    def adicionar_cliente(self, cliente):
        """
        Adiciona um cliente ao banco.

        Parâmetros:
            cliente: Cliente a ser adicionado.
        """
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado ao banco {self.nome}.")

    def listar_clientes(self):
        """
        Lista todos os clientes do banco.
        """
        print(f"Clientes do banco {self.nome}:")
        for cliente in self.clientes:
            cliente.apresentar()
    
    def autenticar_cliente(self, numero_conta):
        """
        Autentica um cliente com base no número da conta.

        Parâmetros:
            numero_conta: Número da conta do cliente.

        Retorna:
            O cliente autenticado ou None se não encontrado.
        """
        for cliente in self.clientes:
            if cliente.conta.numero == numero_conta:
                return cliente
        print("Cliente não encontrado.")
        return None

# Exemplo de uso
if __name__ == "__main__":
    banco = Banco("Banco Master")

    conta_corrente = ContaCorrente(123, "João", 500)
    cliente1 = Cliente("João", 30, conta_corrente)
    banco.adicionar_cliente(cliente1)

    conta_poupanca = ContaPoupanca(456, "Maria", 1000)
    cliente2 = Cliente("Maria", 25, conta_poupanca)
    banco.adicionar_cliente(cliente2)
    print()
    banco.listar_clientes()
    print()
    # Testando operações bancárias
    autenticado = banco.autenticar_cliente(123)
    if autenticado:
        autenticado.conta.sacar(200)
        autenticado.conta.depositar(300)
    print()
    autenticado = banco.autenticar_cliente(456)
    if autenticado:
        autenticado.conta.sacar(1500)  # Tentativa de saque maior que o saldo
        autenticado.conta.depositar(500)