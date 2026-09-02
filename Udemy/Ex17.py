class ContaBancaria:
    '''
    Representa uma conta bancária com saldo privado. Permite consultar o saldo, realizar depósitos e saques de forma segura.
    
    Parâmetros:
        saldo: O saldo inicial da conta.
    
    Levanta:
        ValueError: Se o saldo inicial não for um número ou for negativo.
    '''
    def __init__(self, saldo):
        '''
        Inicializa uma conta bancária com um saldo informado. O saldo deve ser numérico e não pode ser negativo.

        Parâmetros:
            saldo: O saldo inicial da conta.

        Levanta:
            ValueError: Se o saldo inicial não for um número ou for negativo.
        '''
        if not isinstance(saldo, (int, float)):
            raise ValueError("O saldo inicial deve ser um número.")
        if saldo < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self.__saldo = saldo
    
    @property
    def saldo(self):
        '''
        Retorna o saldo atual da conta. O valor armazenado representa o saldo disponível para transações.
        '''
        return self.__saldo
    
    def depositar(self, valor):
        '''
        Adiciona um valor ao saldo da conta após validar seu conteúdo. O valor deve ser positivo.
        
        Parâmetros:
            valor: O valor a ser depositado.
        
        Levanta:
            ValueError: Se o valor não for um número ou for negativo.
        '''
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor do depósito deve ser um número.")
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.__saldo += valor

    def sacar(self, valor):
        '''
        Remove um valor do saldo da conta após validar seu conteúdo. O valor deve ser positivo e não pode exceder o saldo disponível.

        Parâmetros:
            valor: O valor a ser sacado.
        
        Levanta:
            ValueError: Se o valor não for um número, for negativo ou exceder o saldo
        '''
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor do saque deve ser um número.")
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= valor

conta = ContaBancaria(1000)
print(conta.saldo)

try:
    conta.saldo = 2000
except AttributeError as e:
    print(e)

conta.depositar(500)
print(conta.saldo)