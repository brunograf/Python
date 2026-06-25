import unittest

def soma(a, b):
    """
    Soma dois números e retorna o resultado.
    
    Parâmetros:
    a (int or float): O primeiro número.
    b (int or float): O segundo número.
    
    Retorna:
    int or float: A soma dos dois números.
    """
    return a + b

def subtracao(a, b):
    """
    Subtrai um número do outro e retorna o resultado.
    
    Parâmetros:
    a (int or float): O número que será subtraído.
    b (int or float): O número do qual será subtraído.
    
    Retorna:
    int or float: A diferença entre os dois números.
    """
    return a - b

class TestOperacaoMatematica(unittest.TestCase):
    def test_soma(self):
        """
        Testa a função soma.
        """
        resultado = 2 + 3
        self.assertEqual(resultado, 5)

    def test_subtracao(self):
        """
        Testa a função subtracao.
        """
        resultado = 2 - 3
        self.assertEqual(resultado, -1)

if __name__ == '__main__':
    unittest.main()