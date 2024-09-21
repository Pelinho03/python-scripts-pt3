'''
093. Cria um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e o número de partidas que ele jogou. Em seguida, vai ler a quantidade de golos feitos em cada partida. No final, todas essas informações serão guardadas num dicionário, incluindo o total de golos marcados durante o campeonato.
'''
# Criação de um dicionário para armazenar as informações do jogador
jogador = dict()

# Criação de uma lista para armazenar a quantidade de golos em cada partida
partidas = list()

# Solicita o nome do jogador e armazena no dicionário
jogador['nome'] = str(input('Nome do Jogador: '))

# Pergunta quantas partidas o jogador jogou e armazena o total
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou?'))

# Loop para perguntar a quantidade de golos em cada partida
for c in range(0, tot):
    # Adiciona a quantidade de golos de cada partida à lista 'partidas'
    partidas.append(int(input(f'Quantos golos na partida {c + 1}? ')))

# Armazena a lista de golos em cada partida no dicionário 'jogador'
jogador['golos'] = partidas[:]

# Calcula o total de golos marcados somando os valores da lista 'partidas'
jogador['total'] = sum(partidas)

# Mostra uma linha de separação visual
print('-=' * 30)

# Mostra o dicionário completo, com as informações do jogador
print(jogador)

# Mostra uma linha de separação visual
print('-=' * 30)

# Itera sobre os itens do dicionário 'jogador' e mostra cada campo com seu valor
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

# Mostra uma linha de separação visual
print('-=' * 30)

# Mostra o total de partidas que o jogador jogou
print(f'O jogador {jogador["nome"]} jogou {len(jogador["golos"])} partidas.')

# Itera pela lista de golos e mostra quantos golos foram marcados em cada partida
for i, v in enumerate(jogador['golos']):
    print(f'    => Na partida {i + 1}, fez {v} golos.')

# Mostra o total de golos marcados durante o campeonato
print(f'Foi um total de {jogador["total"]} golos.')
