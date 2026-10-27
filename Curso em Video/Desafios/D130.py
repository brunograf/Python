from rich import print

class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None
        
        self.base = base
        self.altura = altura
    
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance(base, float) and not isinstance(base, int):
            raise TypeError("A base deve ser um número!")
        if base <= 0:
            raise ValueError("A base deve ser maior do que zero!")
        else:
            self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, float) and not isinstance(altura, int):
            raise TypeError("A altura deve ser um número!")
        if altura <= 0:
            raise ValueError("A altura deve ser maior do que zero!")
        else:
            self._altura = altura

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area
    
    @area.setter
    def area(self, area):
        raise PermissionError("Não é possível alterar o valor da área!")
    
    @property
    def medidas(self):
        return f"Base: {self.base} | Altura: {self.altura} | Área: {self.area}"
        
    @medidas.setter
    def medidas(self, medidas:tuple):
        if len(medidas) != 2:
            raise SyntaxError("O retângulo deve ter duas medidas: base e altura!")
        if isinstance(medidas[0], float) or isinstance(medidas[0], int):
            self.base = medidas[0]
        else:
            raise TypeError("A base deve ser um número!")
        if isinstance(medidas[1], float) or isinstance(medidas[1], int):
            self.altura = medidas[1]
        else:
            raise TypeError("A altura deve ser um número!")
        self._area = self._base * self._altura
        return f"Base: {self._base} | Altura: {self._altura} | Área: {self._area}"

def main():
    ret = Retangulo()
    ret.medidas = (5, 9)
    print(ret.medidas)


if __name__ == "__main__":
    main()


