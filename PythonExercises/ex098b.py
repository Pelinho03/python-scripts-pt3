'''
098. Faz um programa que tenha uma função chamada `contador()`, que recebe três parâmetros: início, fim e passo. O programa tem que realizar três contagens através da função criada:
- A) De 1 até 10, de 1 em 1.
- B) De 10 até 0, de 2 em 2.
- C) Uma contagem personalizada.
'''
from time import sleep

# Função para realizar a contagem
def contador(i, f, p):
    # Verifica se o passo é negativo, transforma em positivo
    if p < 0:
        p *= -1

    # Evita que o passo seja zero, o que causaria um loop infinito
    if p == 0:
        p = 1

    # Exibe uma mensagem informando a contagem que será feita
    print('-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)  # Pausa para dar um efeito de espera antes de começar a contagem

    # Se o início for menor que o fim, faz uma contagem crescente
    if i < f:
        cont = i  # A variável cont vai controlar o início da contagem
        while cont <= f:  # Continua até atingir o valor final
            print(f'{cont} ', end='', flush=True)  # Imprime o valor atual da contagem
            sleep(0.5)  # Pausa de 0.5 segundos entre cada número para dar um efeito gradual
            cont += p  # Incrementa o contador com o valor do passo
        print('FIM!')  # Indica o fim da contagem

    # Se o início for maior que o fim, faz uma contagem decrescente
    else:
        cont = i  # A variável cont vai começar no valor inicial
        while cont >= f:  # Continua até atingir o valor final, mas decrescendo
            print(f'{cont} ', end='', flush=True)  # Imprime o valor atual da contagem
            sleep(0.5)  # Pausa de 0.5 segundos entre cada número para dar o efeito gradual
            cont -= p  # Decrementa o contador com o valor do passo
        print('FIM!')  # Indica o fim da contagem


# Chama a função contador com os valores padrão
contador(1, 10, 1)  # A) Contagem de 1 até 10 de 1 em 1
contador(10, 0, 2)  # B) Contagem de 10 até 0 de 2 em 2

# Mensagem para pedir contagem personalizada
print('-' * 20)
print('Agora é a tua vez de personalizar a contagem!')

# Obtém os valores de início, fim e passo do utilizador
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

# Chama a função contador com os valores personalizados
contador(ini, fim, pas)
