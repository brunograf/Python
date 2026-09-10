from abc import ABC, abstractmethod

class ProcessadorPagamento(ABC):
    """
    Classe abstrata para processadores de pagamento.
    
    Parâmetros:
        abc: Módulo para definir classes abstratas.
    """
    @abstractmethod
    def processar(self, valor):
        """
        Método abstrato para processar um pagamento.
        
        Parâmetros:
            valor: Valor do pagamento.
        """
        pass
    
    @abstractmethod
    def reembolsar(self, valor):
        """
        Método abstrato para reembolsar um pagamento.
        
        Parâmetros:
            valor: Valor do reembolso.
        """
        pass

class PayPal(ProcessadorPagamento):
    """
    Classe para processadores de pagamento via PayPal.
    
    Parâmetros:
        valor: Valor do pagamento.
    """
    def processar(self, valor):
        """
        Método para processar um pagamento via PayPal.
        
        Parâmetros:
            valor: Valor do pagamento.
        """
        print(f"Processando pagamento de R${valor} via PayPal.")
    
    def reembolsar(self, valor):
        """
        Método para reembolsar um pagamento via PayPal.
        
        Parâmetros:
            valor: Valor do reembolso.
        """
        print(f"Reembolsando R${valor} via PayPal.")

class PagSeguro(ProcessadorPagamento):
    """
    Classe para processadores de pagamento via PagSeguro.
    
    Parâmetros:
        valor: Valor do pagamento.
    """
    def processar(self, valor):
        """
        Método para processar um pagamento via PagSeguro.
        
        Parâmetros:
            valor: Valor do pagamento.
        """
        print(f"Processando pagamento de R${valor} via PagSeguro.")
    
    def reembolsar(self, valor):
        """
        Método para reembolsar um pagamento via PagSeguro.
        
        Parâmetros:
            valor: Valor do reembolso.
        """
        print(f"Reembolsando R${valor} via PagSeguro.")

def realizar_pagamento(processador, valor):
    """
    Função para realizar um pagamento.
    
    Parâmetros:
        processador: Instância de ProcessadorPagamento.
        valor: Valor do pagamento.
    """
    processador.processar(valor)

def realizar_reembolso(processador, valor):
    """
    Função para realizar um reembolso.
    
    Parâmetros:
        processador: Instância de ProcessadorPagamento.
        valor: Valor do reembolso.
    """
    processador.reembolsar(valor)

realizar_pagamento(PayPal(), 100)
realizar_pagamento(PagSeguro(), 200)
realizar_reembolso(PayPal(), 50)
realizar_reembolso(PagSeguro(), 100)