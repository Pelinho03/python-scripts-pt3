'''
076. Criar um programa que tenha uma tupla única com nomes de produtos e respetivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
# Tupla contendo nomes de produtos intercalados com os respetivos preços
listagem = ('Produto 1', 50,
            'Produto 2', 60,
            'Produto 3', 120,
            'Produto 4', 30)

# Exibe o cabeçalho da tabela
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')  # Centraliza o texto 'LISTAGEM DE PREÇOS' com 40 caracteres
print('-' * 40)

# Percorre a tupla para mostrar os produtos e preços de forma tabular
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        # Quando 'pos' é par, significa que é o nome do produto, exibido com alinhamento à esquerda e preenchido com '.'
        print(f'{listagem[pos]:.<33}', end='')
    else:
        # Quando 'pos' é ímpar, significa que é o preço, que é exibido com duas casas decimais e alinhado à direita
        print(f'{listagem[pos]:6.2f}€')

# Exibe o rodapé da tabela
print('-' * 40)
