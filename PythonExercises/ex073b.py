'''
073. Criar uma tupla preenchida com os 18 primeiros colocados da Tabela do Campeonato Português de Futebol, na ordem de colocação. Depois mostre:
- a) As 5 primeiras equipas.
- b) Os últimos 4 colocados.
- c) Equipas em ordem alfabética.
- d) Em que posição está o Famalicão.
'''
classificacao = (
    'Sporting CP', 'FC Porto', 'Vitória SC', 'Famalicão', 'Benfica', 'Santa Clara', 'Braga', 'Moreirense', 'AVS',
    'Gil Vicente', 'Casa Pia AC', 'Rio Ave', 'Estoril', 'Boavista', 'Nacional', 'Arouca', 'Estrela da Amadora',
    'Farense'
)

# Exibir o título da tabela classificativa
print('=' * 30)
print('{:^30}'.format('TABELA CLASSIFICATIVA'))
print('=' * 30)

# Exibir todas as equipas com a sua respetiva colocação
for i in range(len(classificacao)):
    print(f'{i + 1:2}º', '->', f'{classificacao[i]}')

# Exibir as 5 primeiras equipas
print('\n')
print('=' * 30)
print('{:^30}'.format('5 PRIMEIROS'))
print('=' * 30)

for p in range(5):
    print(f'{p + 1}º', '->', f'{classificacao[p]}')

# Exibir os últimos 4 colocados
print('\n')
print('=' * 30)
print('{:^30}'.format('4 ÚLTIMOS'))
print('=' * 30)

for u in range(4):
    print(f'{u + 14}º', '->', f'{classificacao[u + 14]}')

# Exibir as equipas em ordem alfabética
print('\n')
print('=' * 30)
print('{:^30}'.format('ORDEM ALFABÉTICA'))
print('=' * 30)

ordem_alfa = sorted(classificacao)
for ordem in range(len(classificacao)):
    print(f'{ordem + 1:2}º', '->', f'{ordem_alfa[ordem]}')

# Exibir a posição do Famalicão na tabela
print('\n')
print('=' * 30)
print('{:^30}'.format('POSIÇÃO | FAMALICÃO'))
print('=' * 30)

print(f'O Famalicão está na {classificacao.index("Famalicão") + 1}ª posição')

# Outra versão mais resumida dos resultados, apenas com os dados diretos
print('\n')
print('=' * 30)
print(f'Os 5 primeiros são {classificacao[0:5]}')
print(f'Os 4 últimos são {classificacao[-4:]}')
print(f'Ordem alfabética: {sorted(classificacao)}')
print(f'O Famalicão está na {classificacao.index("Famalicão") + 1}ª posição')
