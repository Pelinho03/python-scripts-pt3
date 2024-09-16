'''
076. Criar um programa que tenha uma tupla única com nomes de produtos e respetivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
# Tupla com os produtos e preços
produtos = ('Produto 1', 50,
            'Produto 2', 60,
            'Produto 3', 120,
            'Produto 4', 30)

# Cabeçalho
print('=' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('=' * 40)

# Loop para mostrar os produtos e preços
for i in range(0, len(produtos), 2):
    produto = produtos[i]
    preco = produtos[i + 1]
    print(f'{produto:.<32} {preco:>5.2f}€')

print('=' * 40)
