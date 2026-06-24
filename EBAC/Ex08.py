import multiprocessing

resultados = []

def calculo_quadrado(numero):
    """
    Calcula e armazena o quadrado de uma sequência de números. 
    Esta função recebe uma coleção de valores numéricos, calcula o quadrado de cada elemento e registra os resultados em uma lista global.

    Args:
        numero: Iterável contendo os números que terão seus quadrados calculados.
    """
    global resultados
    print('Calculando o quadrado do número:')
    for i in numero:
        resultado = i * i
        resultados.append(resultado)
        print(f'O quadrado do número {i} é {resultado}')

if __name__ == "__main__":
    numero = [1, 2, 3, 4, 5]
    #Criando o multiprocessamento
    p1 = multiprocessing.Process(target=calculo_quadrado, args=(numero,))
    #Iniciando o multiprocessamento em paralelo
    p1.start()
    #Aguardando o término da função calculo_quadrado
    p1.join()
    print('Sucesso')