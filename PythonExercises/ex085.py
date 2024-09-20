'''
085. Cria um programa onde o utilizador possa digitar sete valores numéricos e registá-los numa lista única que mantenha separados os valores pares e ímpares. No final, mostra os valores pares e ímpares em ordem crescente.
'''
valores = [[], []]  # A primeira lista será para pares, a segunda para ímpares

for i in range(7):
    num = int(input(f'{i + 1}º valor: '))

    # Verifica se o número é par ou ímpar e adiciona à lista apropriada
    if num % 2 == 0:
        valores[0].append(num)  # Adiciona à lista de pares (índice 0)
    else:
        valores[1].append(num)  # Adiciona à lista de ímpares (índice 1)

# Ordena os valores dentro de cada lista
valores[0].sort()  # Ordena a lista de pares
valores[1].sort()  # Ordena a lista de ímpares

# Mostra os valores pares e ímpares ordenados
print(f'Valores pares: {valores[0]}')
print(f'Valores ímpares: {valores[1]}')
