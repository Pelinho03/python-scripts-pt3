'''
099. Faz um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros. O programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep


def maior(*num):
    cont = 0
    maior_valor = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)  # Apenas para simular uma pausa e fazer o programa mais dinâmico
        if cont == 0:  # Primeiro número é considerado o maior inicialmente
            maior_valor = valor
        else:
            if valor > maior_valor:  # Comparar com o valor atual do maior
                maior_valor = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')
    print('-=' * 30)


# Testes da função
maior(2, 9, 4, 5, 7, 1)
maior(1, 2)
maior(6)
maior()  # Caso não passe nenhum valor
