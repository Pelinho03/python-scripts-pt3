'''
075. Desenvolver um programa que leia quatro valores pelo teclado e guarde-os numa tupla. No final, mostre:
- A) Quantas vezes apareceu o valor 9.
- B) Em que posição foi digitado o primeiro valor 3.
- C) Quais foram os números pares.
'''
# Lê quatro números do utilizador e armazena-os numa tupla
num = (int(input('Digita um número: ')),
       int(input('Digita outro número: ')),
       int(input('Digita mais um número: ')),
       int(input('Digita o último número: ')))

# Mostra os valores digitados
print('\n')
print('=' * 30)
print('{:^30}'.format('VALORES DIGITADOS'))
print('=' * 30)
print(f'Digitaste os valores {num}.')

# Contagem de quantas vezes o número 9 apareceu
print('\n')
print('=' * 30)
print(f'O valor 9 apareceu {num.count(9)} vez(es).')

# Verificar a posição do primeiro número 3
print('\n')
print('=' * 30)
if 3 in num:
    # Se o 3 estiver na tupla, mostrar a posição (índice + 1 para posição humana)
    print(f'O valor 3 apareceu na {num.index(3) + 1} posição.')
else:
    # Se não estiver presente, mostrar mensagem
    print('O valor 3 não foi digitado em nenhuma posição.')

# Mostrar todos os números pares digitados
print('\n')
print('=' * 30)
print('Os valores pares digitados foram ', end='')

# Itera sobre os números da tupla e verifica quais são pares
for n in num:
    if n % 2 == 0:
        print(n, end=' ')  # Se for par, exibe o número
