from rich import print
from hashlib import sha256

class Credencial:
    def __init__(self):
        self.__hash = None
    
    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        else:
            raise ValueError("A senha não pode ser vazia!")

    def validar(self, chave):
        if self.__hash == sha256(chave.encode("utf-8")).hexdigest():
            print("[green]Acesso permitido![/]")
        else:
            print("[red]Acesso negado![/]")
        return sha256(chave.encode("utf-8")).hexdigest()


def main():
    credencial = Credencial()
    credencial.senha = "Gafanhoto"
    print(credencial.senha)
    credencial.validar("CeV")
    credencial.validar("Gafanhoto")
    
if __name__ == "__main__":
    main()