'''
082.  Cria um programa que vai ler vários números e colocá-los numa lista. Depois disso, cria duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respetivamente. No final, mostra o conteúdo das três listas geradas.
'''
# Inicializa três listas: uma para todos os valores, uma para os pares e outra para os ímpares.
valores = []
par = []
impar = []

print('-' * 30)
print('{:^30}'.format('LISTA DE NÚMEROS'))
print('-' * 30)

# Pede ao utilizador quantos números ele deseja digitar.
vezes = int(input('Quantos números queres digitar? '))
print('-' * 30)

# Loop para ler os números e adicionar à lista principal.
for i in range(vezes):
    num = int(input(f'{i + 1}º número: '))
    valores.append(num)  # Adiciona o número à lista de valores.

    # Verifica se o número é par ou ímpar e adiciona à lista correspondente.
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print('\n', '{:^30}'.format('LISTA COMPLETA'))
print(f'Lista total: {valores}')
print('-' * 30)

print('\n', '{:^30}'.format('PARES'))
print(f'Lista dos pares: {par}')
print('-' * 30)

print('\n', '{:^30}'.format('ÍMPARES'))
print(f'Lista dos ímpares: {impar}')
print('-' * 30)
