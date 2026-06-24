import time, threading

def calculo_quadrado(numero):
    """
    Calcula e exibe o quadrado e o cubo de uma sequência de números. 
    Esta função recebe uma coleção de valores numéricos e imprime o quadrado de cada elemento com um atraso entre as execuções.

    Args:
        numero: Iterável contendo os números que terão seus quadrados calculados.
    """
    print('Calculando o quadrado do número:')
    for i in numero:
        time.sleep(2)
        print(f'O quadrado do número {i} é {i * i}')

def calculo_cubo(numero):
    print('Calculando o cubo do número:')
    for i in numero:
        time.sleep(2)
        print(f'O cubo do número {i} é {i * i * i}')

if __name__ == "__main__":
    numero = [1, 2, 3, 4, 5]
    #Criando duas threads
    t1 = threading.Thread(target=calculo_quadrado, args=(numero,))
    t2 = threading.Thread(target=calculo_cubo, args=(numero,))
    #Iniciando as threads em paralelo
    t1.start()
    t2.start()
    #Aguardando o término da função calculo_quadrado
    t1.join()
    #Aguardando o término da função calculo_cubo
    t2.join()
    print('Sucesso')