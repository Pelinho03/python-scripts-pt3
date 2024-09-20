'''
088. Faz um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, registando tudo numa lista composta.
'''
from random import randint
from time import sleep  # Para dar um efeito de "suspense" ao mostrar os resultados

# Criação da lista para armazenar os jogos
jogos_mega_sena = []

# Interface inicial
print('=' * 30)
print('{:^30}'.format('JOGO DA SORTE - PALPITES'))
print('=' * 30)

# Pergunta quantos jogos o utilizador pretende gerar
quantidade_jogos = int(input('Quantos jogos pretendes gerar? '))

# Geração dos jogos
for i in range(quantidade_jogos):
    jogo = []  # Lista para armazenar os 6 números de cada jogo
    while len(jogo) < 6:  # Gera até ter 6 números únicos
        numero = randint(1, 60)
        if numero not in jogo:  # Garante que o número não está repetido no mesmo jogo
            jogo.append(numero)

    jogo.sort()  # Ordena os números de cada jogo para ficarem em ordem crescente
    jogos_mega_sena.append(jogo)  # Adiciona o jogo gerado à lista de jogos

    # Mostra cada jogo com um pequeno delay para dar um efeito de "suspense"
    print(f'Jogo {i + 1}: {jogo}')
    sleep(1)  # Pausa de 1 segundo entre cada jogo (opcional)

# Mensagem final
print('=' * 30)
print('{:^30}'.format('BOA SORTE!'))
print('=' * 30)
