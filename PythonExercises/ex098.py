'''
098. Faz um programa que tenha uma função chamada `contador()`, que recebe três parâmetros: início, fim e passo. O programa tem que realizar três contagens através da função criada:
- A) De 1 até 10, de 1 em 1.
- B) De 10 até 0, de 2 em 2.
- C) Uma contagem personalizada.
'''
from time import sleep
def contador(inicio, fim, passo):
    # Verifica se o passo é zero ou negativo, e ajusta se necessário
    if passo == 0:
        if inicio < fim:
            passo = 1
        else:
            passo= -1
    elif passo < 0:
        passo = -abs(passo)  # Garante que o passo seja negativo para contagens decrescentes
    else:
        passo = abs(passo)  # Garante que o passo seja positivo para contagens crescentes

    # Contagem crescente ou decrescente
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):  # Contagem crescente
            print(i, '-> ', end='')
            sleep(0.5)
    else:
        for i in range(inicio, fim - 1, passo):  # Contagem decrescente
            print(i, '-> ', end='')
            sleep(0.5)

    print('FIM')


# A) Contagem de 1 até 10 de 1 em 1
print('Contagem de 1 até 10 de 1 em 1:')
contador(1, 10, 1)

# B) Contagem de 10 até 0 de 2 em 2
print('\nContagem de 10 até 0 de 2 em 2:')
contador(10, 0, -2)

# C) Contagem personalizada
print('\nContagem personalizada:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
