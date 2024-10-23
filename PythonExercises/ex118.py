from random import choice  # Importa a função 'choice' do módulo random para escolher aleatoriamente um filme da lista
from time import sleep  # Importa a função 'sleep' do módulo time para criar uma contagem regressiva com pausas

filmes = list()  # Inicializa uma lista vazia para armazenar os filmes

# Pede ao utilizador para introduzir o número de filmes que quer adicionar à lista
num = int(input('Digita o número de filmes que queres introduzir: '))

# Ciclo para adicionar os filmes à lista
for i in range(num):
    adicionar = input(f'{i + 1}º filme: ')  # Pede o nome do filme
    filmes.append(adicionar)  # Adiciona o filme à lista

print('\n')  # Nova linha para espaçamento
print('=' * 30)  # Linha de separação para formatar a saída
print('{:^30}'.format('LISTA DE FILMES'))  # Formata o título "LISTA DE FILMES" no centro com 30 caracteres
print('=' * 30)

# Ciclo para exibir a lista de filmes, numerada
for c, filme in enumerate(filmes):
    print(f'{c + 1}º -> {filme}')  # Mostra o número e o nome do filme
print('=' * 30)  # Linha de separação no fim da lista

print('\n')  # Nova linha para espaçamento
print('=' * 30)  # Linha de separação para formatar a saída
print('{:^30}'.format('FILME ESCOLHIDO'))  # Formata o título "FILME ESCOLHIDO" no centro com 30 caracteres
print('=' * 30)

# Cria uma contagem regressiva de 5 a 1
print('5')
sleep(1)  # Espera 1 segundo antes de passar para o próximo número
print('4')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)

print('\n')  # Nova linha para espaçamento
filme_escolhido = choice(filmes).upper()  # Escolhe um filme aleatoriamente da lista e converte o nome para maiúsculas
print(f'O filme escolhido foi o {filme_escolhido}')  # Mostra o nome do filme escolhido
print('=' * 30)  # Linha de separação no fim do programa
