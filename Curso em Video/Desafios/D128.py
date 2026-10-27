from rich import print

class Diario:
    def __init__(self, senha = "Gafanhoto"):
        self.__segredos = []
        self.__senha = senha
    
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha):
        if senha == self.__senha:
            print(f"[green]Diário liberado![/]")
            for msg in self.__segredos:
                print(f"- {msg}")
        else:
            raise PermissionError(f"Você não pode ler o meu diário!")

def main():
    diario = Diario("123")
    diario.escrever("Hoje eu comi uma pizza")
    diario.escrever("Hoje eu fiquei com a minha namorada")
    try:
        print(diario.ler("Gafanhoto"))
    except PermissionError as e:
        print(f"[red]{e}[/]")
    print(diario.ler("123"))

if __name__ == "__main__":
    main()


