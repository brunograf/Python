class Porta:
    def abrir(self):
        print(f"Girar a maçaneta e empurrar/puxar a porta")

class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor com a documentação para abrir um CNPJ")

class Ovo:
    def abrir(self):
        print(f"Quebre a casca do ovo e coloque na frigideira")

class Pedra:
    pass

def tentar_abrir(objeto):#Método polimórfico duck typing
    try:
        objeto.abrir()
    except AttributeError:
        print(f"Não é possível abrir {objeto.__class__.__name__}")

def main():
    a = Porta()
    b = Empresa()
    c = Ovo()
    d= Pedra()

    tentar_abrir(a)
    tentar_abrir(b)
    tentar_abrir(c)
    tentar_abrir(d)

if __name__ == "__main__":
    main()