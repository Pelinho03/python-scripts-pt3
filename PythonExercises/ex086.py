'''
086. Cria um programa que declare uma matriz de dimensão 3x3 e preencha-a com valores lidos pelo teclado. No final, mostra a matriz no ecrã, com a formatação correta.
'''
# Declara uma matriz 3x3 vazia
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenche a matriz com os valores lidos pelo teclado
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digita um número para [{linha}, {coluna}]: '))

# Mostra a matriz no ecrã com a formatação correta
print('\n')
print('=' * 30)
print('{:^30}'.format('RESULTADOS'))
print('=' * 30)

for linha in range(3):
    for coluna in range(3):
        matriz_formatada = (f'[{matriz[linha][coluna]:^5}]') # Formatação para mostrar a matriz alinhada
        print('{:^10}'.format(matriz_formatada), end='')
    print()# Muda para a próxima linha após imprimir cada linha da matriz
