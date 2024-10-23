'''
103. Faz um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e quantos golos ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''


def ficha(jog='<desconhecido>', golo=0):
    # Mostra a ficha do jogador com nome e quantidade de golos
    print(f'O {jog} fez {golo} golo(s) no campeonato.')


# Programa principal
n = str(input('Nome do Jogador: '))  # Lê o nome do jogador
g = str(input('Número de Golos: '))  # Lê a quantidade de golos

# Verifica se a entrada para golos é um número
if g.isnumeric():
    g = int(g)  # Converte para inteiro se for numérico
else:
    g = 0  # Caso contrário, atribui 0

# Verifica se o nome foi preenchido ou não
if n.strip() == '':
    ficha(golo=g)  # Chama a função sem nome (usa valor padrão)
else:
    ficha(n, g)  # Chama a função com nome e número de golos
