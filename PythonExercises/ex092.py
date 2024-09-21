'''
092. Cria um programa que leia o nome, o ano de nascimento e a carteira de trabalho de uma pessoa, registando também a idade num dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário também receberá o ano de contratação e o salário. Calcula e acrescenta, além da idade, com quantos anos a pessoa se vai reformar.
'''
from datetime import datetime  # Para obter o ano atual

pessoa = dict()

# Recolhe os dados do utilizador
pessoa['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - ano_nasc  # Calcula a idade atual
pessoa['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))

# Se a pessoa tiver CTPS válida
if pessoa['ctps'] != 0:
    pessoa['ano_contratacao'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: €'))

    # Calcula com quantos anos a pessoa se reforma (tempo de trabalho + idade atual)
    anos_trabalho = 65 - pessoa['idade']  # Faltam quantos anos para atingir os 65
    pessoa['idade_reforma'] = pessoa['ano_contratacao'] + anos_trabalho

# Mostra os dados finais
print('\nDados registados:')
for k, v in pessoa.items():
    print(f'  - {k.capitalize()}: {v}')
