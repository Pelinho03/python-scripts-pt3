'''
088. Faz um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, registando tudo numa lista composta.
'''
from random import randint  # Importa a função randint para gerar números aleatórios
from time import sleep  # Importa a função sleep para criar uma pausa entre os jogos

lista = list()  # Lista temporária para armazenar os números sorteados de cada jogo
jogos = list()  # Lista composta que vai armazenar todos os jogos sorteados

# Cabeçalho do programa
print('-' * 30)
print('{:^30}'.format('JOGOS DA SORTE'))  # Exibe o título centralizado
print('-' * 30)

# Solicita ao utilizador quantos jogos deseja sortear
quant = int(input('Quantos jogos queres que sorteie? '))

tot = 1  # Inicializa o contador de jogos

# Laço principal para gerar os jogos
while tot <= quant:
    cont = 0  # Contador de números sorteados para cada jogo
    while True:
        num = randint(1, 60)  # Gera um número aleatório entre 1 e 60
        if num not in lista:  # Verifica se o número já foi sorteado neste jogo
            lista.append(num)  # Adiciona o número à lista temporária
            cont += 1  # Incrementa o contador de números sorteados
        if cont >= 6:  # Se já houver 6 números sorteados, termina o sorteio deste jogo
            break
    lista.sort()  # Ordena os números do jogo em ordem crescente
    jogos.append(lista[:])  # Adiciona a cópia da lista de números sorteados à lista de jogos
    lista.clear()  # Limpa a lista temporária para o próximo jogo
    tot += 1  # Incrementa o contador de jogos

# Exibe os jogos sorteados
print('\n')
print('-' * 5, f' {quant} JOGOS SORTEADOS', '-' * 5)
for i, l in enumerate(jogos):  # Loop para exibir cada jogo sorteado
    print(f'Jogo {i + 1}: {l}')  # Exibe o número do jogo e os seus números sorteados
    sleep(1)  # Pausa de 1 segundo entre a exibição dos jogos para dar um efeito visual

# Mensagem de encerramento
print('-' * 7, '< BOA SORTE! >', '-' * 7)
