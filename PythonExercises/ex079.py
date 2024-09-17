'''
079. Cria um programa onde o utilizador possa digitar vários valores numéricos e registá-los numa lista. Caso o número já exista na lista, ele não será adicionado. No final, serão exibidos todos os valores únicos introduzidos, em ordem crescente.
'''
# Inicializa uma lista vazia para armazenar os valores únicos.
valores = []

while True:
    # Pede ao utilizador para digitar um número.
    num = int(input('Digita um número: '))

    # Verifica se o número já está na lista.
    if num not in valores:
        # Se não estiver, adiciona à lista e confirma ao utilizador.
        valores.append(num)
        print(f'Valor {num} adicionado com sucesso!')
    else:
        # Se o número já existir, informa o utilizador.
        print('Valor duplicado, não adicionado!')

    print('-' * 30)

    # Pergunta ao utilizador se quer continuar a adicionar números.
    escolha = str(input('Pretendes continuar? [S/N] ')).strip().upper()[0]

    # Se o utilizador digitar 'N', o loop é encerrado.
    if escolha == 'N':
        break
    print('-' * 30)

# Exibe os valores introduzidos em ordem crescente.
print('\n')
print(f'Os valores inseridos foram {sorted(valores)}')
