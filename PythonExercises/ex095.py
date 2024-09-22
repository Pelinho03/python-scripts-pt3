'''
095. Aprimora o desafio 93 para que funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
equipa = list()  # Lista para armazenar os dados de vários jogadores
jogador = dict()  # Dicionário para armazenar os dados de cada jogador individualmente
partidas = list()  # Lista para armazenar o número de golos por partida

while True:
    jogador.clear()  # Limpa o dicionário do jogador para garantir que não existam dados antigos
    jogador['nome'] = str(input('Nome do Jogador: '))  # Coleta o nome do jogador
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))  # Coleta o número de partidas jogadas
    partidas.clear()  # Limpa a lista de partidas para garantir que não existam dados antigos

    # Loop para coletar o número de golos de cada partida
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos golos na partida {c + 1}? ')))  # Adiciona os golos à lista de partidas

    jogador['golos'] = partidas[:]  # Copia a lista de golos para o dicionário do jogador
    jogador['total'] = sum(partidas)  # Calcula o total de golos e armazena no dicionário

    equipa.append(jogador.copy())  # Faz uma cópia do dicionário do jogador e adiciona à lista da equipa

    # Pergunta ao utilizador se quer continuar a adicionar jogadores
    while True:
        resp = str(input('Queres continuar? [S/N] ')).upper()[0]
        if resp in 'SN':  # Validação da resposta
            break
        print('ERRO! Responde apenas S ou N.')

    if resp == 'N':  # Se a resposta for 'N', termina o loop
        break

# Exibição do cabeçalho com os campos
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():  # Mostra as chaves do dicionário como cabeçalhos
    print(f'{i:<15}', end='')
print()

# Exibição da tabela de dados de cada jogador
print('-' * 40)
for k, v in enumerate(equipa):  # Para cada jogador na equipa
    print(f'{k:>3} ', end='')  # Mostra o índice do jogador (código)
    for d in v.values():  # Mostra os valores (nome, golos, total)
        print(f'{str(d):<15}', end='')  # Exibe os dados formatados
    print()

print('-' * 40)

# Loop para exibir detalhes de um jogador específico
while True:
    busca = int(input('Mostrar dados de que jogador? (999 para parar.) '))  # Solicita o código do jogador
    if busca == 999:  # Se o utilizador digitar 999, o loop é encerrado
        break
    if busca >= len(equipa):  # Verifica se o código inserido é válido
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        # Exibe os detalhes do jogador específico
        print(f' -- LEVANTAMENTO DO JOGADOR {equipa[busca]["nome"]}')
        for i, g in enumerate(equipa[busca]['golos']):  # Lista os golos por partida
            print(f'    No {i + 1}º jogo fez {g} golos.')
    print('-' * 40)

# Mensagem de despedida
print('<<< VOLTE SEMPRE >>>')
