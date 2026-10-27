from rich import print

class Termostato:
    def __init__(self, temperatura = 24):
        self.__temperatura = temperatura
        
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura % 1 not in (0.0, 0.5):
            raise ValueError(f"Temperatura de {temperatura}°C inválida")
        if temperatura < 16:
            self.__temperatura = 16
        elif temperatura > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = temperatura

    def __str__(self):
        return f"Temperatura: {self.__temperatura}°C"

if __name__ == "__main__":
    t = Termostato()
    print(t)
    t.temperatura = 15
    print(t)
    t.temperatura = 18.5
    print(t)
    t.temperatura = 25.2
    print(t)