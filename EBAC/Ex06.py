import threading

def new():
    """
    Executa uma única thread que imprime uma mensagem diversas vezes.

    Esta função representa o trabalho executado por uma thread, repetindo
    a impressão de uma mensagem fixa no console.
    """
    for i in range(6):
        print('Thread única')

t1 = threading.Thread(target=new)

t1.start()
t1.join()
print('Sucesso')
