'''
103. Faz um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e quantos golos ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''


def ficha(nome='<desconhecido>', quantGolos=0):
    """
    --> Mostra a ficha de um jogador, com nome e quantidade de golos.
    :param nome: (opcional) nome do jogador.
    :param quantGolos: (opcional) número de golos marcados.
    :return: Sem retorno.
    """
    # Verifica se o nome está vazio e usa '<desconhecido>' por padrão
    if not nome.strip():  # strip() remove espaços em branco
        nome = '<desconhecido>'
    # Verifica se o valor de quantGolos não é válido e ajusta para 0
    if not isinstance(quantGolos, int):
        quantGolos = 0

    # Exibe a ficha do jogador
    print(f'O jogador {nome} marcou {quantGolos} golo(s).')


# Programa Principal
nome = input('Digita o nome do jogador: ').strip()  # strip() remove espaços em branco
# Usa try/except para evitar erro ao inserir um valor inválido
try:
    quantGolos = int(input('Quantidade de golos: '))
except ValueError:
    quantGolos = 0  # Se o utilizador não inserir um número, assume 0

# Chama a função com os valores fornecidos
ficha(nome, quantGolos)