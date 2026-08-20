import time

def cronometrar(funcao):
    """
    Decorator que cronometra a execução de uma função e imprime o tempo de execução.

    Parâmetros:
    funcao (function): A função a ser cronometrada.

    Retorna:
    function: A função decorada.
    """
    def wrapper(*args, **kwargs):
        """
        Função que simula um processo demorado.

        Esta função é decorada com a função cronometrar para cronometrar seu tempo de execução.

        Retorna:
        None
        """
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@cronometrar
def processar():
    time.sleep(2)
    print("Processando...")

processar()

