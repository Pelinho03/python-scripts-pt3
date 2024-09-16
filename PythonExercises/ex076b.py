'''
076. Criar um programa que tenha uma tupla única com nomes de produtos e respetivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
# Tupla de tuplas contendo produtos e respetivos preços
produtos = (('Bola', 12),
            ('Toalha', 4),
            ('Pedra', 3),
            ('Relógio', 120),
            ('iPhone', 980))

# Exibir cabeçalho formatado
print('=' * 40)
print('{:^40}'.format('LISTA DE ARTIGOS'))
print('=' * 40)

# Percorrer a tupla e exibir cada produto e preço formatado
for x, y in produtos:
    # Alinhar o nome do produto à esquerda e o preço à direita com 2 casas decimais
    print(f'{x:.<32}', f'{y:.>7.2f}')

# Exibir rodapé formatado
print('=' * 40)

