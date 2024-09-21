'''
091. Cria um programa onde quatro jogadores joguem um dado e obtenham resultados aleatórios. Guarda esses resultados num dicionário em Python. No final, organiza esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep  # Para dar um efeito de espera nos resultados

jogadores = []  # Lista para armazenar os jogadores e resultados

# Regista o nome e o valor do dado para cada jogador
for i in range(4):
    jogador = dict()  # Inicializa um novo dicionário para cada jogador
    jogador['Nome'] = str(input(f'Nome da {i + 1}ª pessoa: '))
    jogador['Dado'] = randint(1, 6)  # Resultado do dado
    jogadores.append(jogador.copy())  # Adiciona o jogador à lista

# Ordena os jogadores pelos resultados do dado de forma decrescente (maior primeiro)
jogadores.sort(key=lambda x: x['Dado'], reverse=True)

# Mostra os resultados
print('\n')
print('=' * 30)
print('{:^30}'.format('RESULTADOS FINAIS'))
print('=' * 30)
for pessoa in jogadores:
    print(f'O {pessoa["Nome"]} tirou {pessoa["Dado"]} no dado.')
    sleep(1)  # Adiciona um pequeno delay para dar efeito

# Mostra o vencedor
print('=' * 30)
print(f'O vencedor é {jogadores[0]["Nome"]} com {jogadores[0]["Dado"]} no dado!')
print('=' * 30)
