from functools import singledispatchmethod

class Analisador:
    @singledispatchmethod
    def analisar(self, valor):
        print(f"Não foi possível analisar o valor {valor}")
    
    @analisar.register(int)
    def _(self, valor):
        print(f"{valor} é um número inteiro")

    @analisar.register(float)
    def _(self, valor):
        print(f"{valor} é um número real")

    @analisar.register(str)
    def _(self, valor):
        print(f"'{valor}' é uma cadeia de caracteres")
    
    @analisar.register(list|tuple|set|dict)
    def _(self, valor):
        print(f"{valor} é uma coleção de dados")

def main():
    analisador = Analisador()
    analisador.analisar(10)
    analisador.analisar(3.14)
    analisador.analisar("Olá, mundo!")
    analisador.analisar([1, 2, 3])

if __name__ == "__main__":
    main()