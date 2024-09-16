'''
075. Desenvolver um programa que leia quatro valores pelo teclado e guarde-os numa tupla. No final, mostre:
- A) Quantas vezes apareceu o valor 9.
- B) Em que posição foi digitado o primeiro valor 3.
- C) Quais foram os números pares.
'''
# Ler quatro valores e guardá-los numa tupla
num1 = int(input('Insere o 1º valor: '))
num2 = int(input('Insere o 2º valor: '))
num3 = int(input('Insere o 3º valor: '))
num4 = int(input('Insere o 4º valor: '))

# Criar a tupla com os valores inseridos
numeros = (num1, num2, num3, num4)

# A) Contar quantas vezes o número 9 aparece
print(f'O número 9 apareceu {numeros.count(9)} vez(es).')

# B) Verificar a posição do primeiro número 3 (se existir)
if 3 in numeros:
    print(f'O primeiro 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi inserido.')

# C) Mostrar os números pares
pares = tuple(num for num in numeros if num % 2 == 0)
print(f'Os números pares foram: {pares}' if pares else 'Nenhum número par foi inserido.')
