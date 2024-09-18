'''
084. Faz um programa que leia o nome e o peso de várias pessoas, guardando tudo numa lista. No final, mostra:
- A) Quantas pessoas foram registadas.
- B) Uma listagem com as pessoas mais pesadas.
- C) Uma listagem com as pessoas mais leves
'''
# Inicializa a lista principal para armazenar as pessoas
pessoas = []

# Variáveis para contar o número de pessoas registadas e para armazenar os maiores e menores pesos
cont = 0
maior_peso = menor_peso = 0
mais_pesadas = []
mais_leves = []

# Loop para coletar os dados das pessoas
while True:
    nome = input('Nome: ').strip()        # Lê o nome da pessoa
    peso = float(input('Peso: '))        # Lê o peso da pessoa
    pessoas.append([nome, peso])          # Adiciona uma sublista com nome e peso à lista principal
    cont += 1                              # Incrementa o contador de pessoas

    # Pergunta ao utilizador se quer continuar a inserir dados
    resp = input('Queres continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break  # Encerra o loop se o utilizador escolher 'N'

# Exibe a lista completa de pessoas registadas
print('\n')
print('=' * 30)
print('{:^30}'.format('PESSOAS REGISTADAS'))
print('=' * 30)
for p in pessoas:
    print(f'{p[0]:<20} -> {p[1]:>5} kg')
print('=' * 30)

# Determina o maior e o menor peso
# Inicializa com o peso da primeira pessoa para comparação
maior_peso = menor_peso = pessoas[0][1]

# Percorre a lista para encontrar o maior e o menor peso
for p in pessoas:
    if p[1] > maior_peso:
        maior_peso = p[1]
    if p[1] < menor_peso:
        menor_peso = p[1]

# Identifica todas as pessoas com o maior peso
for p in pessoas:
    if p[1] == maior_peso:
        mais_pesadas.append(p[0])

# Identifica todas as pessoas com o menor peso
for p in pessoas:
    if p[1] == menor_peso:
        mais_leves.append(p[0])

# Exibe o total de pessoas registadas
print(f'\nForam registadas {cont} pessoas.')

# Exibe a listagem das pessoas mais pesadas
print(f'\nAs pessoas mais pesadas, com {maior_peso} kg, são:')
for p in mais_pesadas:
    print(f'- {p}')

# Exibe a listagem das pessoas mais leves
print(f'\nAs pessoas mais leves, com {menor_peso} kg, são:')
for p in mais_leves:
    print(f'- {p}')
