'''
078. Fazer um programa que leia 5 valores numéricos e guarde-os numa lista. No final, mostre qual foi o maior e o menor valor digitado e as respetivas posições na lista.
'''
# Inicializa uma lista vazia para armazenar os valores numéricos
listanum = []

# Inicializa as variáveis para armazenar o maior e menor valor
maior = menor = 0

# Loop para ler 5 valores do utilizador
for c in range(5):
    # Lê um valor e adiciona à lista, especificando a posição atual
    listanum.append(int(input(f'Digita um valor para a Posição {c + 1}: ')))

    # Se for o primeiro valor, define-o como maior e menor
    if c == 0:
        maior = menor = listanum[c]
    else:
        # Atualiza o maior valor, se necessário
        if listanum[c] > maior:
            maior = listanum[c]
        # Atualiza o menor valor, se necessário
        if listanum[c] < menor:
            menor = listanum[c]

# Exibe a lista de valores digitados
print('=-' * 30)
print(f'Digitaste os valores {listanum}')

# Exibe o maior valor e as respetivas posições
print(f'O maior valor foi {maior} na posição ', end='')
# Loop através da lista com índice e valor usando enumerate
for i, v in enumerate(listanum):
    # Verifica se o valor é igual ao maior valor
    if v == maior:
        # Imprime a posição onde o maior valor foi encontrado
        print(f'{i}...', end='')
print()

# Exibe o menor valor e as respetivas posições
print(f'O menor valor foi {menor} na posição ', end='')
# Loop através da lista com índice e valor usando enumerate
for i, v in enumerate(listanum):
    # Verifica se o valor é igual ao menor valor
    if v == menor:
        # Imprime a posição onde o menor valor foi encontrado
        print(f'{i}...', end='')
print()
