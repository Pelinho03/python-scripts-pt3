'''
094. Cria um programa que leia o nome, o sexo e a idade de várias pessoas, guardando os dados de cada pessoa num dicionário e todos os dicionários numa lista. No final, mostra:
- A) Quantas pessoas foram cadastradas.
- B) A média de idade.
- C) Uma lista com as mulheres.
- D) Uma lista de pessoas com idade acima da média.
'''
# Inicializa uma lista para armazenar os dados de todas as pessoas e um dicionário para armazenar os dados de cada pessoa
pessoal = list()
pessoa = dict()

# Variáveis para calcular a soma das idades e a média
soma = media = 0

# Loop principal para cadastrar várias pessoas
while True:
    pessoa.clear()  # Limpa o dicionário antes de cada novo cadastro

    # Coleta o nome da pessoa
    pessoa['nome'] = str(input('Nome: '))

    # Coleta o sexo da pessoa e garante que a entrada seja 'M' ou 'F'
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':  # Verifica se a resposta é válida
            break
        print('ERRO! Por favor, digita apenas M ou F.')

    # Coleta a idade da pessoa
    pessoa['idade'] = int(input('Idade: '))

    # Soma a idade para depois calcular a média
    soma += pessoa['idade']

    # Adiciona uma cópia do dicionário 'pessoa' à lista 'pessoal'
    pessoal.append(pessoa.copy())

    # Pergunta se o utilizador deseja continuar e verifica se a resposta é válida
    while True:
        resp = str(input('Queres continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':  # Verifica se a resposta é válida
            break
        print('ERRO! Responde apenas S ou N.')

    # Se a resposta for 'N', interrompe o loop
    if resp == 'N':
        break

# Exibe uma linha de separação visual
print('-=' * 30)

# A) Exibe o número total de pessoas registadas
print(f'A) Ao todo temos {len(pessoal)} pessoas registadas.')

# Calcula a média de idades
media = soma / len(pessoal)

# B) Exibe a média de idades
print(f'B) A média de idades é de {media:5.2f} anos.')

# C) Lista as mulheres registadas
print(f'C) As mulheres registadas foram ', end='')
for p in pessoal:
    if p['sexo'] == 'F':  # Verifica se o sexo é feminino
        print(f'{p["nome"]} ', end='')
print()

# D) Lista as pessoas com idade acima da média
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in pessoal:
    if p['idade'] >= media:  # Verifica se a idade está acima da média
        print('    ')
        for k, v in p.items():  # Itera pelos campos de cada pessoa
            print(f'{k} = {v}; ', end='')
            print()

# Mensagem de término do programa
print('<< A TERMINAR >>')
