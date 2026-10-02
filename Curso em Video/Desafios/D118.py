from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":book: Você começou a ler o livro [blue]{self.titulo}[/blue] com [green]{self.paginas} páginas[/green] no total. Você agora está na [yellow]página {self.pagina_atual}[/yellow]")

    def avancar_paginas(self, qtd=1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág {self.pagina_atual} :arrow_forward: ", end=" ")
                sleep(0.3)
                cont += 1
        print(f"Você avançou [green]{cont} páginas[/green] e agora está na [yellow]página {self.pagina_atual}[/yellow]")
        if self.fim_do_livro():
            print(f":police_car_light: Você terminou o livro [blue]{self.titulo}[/blue]. Parabéns!")
    
    def fim_do_livro(self):
        if self.pagina_atual == self.paginas:
            return True
        else:
            return False

livro1 = Livro("10 coisas que aprendi", 20)
livro1.avancar_paginas(5)
livro1.avancar_paginas(10)
livro1.avancar_paginas(100)