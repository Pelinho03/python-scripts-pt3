'''
073. Criar uma tupla preenchida com os 18 primeiros colocados da Tabela do Campeonato Português de Futebol, na ordem de colocação. Depois mostre:
- a) As 5 primeiras equipas.
- b) Os últimos 4 colocados.
- c) Equipas em ordem alfabética.
- d) Em que posição está o Famalicão.
'''
# Tupla com a classificação das equipas
classificacao = (
    'Sporting CP', 'FC Porto', 'Vitória SC', 'Famalicão', 'Benfica', 'Santa Clara', 'Braga', 'Moreirense', 'AVS',
    'Gil Vicente', 'Casa Pia AC', 'Rio Ave', 'Estoril', 'Boavista', 'Nacional', 'Arouca', 'Estrela da Amadora',
    'Farense'
)

print('=' * 50)
print('{:^50}'.format('TABELA CLASSIFICATIVA'))
print('=' * 50)

# Mostrar a classificação completa
print('\nClassificação Completa:')
for i in range(18):
    print(f'{i + 1}º -> {classificacao[i]}')

print('\n' + '=' * 50)

# a) As 5 primeiras equipas
print(f'5 Primeiros Lugares:')
for i in range(5):
    print(f'{i + 1}º -> {classificacao[i]}')

# b) Os últimos 4 colocados
print('\nÚltimos 4 Colocados:')
for i in range(-4, 0):
    print(f'{18 + i +1}º -> {classificacao[i]}')

# c) Equipas em ordem alfabética
print('\nEquipas em Ordem Alfabética:')
for equipa in sorted(classificacao):
    print(f'- {equipa}')

# d) Em que posição está o Famalicão
posicao_famalicao = classificacao.index('Famalicão') + 1
print(f'\nO Famalicão encontra-se na posição: {posicao_famalicao}º')
