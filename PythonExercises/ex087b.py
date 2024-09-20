'''
087. Aprimora o desafio anterior, mostrando no final:
- A) A soma de todos os valores pares digitados.
- B) A soma dos valores da terceira coluna.
- C) O maior valor da segunda linha.
'''
# Cria uma matriz 3x3 preenchida inicialmente com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0  # Variáveis para armazenar a soma dos pares, maior valor da segunda linha e a soma da terceira coluna

# Preenchimento da matriz com os valores introduzidos pelo utilizador
for l in range(3):  # Loop para percorrer as linhas
    for c in range(3):  # Loop para percorrer as colunas
        matriz[l][c] = int(input(f'Digita um valor [{l}, {c}]: '))  # Preenche a matriz com o valor fornecido

print('-=' * 30)

# Exibição da matriz e cálculo da soma dos valores pares
for l in range(3):  # Loop para percorrer as linhas
    for c in range(3):  # Loop para percorrer as colunas
        print(f'[{matriz[l][c]:^5}]', end='')  # Exibe cada valor da matriz formatado
        if matriz[l][c] % 2 == 0:  # Verifica se o valor é par
            spar += matriz[l][c]  # Soma os valores pares
    print()  # Salta para a próxima linha após imprimir uma linha da matriz

print('-=' * 30)

# Mostra a soma dos valores pares
print(f'A) A soma dos valores pares é {spar}')

# Soma dos valores da terceira coluna (coluna de índice 2)
for l in range(3):
    scol += matriz[l][2]  # Soma os valores da terceira coluna

print(f'B) A soma dos valores da terceira coluna é {scol}.')

# Cálculo do maior valor da segunda linha (linha de índice 1)
for c in range(3):
    if c == 0:
        mai = matriz[1][c]  # Inicializa o maior valor com o primeiro elemento da segunda linha
    elif matriz[1][c] > mai:  # Verifica se os valores subsequentes são maiores
        mai = matriz[1][c]  # Atualiza o maior valor

print(f'C) O maior valor da segunda linha é {mai}.')
