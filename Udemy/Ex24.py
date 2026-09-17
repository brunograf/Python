class ContaError(Exception):
    """
    Classe base para erros relacionados a contas bancárias.
    """
    pass

class SaldoInsuficienteError(ContaError):
    """
    Erro levantado quando o saldo da conta é insuficiente para realizar uma operação de saque.
    """
    def __init__(self, saldo, valor):
        """
        Inicializa o erro com o saldo atual e o valor solicitado.
        
        Parâmetros:
            saldo (float): O saldo atual da conta.
            valor (float): O valor que se tentou sacar.
        """
        super().__init__(f"Saldo insuficiente: saldo atual {saldo}, valor solicitado {valor}.")
        self.saldo = saldo
        self.valor = valor

class ContaBloqueadaError(ContaError):
    """
    Erro levantado quando a conta está bloqueada.
    """
    def __init__(self, motivo):
        """
        Inicializa o erro com o motivo pelo qual a conta está bloqueada.
        
        Parâmetros:
            motivo (str): O motivo pelo qual a conta foi bloqueada.
        """
        super().__init__(f"Conta bloqueada: {motivo}")
        self.motivo = motivo

class ContaBancaria:
    """
    Classe que representa uma conta bancária.
    """
    def __init__(self, saldo):
        """
        Inicializa a conta bancária com um saldo inicial.

        Parâmetros:
            saldo (float): O saldo inicial da conta.
        """
        self.saldo = saldo
        self.bloqueada = False

    def sacar(self, valor):
        """
        Realiza um saque na conta bancária.

        Parâmetros:
            valor (float): O valor a ser sacado.

        Retorna:
            float: O novo saldo da conta.
        """
        if self.bloqueada:
            raise ContaBloqueadaError("Suspeita de fraude detectada.")
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        return self.saldo

conta = ContaBancaria(1000)

try:
    conta.sacar(1500)
except SaldoInsuficienteError as e:
    print(e)
    print(f"Você pode sacar até {e.saldo}.")