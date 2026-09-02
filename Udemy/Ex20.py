class Carro:
    """
    Representa um carro com um modelo e um motor. Permite ligar o motor associado ao carro.

    Parâmetros:
        modelo: O modelo do carro.
        potencia: A potência do motor do carro.
    """
    def __init__(self, modelo, potencia):
        """
        Cria um carro com o modelo e a potência informados. Associa um motor com a potência especificada ao carro.

        Parâmetros:
            modelo: O modelo do carro.
            potencia: A potência do motor do carro.
        """
        self.modelo = modelo
        self.motor = Motor(potencia)
    
    def ligar(self):
        """
        Liga o motor do carro chamando o método ligar do objeto Motor associado.
        """
        self.motor.ligar()

class Motor:
    """
    Representa um motor com uma potência específica. Permite ligar o motor.
    
    Parâmetros:
        potencia: A potência do motor em cavalos-vapor (CV).
    """
    def __init__(self, potencia):
        """
        Cria um motor com a potência informada. Mantém a potência disponível para uso posterior.
        
        Parâmetros:
            potencia: A potência do motor em cavalos-vapor (CV).
        """
        self.potencia = potencia

    def ligar(self):
        """
        Liga o motor e exibe uma mensagem indicando que o motor está ligado.
        """
        print(f"O motor de {self.potencia} CV está ligado.")

carro = Carro("Fusca", 50)
carro.ligar()

print(f"Modelo do carro: {carro.modelo}")
print(f"Potência do motor: {carro.motor.potencia} CV")