'''
087. Aprimora o desafio anterior, mostrando no final:
- A) A soma de todos os valores pares digitados.
- B) A soma dos valores da terceira coluna.
- C) O maior valor da segunda linha.
'''
# Criação da matriz 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

# Preenchimento da matriz e cálculo dos resultados
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digita o valor para [{linha}, {coluna}]: '))
        # Verifica se o número é par para somar
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        # Soma os valores da terceira coluna (índice 2)
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]
        # Verifica o maior valor da segunda linha (índice 1)
        if linha == 1:
            if coluna == 0 or matriz[linha][coluna] > maior_segunda_linha:
                maior_segunda_linha = matriz[linha][coluna]

# Mostra a matriz no ecrã com a formatação correta
print('=' * 30)
print('{:^30}'.format('RESULTADOS'))
print('=' * 30)

for linha in range(3):
    for coluna in range(3):
        matriz_formatada = (f'[{matriz[linha][coluna]:^5}]')  # Formatação para mostrar a matriz alinhada
        print('{:^10}'.format(matriz_formatada), end='')
    print()  # Muda para a próxima linha após imprimir cada linha da matriz

# Resultados
print('\n')
print('=' * 30)
print('{:^30}'.format('SOMA DOS PARES'))
print('=' * 30)
print(f'A) A soma de todos os valores pares é {soma_pares}.')

print('\n')
print('=' * 30)
print('{:^30}'.format('SOMA 3ª COLUNA'))
print('=' * 30)
print(f'B) A soma dos valores da terceira coluna é {soma_terceira_coluna}.')

print('\n')
print('=' * 30)
print('{:^30}'.format('MAIOR VALOR 2ª COLUNA'))
print('=' * 30)
print(f'C) O maior valor da segunda linha é {maior_segunda_linha}.')
