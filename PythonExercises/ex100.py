'''
100. Faz um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e colocá-los dentro da lista, e a segunda função vai mostrar a soma de todos os valores pares sorteados pela função anterior.
'''
from random import randint

numeros = list()
parlista = list()


# Função que sorteia 5 números e os adiciona à lista
def sorteia(numeros):
    print('A sortear 5 números para a lista: ', end='')
    for i in range(5):
        num = randint(0, 10)  # Sorteia um número entre 0 e 10
        numeros.append(num)
        print(f'{num} ', end='', flush=True)
    print()  # Pula uma linha após a impressão dos números


# Função que soma os números pares
def somaPar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:  # Verifica se o número é par
            soma += valor
            parlista.append(valor)
    print(f'A soma dos valores pares de {numeros}, que são {parlista}, temos {soma}.')


# Chamar as funções
sorteia(numeros)  # Preenche a lista 'numeros' com 5 números sorteados
somaPar(numeros)  # Calcula a soma dos números pares da lista
