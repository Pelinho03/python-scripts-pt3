'''
106. Faz um mini-sistema que utilize o Interactive Help do Python. O utilizador vai digitar o comando e o manual vai aparecer. Quando o utilizador digitar a palavra 'FIM', o programa será encerrado. Importante: usa cores.
'''
from time import sleep

# Definição das cores usadas no terminal
c = ('\033[m',  # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m',  # 6 - branco
     '')


# Função para mostrar o manual de um comando/biblioteca
def ajuda(com):
    titulo(f'Acessar ao manual do comando \'{com}\'', 4)  # Mostra o título com cor azul
    print(c[6], end='')  # Muda a cor do texto para branco
    help(com)  # Mostra a documentação do comando usando o help do Python
    print(c[0], end='')  # Reseta as cores para o padrão
    sleep(2)


# Função para imprimir um título estilizado
def titulo(msg, cor=0):
    tam = len(msg) + 4  # Calcula o tamanho da linha de acordo com a mensagem
    print(c[cor], end='')  # Aplica a cor desejada
    print('~' * tam)  # Imprime a linha superior
    print(f'  {msg}')  # Imprime a mensagem centralizada
    print('~' * tam)  # Imprime a linha inferior
    print(c[0], end='')  # Reseta as cores para o padrão
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)  # Título inicial com cor verde
    comando = str(input('Função ou Biblioteca > '))  # Recebe o comando do utilizador
    if comando.upper() == 'FIM':  # Se o comando for 'FIM', o programa termina
        break
    else:
        ajuda(comando)  # Chama a função de ajuda para o comando inserido
titulo('ATÉ LOGO!', 1)  # Mensagem de despedida com cor vermelha
