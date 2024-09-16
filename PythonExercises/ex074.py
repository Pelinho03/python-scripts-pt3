'''
074.  Criar um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostra a listagem de números gerados e também indicar o menor e o maior valor que estão na tupla.
'''
from random import randint

# Gerar cinco números aleatórios e colocá-los numa tupla
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

# Exibir os números gerados
print('=' * 50)
print('Números gerados: ', end='')
for num in numeros:
    print(f'{num} ', end='-> ')
print('FIM')
print('=' * 50)

# Exibir o maior e o menor número
print(f'O maior número gerado foi: {max(numeros)}')
print(f'O menor número gerado foi: {min(numeros)}')
print('=' * 50)
