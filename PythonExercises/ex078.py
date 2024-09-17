'''
078. Fazer um programa que leia 5 valores numéricos e guarde-os numa lista. No final, mostre qual foi o maior e o menor valor digitado e as respetivas posições na lista.
'''
# Inicializar as variáveis maior e menor com o primeiro valor da lista.
# Isso garante que, ao iniciar o loop, temos uma base para comparar.
maior = menor = 0
lista = [int(input('Digita um número: ')),
         int(input('Digita outro número: ')),
         int(input('Digita outro número: ')),
         int(input('Digita mais um número: ')),
         int(input('Digita o último número: '))]

# Inicializar o maior e menor com o primeiro valor da lista.
# Desta forma, já temos um ponto de comparação válido.
maior = menor = lista[0]

# Loop para percorrer a lista e encontrar os valores máximos e mínimos.
for n in lista:
    if n > maior:  # Verifica se o valor atual é maior que o armazenado em 'maior'.
        maior = n
    if n < menor:  # Verifica se o valor atual é menor que o armazenado em 'menor'.
        menor = n

# Imprimir os resultados
print('\n')
print('=' * 30)
print('{:^30}'.format('RESULTADOS'))  # Formatação do título de resultados
print('=' * 30)
print(lista)  # Mostrar a lista completa digitada pelo utilizador
print('=' * 30)

# Mostrar o maior valor e a sua posição na lista
print(f'O maior valor digitado foi {maior} na {lista.index(maior) + 1}ª posição.')
# Mostrar o menor valor e a sua posição na lista
print(f'O menor valor digitado foi {menor} na {lista.index(menor) + 1}ª posição.')
