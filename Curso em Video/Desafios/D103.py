def ficha(nome='<desconecido>', gols=0):
    '''
    Mostra a ficha de um jogador de futebol com o número de gols feitos.
    
    Parâmetros:
        nome: O nome do jogador. Padrão: '<desconecido>'.
        gols: O número de gols feitos. Padrão: 0.
    '''
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome_jogador = input("Digite o nome do jogador: ")
gols_jogador = input("Digite o número de gols feitos: ")
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador.strip() == '':
    nome_jogador = '<desconecido>'
ficha(nome_jogador, gols_jogador)