from interface import cabecalho, menu, leiaInt
from lista import arquivoExiste, criarArquivo, lerArquivo, cadastrar
from time import sleep

arquivo = 'pessoas.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho(f'\033[31mERRO: Digite uma opção válida.\033[m')
    sleep(1)