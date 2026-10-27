from hashlib import sha256
from rich import print

class ContaBancaria:
    def __init__(self, id, nome = None, saldo = 0, chave = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        if chave is None:
            chave = self.pede_senha()
        print(f"Conta {self._id} criada com sucesso! Saldo atual de R${self.__saldo:.2f}.")
    
    def pede_senha(self):
        from pwinput import pwinput
        while True:
            senha = pwinput("Digite uma senha: ").strip()
            if len(senha) < 6:
                print("Senha muito curta! Tente novamente.")
            else:
                return senha
    
    def validar_senha(self, chave):
        if self.__hash == sha256(chave.encode("utf-8")).hexdigest():  # noqa: SIM103
            return True
        else:
            return False
    
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} autorizado na conta {self._id}.")
    
    def sacar(self, valor, chave = None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Saque negado de R${valor:.2f} na conta {self._id}. Saldo insuficiente!")
            else:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} autorizado na conta {self._id}.")
        else:
            print(f"Senha não confere. Saque não autorizado!")
    
    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self, novonome = None):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            self._titular = novonome
            print(f"Nome alterado para {self._titular}.")
        else:
            print("Senha não confere. Nome não alterado!")

    def __str__(self):
        return f"Conta {self._id} - Titular: {self._titular} - Saldo: R${self.__saldo:.2f}"

if __name__ == "__main__":
    conta = ContaBancaria(123456, "João da Silva", 1000, "123456")
    print(conta)
    conta.depositar(500)
    print(conta)
    conta.sacar(200)
    print(conta)
    conta.nome = "Maria da Silva"
    print(conta)