def lista_de_tarefas():
    """
    Gerencia uma lista de tarefas por meio de comandos interativos no terminal.
    Permite adicionar, listar, desfazer e refazer tarefas, retornando a lista final ao encerrar.

    Parâmetros:
        None: Todos os dados necessários são obtidos por meio de entradas do usuário.

    Retorna:
        list: Lista contendo as tarefas restantes após o término da interação.
    """
    tarefas = []
    while True:
        tarefa = input("Digite um comando:\n1 - Adicionar tarefa\n2 - Comandos\n3 - Sair\n")
        if tarefa.lower() == '1':
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
        elif tarefa.lower() == '2':
            print("Comandos disponíveis:\n1 - Listar tarefas\n2 - Desfazer\n3 - Refazer\n4 - Sair")
            while True:
                comando = input("Digite um comando: ")
                if comando.lower() == '1':
                    print("Tarefas:")
                    for i, tarefa in enumerate(tarefas):
                        print(f"{i + 1}. {tarefa}")
                elif comando.lower() == '2':
                    if tarefas:
                        tarefa_desfeita = tarefas.pop()
                        print(f"Tarefa '{tarefa_desfeita}' desfeita.")
                    else:
                        print("Não há tarefas para desfazer.")
                elif comando.lower() == '3':
                    if tarefa_desfeita is not None:
                        tarefas.append(tarefa_desfeita)
                        print(f"Tarefa '{tarefa_desfeita}' refeita.")
                        tarefa_desfeita = None
                    else:
                        print("Não há tarefas para refazer.")
                elif comando.lower() == '4':
                    break
                else:
                    print("Comando inválido. Tente novamente.")
        elif tarefa.lower() == '3':
            break
        else:
            print("Comando inválido. Tente novamente.")
    return tarefas


tarefas = lista_de_tarefas()
print("Tarefas restantes:")
for i, tarefa in enumerate(tarefas):
    print(f"{i + 1}. {tarefa}")